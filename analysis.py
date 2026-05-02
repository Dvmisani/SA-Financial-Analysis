"""
SA Business Financial Analysis
================================
Author  : Dumisani Abrahm Baloyi
GitHub  : https://github.com/Dvmisani
Purpose : Analyse monthly revenue, expenses and profitability trends
          for a South African SME using Python and pandas.

Tools used : pandas, matplotlib, seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", palette="deep")
GOLD   = "#B8962E"
NAVY   = "#1B2A4A"
RED    = "#C0392B"
GREEN  = "#1E8449"

# ── Load Data ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/sa_business_financials.csv")

# Create a proper date column for time-series plotting
df["Date"] = pd.to_datetime(df["Month"] + " " + df["Year"].astype(str), format="%B %Y")
df.sort_values("Date", inplace=True)
df.reset_index(drop=True, inplace=True)

# Calculate total expenses and net profit
expense_cols = ["Salaries", "Rent", "Utilities", "Marketing", "Supplies", "Tax"]
df["Total_Expenses"] = df[expense_cols].sum(axis=1)
df["Net_Profit"]     = df["Revenue"] - df["Total_Expenses"]
df["Profit_Margin"]  = (df["Net_Profit"] / df["Revenue"] * 100).round(2)

# ── Summary Statistics ─────────────────────────────────────────────────────
print("=" * 60)
print("  SA BUSINESS FINANCIAL ANALYSIS — SUMMARY")
print("=" * 60)

for year in df["Year"].unique():
    subset = df[df["Year"] == year]
    print(f"\n  {year}:")
    print(f"    Total Revenue      : R{subset['Revenue'].sum():>12,.0f}")
    print(f"    Total Expenses     : R{subset['Total_Expenses'].sum():>12,.0f}")
    print(f"    Net Profit         : R{subset['Net_Profit'].sum():>12,.0f}")
    print(f"    Avg Profit Margin  : {subset['Profit_Margin'].mean():>11.1f}%")
    print(f"    Best Month         : {subset.loc[subset['Revenue'].idxmax(), 'Month']}")

print("\n" + "=" * 60)

# ── Chart 1: Monthly Revenue vs Expenses ──────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(df["Date"], df["Revenue"],        color=NAVY,  linewidth=2.5, marker="o", markersize=5, label="Revenue")
ax.plot(df["Date"], df["Total_Expenses"], color=GOLD,  linewidth=2.5, marker="s", markersize=5, label="Total Expenses")
ax.fill_between(df["Date"], df["Revenue"], df["Total_Expenses"],
                where=df["Revenue"] >= df["Total_Expenses"],
                alpha=0.12, color=GREEN, label="Profit Zone")

ax.set_title("Monthly Revenue vs Total Expenses (2023–2024)", fontsize=14, fontweight="bold", color=NAVY, pad=14)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Amount (ZAR)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R{x/1000:.0f}k"))
ax.legend(fontsize=10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/1_revenue_vs_expenses.png", dpi=150)
plt.close()
print("  Chart saved: 1_revenue_vs_expenses.png")

# ── Chart 2: Net Profit Trend ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 4))

colors = [GREEN if p >= 0 else RED for p in df["Net_Profit"]]
ax.bar(df["Date"], df["Net_Profit"], color=colors, width=20, edgecolor="white", linewidth=0.5)
ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Monthly Net Profit (2023–2024)", fontsize=14, fontweight="bold", color=NAVY, pad=14)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Net Profit (ZAR)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R{x/1000:.0f}k"))
plt.xticks(df["Date"], [d.strftime("%b %Y") for d in df["Date"]], rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/2_net_profit_trend.png", dpi=150)
plt.close()
print("  Chart saved: 2_net_profit_trend.png")

# ── Chart 3: Expense Breakdown (Average) ──────────────────────────────────
avg_expenses = df[expense_cols].mean()
explode = [0.05] * len(expense_cols)
colors_pie = [NAVY, GOLD, "#5D8AA8", "#A0522D", "#6B8E23", "#708090"]

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    avg_expenses, labels=expense_cols, autopct="%1.1f%%",
    startangle=140, explode=explode, colors=colors_pie,
    textprops={"fontsize": 11}
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_color("white")
    at.set_fontweight("bold")
ax.set_title("Average Monthly Expense Breakdown", fontsize=14, fontweight="bold", color=NAVY, pad=20)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/3_expense_breakdown.png", dpi=150)
plt.close()
print("  Chart saved: 3_expense_breakdown.png")

# ── Chart 4: Year-on-Year Revenue Comparison ──────────────────────────────
months_order = ["January","February","March","April","May","June",
                "July","August","September","October","November","December"]
df["Month"] = pd.Categorical(df["Month"], categories=months_order, ordered=True)
pivot = df.pivot_table(index="Month", columns="Year", values="Revenue", aggfunc="sum")
pivot = pivot.reindex(months_order)

fig, ax = plt.subplots(figsize=(14, 5))
x = range(len(pivot))
bar_width = 0.35
ax.bar([i - bar_width/2 for i in x], pivot[2023], width=bar_width, color=NAVY,  label="2023", edgecolor="white")
ax.bar([i + bar_width/2 for i in x], pivot[2024], width=bar_width, color=GOLD,  label="2024", edgecolor="white")
ax.set_title("Year-on-Year Monthly Revenue Comparison", fontsize=14, fontweight="bold", color=NAVY, pad=14)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Revenue (ZAR)", fontsize=11)
ax.set_xticks(list(x))
ax.set_xticklabels([m[:3] for m in months_order], fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"R{v/1000:.0f}k"))
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/4_yoy_comparison.png", dpi=150)
plt.close()
print("  Chart saved: 4_yoy_comparison.png")

# ── Chart 5: Profit Margin Over Time ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(df["Date"], df["Profit_Margin"], color=NAVY, linewidth=2.5, marker="D", markersize=5)
ax.fill_between(df["Date"], df["Profit_Margin"], alpha=0.15, color=NAVY)
ax.axhline(df["Profit_Margin"].mean(), color=GOLD, linestyle="--", linewidth=1.5,
           label=f"Average: {df['Profit_Margin'].mean():.1f}%")
ax.set_title("Profit Margin Trend (2023–2024)", fontsize=14, fontweight="bold", color=NAVY, pad=14)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Profit Margin (%)", fontsize=11)
ax.legend(fontsize=10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/5_profit_margin.png", dpi=150)
plt.close()
print("  Chart saved: 5_profit_margin.png")

print("\n  All charts saved to /output/")
print("=" * 60)
