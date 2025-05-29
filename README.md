# 🛒 Retail Sales Forecasting & Automation Project

A full-stack, real-world data analysis project to explore, forecast, and automate retail sales insights using Walmart store data. This project integrates data querying, machine learning, business intelligence dashboards, and LLM-generated executive summaries with an automated email pipeline.

---

## 🚀 Project Overview

This project analyzes historical weekly sales data from multiple Walmart stores to:

- Identify high-performing stores and store types
- Analyze monthly and holiday-driven sales trends
- Forecast future weekly sales using Facebook Prophet
- Generate executive summaries using Ollama (LLaMA2)
- Automate reporting via email using n8n

---

## 🧰 Tools & Technologies

| Component        | Tool/Library                     |
|------------------|----------------------------------|
| **Data Analysis**| Python, Pandas, DuckDB           |
| **Forecasting**  | Prophet                          |
| **LLM Summary**  | Ollama with LLaMA2               |
| **Visualization**| Power BI                         |
| **Automation**   | n8n (Cloud version)              |
| **Scheduling**   | Cron triggers or webhook-based   |

---

## 📊 Key Features

- SQL-style querying with DuckDB
- Forecasts weekly sales 12 weeks into the future
- LLM-generated plain English business insights
- Power BI dashboard with trend, type, and forecast visuals
- Automated weekly summary delivery via email (SMTP + n8n)

---

## 📂 Project Structure

retail-sales-forecasting/
│
├── data/ # Raw Kaggle data
│ ├── train.csv
│ ├── features.csv
│ └── stores.csv
│
├── exports/ # Outputs for dashboards & email
│ ├── forecast_summary.csv
│ └── summary.txt
│
├── dashboard/ # Power BI dashboard (.pbix)
│
├── first.py # Python script for EDA + forecast
│
├── README.md # This file


---

## 📈 Dashboard Visuals (Power BI)

| Visual                     | Dataset                  | Chart Type         | Purpose                    |
|----------------------------|--------------------------|--------------------|----------------------------|
| Avg Sales by Store         | `avg_sales_by_store.csv` | Horizontal Bar     | Compare top stores         |
| Avg Sales by Store Type    | `avg_sales_by_type.csv`  | Donut              | Type-level distribution    |
| Monthly Sales Trend        | `monthly_sales.csv`      | Line Chart         | Seasonality and growth     |
| Weekly Forecast (Future)   | `forecast_summary.csv`   | Line w/ confidence | Business planning          |

---

## 📬 Email Automation (n8n Cloud)

- Triggered via Cron or local Python webhook
- Sends forecast CSV + executive summary via email
- Configured using Gmail SMTP with app passwords

---

## 🔮 Sample LLM Insight (Ollama)

> “Weekly sales are projected to remain stable above $45M for the next 12 weeks, with a noticeable increase in mid-December due to holiday promotions. Inventory planning should accommodate the December spike followed by a January dip.”

---

## ✅ How to Run

1. Clone this repo
2. Run `first.py` (requires Python 3.10+)
3. View output CSVs in `/exports`
4. Open `RetailSalesDashboard.pbix` in Power BI
5. Use n8n Cloud to automate sending summaries weekly

---

## 🧠 Future Enhancements

- Forecast per store and department
- Upload reports to cloud storage
- Build a Streamlit app version
- Add anomaly detection

---

## 📎 Credits

- Dataset: Walmart Sales Forecasting ([Kaggle Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting))
- Tools: Prophet (Meta), Ollama (LLM), Power BI, DuckDB, n8n

---

## 🧳 Author

**Kriahnavyas**  
Data Analyst | Python + SQL + BI + Automation  
[LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

