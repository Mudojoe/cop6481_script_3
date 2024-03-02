import geopandas as gpd
import matplotlib.pyplot as plt


def plot_transactions(joined_gdf):
    """
    Plot credit card transactions on a map.

    Parameters:
        joined_data (geopandas.GeoDataFrame): The spatially joined dataset containing transactions and boroughs.
    """
    # Plot the NYC boroughs as the base layer

    boroughs_gdf = gpd.read_file('./nyc_boroughs.geojson')
    joined_gdf.crs = boroughs_gdf.crs


    fig, ax = plt.subplots(figsize=(12, 12))
    boroughs_gdf.plot(ax=ax, color='lightgrey', linewidth=0.5, edgecolor='black')
    joined_gdf.plot(ax=ax, markersize=10, color='blue', alpha=0.6, label='Transactions')

    # Plot transactions, color-coded by borough name
    for boro_name in joined_gdf['boro_name'].unique():
        gdf_subset = joined_gdf[joined_gdf['boro_name'] == boro_name]
        gdf_subset.plot(ax=ax, label=boro_name)

  #  check_distribution(joined_gdf)
    ax.legend(title='Borough')
    ax.set_title('NYC Credit Card Transactions by Borough')
    plt.show()

"""
def check_distribution(joined_gdf):
     
    # Check the distribution of transactions across boroughs.
    #  Parameters:
    #    joined_gdf (geopandas.GeoDataFrame): The GeoDataFrame containing joined transaction and borough data.
     
    # Count the number of transactions in each borough
    borough_counts = joined_gdf['boro_name'].value_counts()
    total_transactions = joined_gdf.shape[0]

    # Calculate the percentage of transactions in each borough
    borough_percentage = (borough_counts / total_transactions) * 100

    # Display the calculated percentages
    print("Borough Distribution:\n")
    print(borough_percentage)
"""

# Assuming joined_gdf is your GeoDataFrame after the spatial join

