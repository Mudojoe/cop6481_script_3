import geopandas as gpd
import matplotlib.pyplot as plt


def plot_transactions(joined_gdf):
    """
    Plot total number of transactions for the month by merchant on a map,
    color-coded by borough.

    Parameters:
        joined_data (geopandas.GeoDataFrame): The spatially joined dataset containing transactions and boroughs.
    """
    # Aggregate transactions by merchant and calculate the total number of transactions for each merchant

    merchant_counts = joined_gdf.groupby(['Merchant ID', 'boro_name']).size().reset_index(name='Transaction Count')
    # Join this aggregated data back on the original dataframe to get the coordinates
    aggregated_gdf = joined_gdf.drop_duplicates(subset=['Merchant ID']).merge(merchant_counts, on='Merchant ID')
    aggregated_gdf['boro_name'] = aggregated_gdf['boro_name_x']



    # Load the NYC boroughs as the base layer
    boroughs_gdf = gpd.read_file('./nyc_boroughs.geojson')
    aggregated_gdf.crs = boroughs_gdf.crs

    fig, ax = plt.subplots(figsize=(12, 12))
    boroughs_gdf.plot(ax=ax, color='lightgrey', linewidth=0.5, edgecolor='black')

    # Define a color for each borough
    borough_colors = {
        'Manhattan': 'red',
        'Brooklyn': 'green',
        'Queens': 'blue',
        'Bronx': 'purple',
        'Staten Island': 'orange'
    }

    # Plot aggregated transactions, color-coded by borough
    for borough in aggregated_gdf['boro_name'].unique():
        subset = aggregated_gdf[aggregated_gdf['boro_name'] == borough]
        ax.scatter(subset['Longitude'], subset['Latitude'], s=subset['Transaction Count'] * 10,
                   color=borough_colors[borough], label=borough, alpha=0.6)

    ax.legend(title='Borough')
    ax.set_title('NYC Credit Card Transactions by Merchant and Borough')
    plt.show()




