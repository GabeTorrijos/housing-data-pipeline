# 🏠 Housing Data Pipeline

A web-based data pipeline tool that pulls real-time housing and mortgage data directly from the Federal Reserve (FRED API) and displays it with interactive charts and CSV export.

## 📊 Features

- Pull live data from the Federal Reserve (FRED)
- 4 housing datasets: Median Home Price, 30-Year Mortgage Rate, Housing Starts, Home Ownership Rate
- Custom date range selector
- Interactive line chart visualization
- One-click CSV export for use in future ML projects

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Data Source:** FRED API (Federal Reserve Bank of St. Louis)

## 🚀 How to Run

1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Get a free API key from [FRED](https://fred.stlouisfed.org/docs/api/api_key.html)
4. Create a `.env` file in the root folder: FRED_API_KEY=your_api_key_here
5. Run the app: python3app.py
6. Open your browser at `http://127.0.0.1:5000`

## 📁 Project Structure

housing-data-pipeline/
├── app.py
├── requirements.txt
├── .env (not included - see setup above)
├── .gitignore
└── templates/
└── index.html

## 📈 Data Sources

All data is sourced from the [FRED API](https://fred.stlouisfed.org/) provided by the Federal Reserve Bank of St. Louis.