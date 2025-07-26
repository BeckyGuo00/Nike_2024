# Nike 2024 Global Market Analysis – A UX Research Case Study

## 📌 Overview
This project explores global sales trends for Nike in 2024 through the lens of **user-centered data exploration**. The primary goal was to design and evaluate a responsive dashboard that allows stakeholders (e.g., product managers, regional analysts, designers) to identify actionable trends based on **geography, category, and pricing**.

Built with **Streamlit**, the dashboard enables intuitive exploration and interaction with dynamic data visualizations.

---

## 🎯 UX Research Objective

**How can we empower regional Nike teams to quickly identify key sales insights and user behavior patterns through visual tools?**

This project simulates how UX research can inform dashboard design and how insights derived from data can drive **user interface improvements** and **strategic decisions**.

---

## 👥 Target Users

- **Regional Marketing Teams**: Need insights into top-performing products and pricing patterns by region and time.
- **Product Designers**: Benefit from understanding category-specific interest across geographies.
- **Business Analysts**: Use filtering tools to explore shifts in revenue and category performance.

---

## 🧪 Methodology

- **Exploratory Data Analysis**: Used Python (Pandas, Seaborn, Plotly) to extract patterns from structured sales data.
- **Dashboard Design**: Built interactive filters and visualizations using **Streamlit** to reflect user needs.
- **Usability Simulation**: Informally tested interface with peers, revised for clarity and interactivity.

---

## 🔍 Key UX Findings

- **Clear preference shifts** between price tiers across regions.
- **Time-sensitive category spikes** (e.g., Q1 vs. Q4 revenue patterns).
- Users preferred fewer, clearer filter options over dense visuals.
- Regional teams benefit from **month-by-month insights** to adjust campaign timing.

---

## 💡 Design Recommendations

- **Incorporate User Segments**: Allow filtering by user profiles or usage scenarios.
- **Narrative Visualization Layer**: Integrate short written insights above visuals.
- **Interactive Insights Tooltips**: Add hover text with user-impact explanations.

---

## 🖥️ Dashboard Features

- **Regional Filtering**: Select continent or country to see localized data trends.
- **Dynamic Visuals**: Line charts, bar plots, and treemaps updating in real time.
- **Category Breakdown**: Explore product performance by price tier and product line.

---

## 📂 Folder Structure

```
Nike_2024/
├── README.md
├── data/
│   └── nike_global_2024.csv
├── notebooks/
│   └── exploratory_analysis.ipynb
├── dashboard/
│   └── streamlit_app.py
├── images/
│   └── dashboard_demo.gif
└── requirements.txt
```

---

## 📊 Sample Visualizations

Add screenshots or a `.gif` demo here:
- Dashboard UI with filters
- Line chart of monthly revenue
- Tree map of regional pricing breakdowns

---
## Installation

1. Clone this repository:
```bash
git clone https://github.com/BeckyGuo00/Nike_2024.git

```

2. Install required libraries using pip:
```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following content if you haven't done so:

```
streamlit
pandas
plotly
openpyxl
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 🔄 Future Work

- Conduct formal usability tests
- Build user personas for targeted analysis
- Integrate sentiment or feedback data from consumers

---

## 🙋‍♀️ Author

Fanyu Guo – [GitHub](https://github.com/BeckyGuo00) | [Email](mailto:beckyguo01@gmail.com)
