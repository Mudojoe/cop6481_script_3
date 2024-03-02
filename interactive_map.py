import folium
from folium.plugins import HeatMap


def plot_interactive_map(joined_gdf):
    # This should be done where you aggregate the data, which might be in `plot_transactions`.
    if 'Transaction Count' not in joined_gdf.columns:
        # Code to create the 'Transaction Count' column, if missing
        # Example:
        joined_gdf['Transaction Count'] = joined_gdf.groupby('Merchant ID')['Merchant ID'].transform('count')

    # Now that we have the 'Transaction Count', proceed with creating the heatmap data

    data_for_heatmap = joined_gdf[['Latitude', 'Longitude', 'Transaction Count']].values.tolist()

    # Create a map centered around the center of NYC
    map_center = [joined_gdf['Latitude'].mean(), joined_gdf['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Add a heat map layer to the map
    HeatMap(data_for_heatmap).add_to(m)
    # Optionally, add markers for each merchant with popup labels showing more information
    for idx, row in joined_gdf.iterrows():
        folium.CircleMarker(
            location=(row['Latitude'], row['Longitude']),
            radius=row['Transaction Count'] / 10,  # or any other scaling factor for the size
            color='blue',
            fill=True,
            fill_color='blue',
            popup=f'Merchant ID: {row["Merchant ID"]}\nTransactions: {row["Transaction Count"]}',
        ).add_to(m)


    # Save to an HTML file
    m.save('interactive_map.html')

    # Open the interactive map in the browser
    print("Interactive map is saved as 'interactive_map.html'.")
