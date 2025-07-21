import streamlit as st
import pandas as pd
from utils import load_data, roas, incremental_roas

st.set_page_config(page_title="HealthKart Influencer ROI Dashboard", layout="wide")
st.title("HealthKart Influencer Campaign ROI Dashboard")

# Data Loaders
@st.cache_data
def get_data():
    return load_data()

influencers, posts, tracking, payouts = get_data()

# Sidebar: Data Upload Option
st.sidebar.header("Upload Custom Data")
uploaded_infl = st.sidebar.file_uploader("Influencers", type=["csv"])
uploaded_posts = st.sidebar.file_uploader("Posts", type=["csv"])
uploaded_tracking = st.sidebar.file_uploader("Tracking Data", type=["csv"])
uploaded_payouts = st.sidebar.file_uploader("Payouts", type=["csv"])

if uploaded_infl and uploaded_posts and uploaded_tracking and uploaded_payouts:
    influencers = pd.read_csv(uploaded_infl)
    posts = pd.read_csv(uploaded_posts)
    tracking = pd.read_csv(uploaded_tracking)
    payouts = pd.read_csv(uploaded_payouts)

# --- Dashboard Filters ---
brands = tracking['source'].unique()
products = tracking['product'].unique()
platforms = influencers['platform'].unique()

brand_selected = st.sidebar.multiselect("Brand", brands, default=list(brands))
product_selected = st.sidebar.multiselect("Product", products, default=list(products))
platform_selected = st.sidebar.multiselect("Platform", platforms, default=list(platforms))

tracking_filt = tracking[
    tracking['source'].isin(brand_selected) &
    tracking['product'].isin(product_selected)
]
inf_filt = influencers[influencers['platform'].isin(platform_selected)]

# --- Performance Overview ---
st.header("Campaign Performance")

merged = tracking_filt.merge(inf_filt, left_on='influencer_id', right_on='ID')
campaign_perf = merged.groupby(['name','campaign','platform']).agg(
    orders=('orders','sum'),
    revenue=('revenue','sum')
).reset_index()

st.dataframe(campaign_perf)

# --- ROAS Section ---
st.header("ROI & ROAS Analysis")

payouts_merged = payouts.merge(influencers, left_on='influencer_id', right_on='ID')
perf_payout = tracking.merge(payouts_merged, left_on='influencer_id', right_on='influencer_id')
roas_df = perf_payout.groupby('name').agg({
    'revenue': 'sum',
    'total_payout': 'first'
}).reset_index()
roas_df['ROAS'] = roas_df.apply(lambda x: roas(x['revenue'], x['total_payout']), axis=1)
st.dataframe(roas_df[['name', 'revenue', 'total_payout', 'ROAS']])

# --- Incremental ROAS Simulation ---
st.subheader("Incremental ROAS (Hypothetical Baseline)")
baseline_rev = roas_df['revenue'].mean() * 0.7  # Simulate 30% lift
roas_df['Baseline_Revenue'] = baseline_rev
roas_df['Incremental_ROAS'] = roas_df.apply(
    lambda x: incremental_roas(x['revenue'], x['Baseline_Revenue'], x['total_payout']), axis=1
)
st.dataframe(roas_df[['name','revenue','Baseline_Revenue','Incremental_ROAS']])

# --- Insights ---
st.header("Key Insights")

best_infl = roas_df.sort_values('Incremental_ROAS', ascending=False).head(3)
worst_infl = roas_df.sort_values('Incremental_ROAS').head(3)

st.markdown("**Top Influencers by Incremental ROAS:**")
st.table(best_infl[['name','Incremental_ROAS']])

st.markdown("**Lowest Performing Influencers:**")
st.table(worst_infl[['name','Incremental_ROAS']])

# --- Payouts ---
st.header("Payout Tracking")
st.dataframe(payouts_merged[['name','basis','rate','orders','total_payout']])

# --- Data Export ---
import io
out_csv = campaign_perf.to_csv(index=False).encode('utf-8')
st.download_button("Export Campaign Performance CSV", data=out_csv, file_name="campaign_performance.csv", mime="text/csv")

# --- Visualization Example ---
import plotly.express as px
fig = px.bar(roas_df, x='name', y='ROAS', title='ROAS by Influencer')
st.plotly_chart(fig)