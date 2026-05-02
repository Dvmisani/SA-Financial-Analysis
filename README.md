# 📊 SA Business Financial Analysis

A Python-based data analysis project that examines the monthly financial performance of a South African SME — covering revenue, expenses, net profit, and profitability trends across 2023 and 2024.

Built as part of my data analytics portfolio to demonstrate practical skills in Python, pandas, and data visualisation.

---

## 📌 Project Objectives

- Analyse monthly revenue and expense patterns
- Calculate net profit and profit margin over time
- Identify best and worst performing months
- Compare year-on-year (2023 vs 2024) financial performance
- Visualise expense category breakdowns

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| pandas | Data loading, cleaning and analysis |
| matplotlib | Chart and graph generation |
| seaborn | Visual styling |

---

## 📁 Project Structure

```
SA-Financial-Analysis/
│
├── data/
│   └── sa_business_financials.csv   # Monthly financial dataset
│
├── output/                          # Generated charts (auto-created)
│   ├── 1_revenue_vs_expenses.png
│   ├── 2_net_profit_trend.png
│   ├── 3_expense_breakdown.png
│   ├── 4_yoy_comparison.png
│   └── 5_profit_margin.png
│
├── analysis.py                      # Main analysis script
├── requirements.txt
└── README.md
```

---

## 📈 Charts Generated

1. **Revenue vs Total Expenses** — line chart with profit zone shading
2. **Monthly Net Profit** — bar chart highlighting profitable months
3. **Expense Breakdown** — pie chart of average monthly cost categories
4. **Year-on-Year Comparison** — grouped bar chart (2023 vs 2024)
5. **Profit Margin Trend** — line chart with average margin reference line

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Dvmisani/SA-Financial-Analysis.git
cd SA-Financial-Analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis
```bash
python analysis.py
```

Charts will be saved to the `/output/` folder.

---

## 📊 Key Findings

- Revenue grew by **12.6%** from 2023 to 2024
- Net profit improved from **R568,750** (2023) to **R663,800** (2024)
- Average profit margin increased from **41.2%** to **42.6%**
- **Salaries** represent the largest expense category (~55% of total costs)
- **December** was consistently the highest revenue month in both years

---

## 👤 Author

**Dumisani Abrahm Baloyi**
- 📧 dvmisani@gmail.com
- 🐙 [github.com/Dvmisani](https://github.com/Dvmisani)
- 📍 Pretoria, Gauteng, South Africa

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
