import folium
from folium.plugins import HeatMap

def plot_interactive_map_2(joined_gdf):
    # Ensure 'Transaction Count' column exists
    if 'Transaction Count' not in joined_gdf.columns:
        joined_gdf['Transaction Count'] = joined_gdf.groupby('Merchant ID')['Merchant ID'].transform('count')

    # General map settings
    map_center = [joined_gdf['Latitude'].mean(), joined_gdf['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=11)

    # Heatmap for all transactions
    data_for_heatmap = joined_gdf[['Latitude', 'Longitude', 'Transaction Count']].values.tolist()
    HeatMap(data_for_heatmap, name="All Transactions").add_to(m)

    # Heatmap for rejected transactions
    rejected_transactions = joined_gdf[joined_gdf['Status'] == 'Declined'][['Latitude', 'Longitude']].values.tolist()
    if rejected_transactions:
        HeatMap(rejected_transactions, name="Rejected Transactions", radius=15, max_zoom=1, blur=15, gradient={0.4: 'red', 0.65: 'orange', 1: 'yellow'}).add_to(m)


    popular_districts = joined_gdf[joined_gdf['Transaction Count'] > joined_gdf['Transaction Count'].quantile(0.75)][['Latitude', 'Longitude', 'Transaction Count']].values.tolist()
    if popular_districts:
        HeatMap(popular_districts, name="Popular Shopping Districts", radius=20, max_zoom=1, blur=20, gradient={0.4: 'blue', 0.65: 'lime', 1: 'green'}).add_to(m)

    # Add layer control to toggle between maps
    folium.LayerControl().add_to(m)

    # Save the interactive map to an HTML file
    m.save('interactive_map_2.html')
    print("Interactive map is saved as 'interactive_map_2.html'.")
