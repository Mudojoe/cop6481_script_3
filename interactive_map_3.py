import folium
from folium.plugins import HeatMap

def plot_interactive_map_3(joined_gdf):
    if 'Transaction Count' not in joined_gdf.columns:
        joined_gdf['Transaction Count'] = joined_gdf.groupby('Merchant ID')['Merchant ID'].transform('count')

    # Preparing the data for heatmap
    data_for_heatmap = joined_gdf[['Latitude', 'Longitude', 'Transaction Count']].values.tolist()

    # Map centered around NYC
    map_center = [joined_gdf['Latitude'].mean(), joined_gdf['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Adding a heatmap layer for all transactions
    HeatMap(data_for_heatmap).add_to(m)

    rejected_transactions = joined_gdf[joined_gdf['Status'] == 'Declined']
    for idx, row in rejected_transactions.iterrows():
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=f'Rejected Transaction<br>Merchant ID: {row["Merchant ID"]}',
            icon=folium.Icon(color='red')
        ).add_to(m)


    folium.LayerControl().add_to(m)

    # Save the interactive map to an HTML file
    m.save('interactive_map_3.html')
    print("Interactive map is saved as 'interactive_map_3.html'.")
