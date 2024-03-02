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
transactions_df = pd.DataFrame(
    columns=['Transaction ID', 'Date', 'Amount', 'Latitude', 'Longitude', 'User ID', 'Status'])

# Generate transactions for each borough
for borough, percentage in distributions.items():
    n_points = int(total_points * percentage)
    for i in range(n_points):
        transaction_id = np.random.randint(10000000, 99999999)
        date = pd.Timestamp('2023-08-01') + pd.to_timedelta(np.random.randint(1, 31), unit='D')
        amount = np.random.uniform(5, 500)
        lat = np.random.uniform(borough_boundaries[borough]['lat'][0], borough_boundaries[borough]['lat'][1])
        lon = np.random.uniform(borough_boundaries[borough]['lon'][0], borough_boundaries[borough]['lon'][1])
        user_id = np.random.randint(1, 901)
        status = 'Accepted' if np.random.rand() > 0.05 else 'Declined'

        # Append to the DataFrame
        transactions_df = transactions_df._append({
            'Transaction ID': transaction_id,
            'Date': date,
            'Amount': amount,
            'Latitude': lat,
            'Longitude': lon,
            'User ID': user_id,
            'Status': status
        }, ignore_index=True)

# Shuffle the DataFrame to mix transactions
transactions_df = transactions_df.sample(frac=1).reset_index(drop=True)

# Save the DataFrame to a CSV file
transactions_df.to_csv('cc_transactions.csv', index=False)

