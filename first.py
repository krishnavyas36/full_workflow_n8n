import duckdb
import pandas as pd
import matplotlib.pyplot as plt

# === Step 1: Load CSV files ===
sales_df = pd.read_csv('data/train.csv')
features_df = pd.read_csv('data/features.csv')
stores_df = pd.read_csv('data/stores.csv')

# === Step 2: Set up DuckDB in-memory connection ===
con = duckdb.connect(database=':memory:')
con.register('sales', sales_df)
con.register('features', features_df)
con.register('stores', stores_df)

# === Step 3: Query - Average Weekly Sales by Store ===
query_store_sales = """
SELECT s.Store, ROUND(AVG(sa.Weekly_Sales), 2) AS AvgWeeklySales
FROM sales sa
JOIN stores s ON sa.Store = s.Store
GROUP BY s.Store
ORDER BY AvgWeeklySales DESC;
"""
result_df = con.execute(query_store_sales).df()
print("Top 5 Stores by Avg Weekly Sales:\n", result_df.head(), "\n")

# === Query - Average Sales by Store Type ===
query_store_type = """
SELECT st.Type, ROUND(AVG(s.Weekly_Sales), 2) AS AvgSales
FROM sales s
JOIN stores st ON s.Store = st.Store
GROUP BY st.Type
ORDER BY AvgSales DESC;
"""
store_type_sales = con.execute(query_store_type).df()
print("Average Sales by Store Type:\n", store_type_sales, "\n")

# === Query - Monthly Sales Trend ===
query_monthly_sales = """
SELECT STRFTIME(CAST(s.Date AS DATE), '%Y-%m') AS YearMonth,
       ROUND(SUM(s.Weekly_Sales), 2) AS TotalSales
FROM sales s
GROUP BY YearMonth
ORDER BY YearMonth;
"""
monthly_sales = con.execute(query_monthly_sales).df()

# === Step 4: Plot Monthly Sales ===
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['TotalSales'], marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.title("Monthly Total Sales")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


from prophet import Prophet

# === Step 5: Prepare Data for Forecasting ===
# We'll forecast total weekly sales across all stores
query_weekly_sales = """
SELECT CAST(Date AS DATE) AS ds, 
       SUM(Weekly_Sales) AS y
FROM sales
GROUP BY ds
ORDER BY ds;
"""
weekly_sales = con.execute(query_weekly_sales).df()

# === Step 6: Fit Prophet Model ===
model = Prophet()
model.fit(weekly_sales)

# Forecast for next 12 weeks (~3 months)
future = model.make_future_dataframe(periods=12, freq='W')
forecast = model.predict(future)

# === Step 7: Plot Forecast ===
fig = model.plot(forecast)
plt.title("Weekly Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Optional: Show forecast table
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))

import ollama

# Prepare short summary data (last 12 forecasted weeks)
summary_df = forecast[['ds', 'yhat']].tail(12)
summary_text = summary_df.to_string(index=False)

# Build prompt for Ollama
prompt = f"""
You are a business analyst. Based on the following weekly sales forecast data, summarize the expected trend for the next 12 weeks.

{summary_text}

Highlight any increases or decreases, seasonality (e.g. holidays), and any implications for inventory or promotion planning.
Keep it professional and under 120 words.
"""

# Send to Ollama (uses the default model you pulled)
response = ollama.chat(model='llama2', messages=[
    {'role': 'user', 'content': prompt}
])

# Print generated insight
print("\n📊 Executive Summary:\n")
print(response['message']['content'])


# Create a folder called 'exports' in your project directory first

# 1. Store-level average sales
result_df.to_csv('exports/avg_sales_by_store.csv', index=False)

# 2. Store-type sales
store_type_sales.to_csv('exports/avg_sales_by_type.csv', index=False)

# 3. Monthly total sales
monthly_sales.to_csv('exports/monthly_sales.csv', index=False)

# 4. Weekly sales forecast
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12).to_csv('exports/forecast_summary.csv', index=False)


import requests

# Trigger n8n webhook
requests.get("https://krishnavyasdesugari.app.n8n.cloud/webhook-test/run-forecast")
