import pandas as pd
import numpy as np

def load_data():
    influencers = pd.read_csv('sample_data/influencers.csv')
    posts = pd.read_csv('sample_data/posts.csv')
    tracking = pd.read_csv('sample_data/tracking_data.csv')
    payouts = pd.read_csv('sample_data/payouts.csv')
    return influencers, posts, tracking, payouts

def roas(revenue, spend):
    if spend == 0:
        return np.nan
    return revenue / spend

def incremental_roas(campaign_rev, baseline_rev, spend):
    inc_rev = campaign_rev - baseline_rev
    return inc_rev / spend if spend > 0 else np.nan