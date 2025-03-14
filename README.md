# Nike 2024 Global Market Data Analysis Dashboard

## Overview
This Streamlit application provides interactive visualization and analysis of Nike's global sales data for 2024. Users can dynamically explore sales data across different regions, months, product categories, and pricing tiers using an intuitive and interactive interface.

## Features
- **Interactive filtering** by region and month.
- **Dynamic charts:**
  - Bar charts to compare revenue by Main Category, Sub Category, Product Line, and Price Tier.
  - Line chart for Time Series Analysis by month.
  - Hierarchical TreeMap visualization for revenue breakdown.
- Downloadable tables and data files.

## Prerequisites

Ensure Python 3.7+ is installed.

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

## Usage

### Running the Application

Navigate to your project directory and run the app with:

```bash
streamlit run nike_streamlit.py
```

The application will open in a new browser tab automatically.

## Repository Structure
```
nike_streamlit/
├── data/                        # Directory to store datasets (e.g., nike_sales_2024.csv)
├── nike_streamlit.py           # Streamlit application script
├── requirements.txt            # Project dependencies
└── README.md                   # This README file
```

## Using Your Own Data

Upload your CSV, TXT, XLSX, or XLS files directly within the Streamlit app or place them inside the `data` directory for automatic loading.

## Running the App

Launch the app locally with Streamlit:

```bash
streamlit run nike_streamlit.py
```

Your app should automatically open in a new browser tab. If not, manually navigate to `http://localhost:8501`.

Enjoy exploring your Nike market data interactively!
