# HealthKart Influencer Campaign ROI Dashboard

This is a Streamlit-based dashboard designed to help teams analyze influencer marketing campaigns through interactive visualizations, ROI calculations, and payout insights. It supports dynamic data uploads and can run on both real and simulated datasets.

---
# Live Link

https://healthkartdashboard-harsh.streamlit.app/

---
## Project Structure

```
healthkart_dashboard/
├── app.py                # Main Streamlit application
├── data_simulation.py    # Script to generate sample CSV data
├── utils.py              # Common data processing utilities
├── requirements.txt      # List of required Python packages
├── README.md             # This file
├── insights_summary.md   # Key insights in Markdown format
└── sample_data/
    ├── influencers.csv
    ├── posts.csv
    ├── tracking_data.csv
    └── payouts.csv
```

---

## Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone https://github.com/harshtr8/healthkart_dashboard.git
cd healthkart_dashboard
```

Or download as ZIP and extract it.

---

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Generate Sample Data

```bash
python data_simulation.py
```

This will create sample CSVs in the sample_data/ folder.

---

### 5. Run the Streamlit App

```bash
streamlit run app.py
```

Then go to http://localhost:8501 in your browser.

---

## How to Use

- Start with Sample Data  
  Sample datasets are provided to explore dashboard functionality.

- Upload Your Data  
  Use sidebar widgets to upload your influencers.csv, posts.csv, tracking_data.csv, and payouts.csv.

- Filter by Categories  
  Select specific brands, platforms, influencers, or product categories to narrow the analysis.

- View ROI & Performance  
  Visual summaries of reach, engagement, revenue, and ROAS for each influencer/post.

- Export Insights  
  Use built-in buttons to export analytics as CSV.

---

## Data Model & Schema

The dashboard expects four CSV files with the following formats:

### 1. influencers.csv

| ID | name | category | gender | follower_count | platform |
|----|------|----------|--------|----------------|----------|

### 2. posts.csv

| influencer_id | platform | date | URL | caption | reach | likes | comments |
|---------------|----------|------|-----|---------|-------|-------|----------|

### 3. tracking_data.csv

| source | campaign | influencer_id | user_id | product | date | orders | revenue |
|--------|----------|----------------|---------|---------|------|--------|---------|

### 4. payouts.csv

| influencer_id | basis | rate | orders | total_payout |
|---------------|-------|------|--------|---------------|

---

## Core Features

- Dynamic Uploads: Upload your own CSV datasets and get real-time insights.
- Filtering Options: Slice and dice by platform, campaign, product, or influencer category.
- ROI Tracking: Displays total and incremental ROAS (Return on Ad Spend).
- Influencer Insights: View performance by creator and optimize for future campaigns.
- Export Support: Download analytics tables as CSV.
- Insight Summaries: Check insights_summary.md for highlights.

---

## Assumptions

- Default analysis uses simulated data unless replaced by user-uploaded files.
- ROAS baseline logic can be customized per campaign.
- Only .csv uploads are currently supported.
- Data type and header integrity is necessary for proper analytics.

---

## Sample Insights (from insights_summary.md)

- Instagram Fitness Influencers have the highest ROI for protein-based products.
- Payouts based on Orders are more efficient for micro-influencers.
- Around 20% of influencers deliver sub-optimal ROAS — a key area for optimization.

---

## Troubleshooting

- FileNotFoundError: Run python data_simulation.py to regenerate sample files.
- ModuleNotFoundError: Activate the virtual environment and re-run pip install -r requirements.txt.
- Missing Export Button: Ensure Streamlit version ≥1.10 and button logic exists in the code.

---

## Extending the Project

- Add Excel support with pandas.read_excel()
- Improve data validation and error handling
- Add login/auth for campaign managers
- Integrate with APIs for real-time influencer performance tracking

---

## License

This project is open source and free to use for educational or internal business analysis purposes.

---

## Developed By

Harsh Tripathi  
As part of HealthKart Internship Assignment – July 2025

---
