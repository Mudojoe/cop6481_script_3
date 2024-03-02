import numpy as np
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(0)

# Define the number of data points
total_points = 2000

# Distribution percentages for each borough
distributions = {
    'Manhattan': 0.35,
    'Brooklyn': 0.20,
    'Queens': 0.20,
    'Bronx': 0.15,
    'Staten Island': 0.10,
}

# Approximate boundaries for each borough (latitude and longitude)
borough_boundaries = {
    'Manhattan': {'lat': (40.7011, 40.8800), 'lon': (-74.0203, -73.9067)},
    'Brooklyn': {'lat': (40.5700, 40.7395), 'lon': (-74.0431, -73.8334)},
    'Queens': {'lat': (40.4961, 40.7922), 'lon': (-73.9625, -73.7004)},
    'Bronx': {'lat': (40.7855, 40.9153), 'lon': (-73.9339, -73.7654)},
    'Staten Island': {'lat': (40.4961, 40.6518), 'lon': (-74.2591, -74.0345)},
}

# Create an empty DataFrame to store transaction data
transactions_df = pd.DataFrame(columns=['Transaction ID', 'Date', 'Amount', 'Latitude', 'Longitude', 'User ID', 'Status', 'Merchant ID'])

# Generate User IDs and Merchant IDs
user_ids = np.random.randint(1_000_000, 10_000_000, size=int(total_points * 0.9))
user_ids = np.append(user_ids, np.random.choice(user_ids, size=int(total_points * 0.1))) # 10% repeats
merchant_ids_base = np.random.randint(10_000_000, 100_000_000, size=int(total_points * 0.25))
merchant_ids = np.append(merchant_ids_base, np.random.choice(merchant_ids_base, size=total_points - len(merchant_ids_base))) # 75% repeats

# Ensure arrays are shuffled to avoid any unintentional ordering
np.random.shuffle(user_ids)
np.random.shuffle(merchant_ids)

# Generate transactions
for borough, bounds in borough_boundaries.items():
    n_points = int(distributions[borough] * total_points)
    for i in range(n_points):
        transaction_id = np.random.randint(10000000, 99999999)
        date = pd.Timestamp('2023-08-01') + pd.to_timedelta(np.random.randint(1, 31), unit='D')
        amount = np.random.uniform(5, 500)
        lat = np.random.uniform(bounds['lat'][0], bounds['lat'][1])
        lon = np.random.uniform(bounds['lon'][0], bounds['lon'][1])
        user_id = user_ids[i]
        status = 'Accepted' if np.random.rand() > 0.05 else 'Declined'
        merchant_id = merchant_ids[i]

        transactions_df = transactions_df._append({
            'Transaction ID': transaction_id,
            'Date': date,
            'Amount': amount,
            'Latitude': lat,
            'Longitude': lon,
            'User ID': user_id,
            'Status': status,
            'Merchant ID': merchant_id
        }, ignore_index=True)

# Shuffle the DataFrame to mix transactions from different boroughs
transactions_df = transactions_df.sample(frac=1).reset_index(drop=True)
# Save the DataFrame to a CSV file
transactions_df.to_csv('cc_transactions_2.csv', index=False)
