import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def simulate_influencers(num=15):
    np.random.seed(42)
    names = [f"Influencer_{i}" for i in range(num)]
    categories = np.random.choice(['Fitness', 'Wellness', 'Nutrition'], num)
    genders = np.random.choice(['Male', 'Female', 'Other'], num)
    follower_counts = np.random.randint(10000, 500000, num)
    platforms = np.random.choice(['Instagram', 'YouTube', 'Twitter'], num)

    df = pd.DataFrame({
        'ID': [i+1 for i in range(num)],
        'name': names,
        'category': categories,
        'gender': genders,
        'follower_count': follower_counts,
        'platform': platforms
    })
    return df

def simulate_posts(influencers, num_posts=40):
    rows = []
    for i in range(num_posts):
        iid = np.random.choice(influencers['ID'])
        platform = influencers.loc[influencers['ID'] == iid, 'platform'].values[0]
        date = datetime.today() - timedelta(days=np.random.randint(0, 60))
        url = f"https://socialmedia.com/post/{iid}_{i}"
        caption = f"Exciting campaign post {i+1}"
        reach = np.random.randint(8000, 180000)
        likes = np.random.randint(100, 8000)
        comments = np.random.randint(5, 400)
        rows.append({
            'influencer_id': iid,
            'platform': platform,
            'date': date.strftime('%Y-%m-%d'),
            'URL': url,
            'caption': caption,
            'reach': reach,
            'likes': likes,
            'comments': comments
        })
    return pd.DataFrame(rows)

def simulate_tracking(influencers, num_rows=100):
    brands = ['MuscleBlaze', 'Gritzo', 'HKVitals']
    products = ['Protein', 'Supplement', 'Bar', 'Shaker']
    rows = []
    for _ in range(num_rows):
        iid = np.random.choice(influencers['ID'])
        campaign = f"Campaign_{np.random.randint(1,4)}"
        user_id = np.random.randint(1000, 9000)
        product = np.random.choice(products)
        brand = np.random.choice(brands)
        date = datetime.today() - timedelta(days=np.random.randint(0, 60))
        orders = np.random.randint(1, 7)
        revenue = round(orders * np.random.uniform(400, 2200), 2)
        rows.append({
            'source': brand,
            'campaign': campaign,
            'influencer_id': iid,
            'user_id': user_id,
            'product': product,
            'date': date.strftime('%Y-%m-%d'),
            'orders': orders,
            'revenue': revenue
        })
    return pd.DataFrame(rows)

def simulate_payouts(influencers):
    basis_options = ['post', 'order']
    rows = []
    for iid in influencers['ID']:
        basis = np.random.choice(basis_options)
        rate = np.random.randint(1000, 6000) if basis=='post' else np.random.randint(150, 600)
        orders = np.random.randint(15, 90)
        total_payout = (rate * orders) if basis=='order' else rate
        rows.append({
            'influencer_id': iid,
            'basis': basis,
            'rate': rate,
            'orders': orders,
            'total_payout': total_payout
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    inf = simulate_influencers()
    inf.to_csv('sample_data/influencers.csv', index=False)
    simulate_posts(inf).to_csv('sample_data/posts.csv', index=False)
    simulate_tracking(inf).to_csv('sample_data/tracking_data.csv', index=False)
    simulate_payouts(inf).to_csv('sample_data/payouts.csv', index=False)