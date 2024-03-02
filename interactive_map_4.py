import folium
from folium.plugins import HeatMap
import pandas as pd

def plot_interactive_map_4(joined_gdf):
    if 'Transaction Count' not in joined_gdf.columns:
        joined_gdf['Transaction Count'] = joined_gdf.groupby('Merchant ID')['Merchant ID'].transform('count')

    # Create a map centered around the center of NYC
    map_center = [joined_gdf['Latitude'].mean(), joined_gdf['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Adding a heatmap layer for all transactions
    data_for_heatmap = joined_gdf[['Latitude', 'Longitude', 'Transaction Count']].values.tolist()
    HeatMap(data_for_heatmap).add_to(m)

    # Aggregate data by borough
    borough_aggregation = joined_gdf.groupby('boro_name').agg({
        'Merchant ID': pd.Series.nunique,
        'Transaction Count': 'sum',
        'Latitude': 'mean',  # Assuming the mean latitude/longitude can represent the center of the borough
        'Longitude': 'mean'
    }).reset_index()

    # Add one marker per borough
    for idx, row in borough_aggregation.iterrows():
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=f'Borough: {row["boro_name"]}<br>Unique Merchants: {row["Merchant ID"]}<br>Total Transactions: {row["Transaction Count"]}',
            icon=folium.Icon(color='green')
        ).add_to(m)

    # Save the interactive map to an HTML file
    m.save('interactive_map_4.html')
    print("Interactive map is saved as 'interactive_map_4.html'.")



