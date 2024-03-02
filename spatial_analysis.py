import geopandas as gpd
import pandas as pd
from shapely import Point


def perform_spatial_join(transactions_csv, boroughs_geojson):
    """
    Perform a spatial join between credit card transactions and NYC boroughs.
    It adds a 'boro_name' column to the transactions based on their coordinates.

    Parameters:
        transactions_csv (str): Path to the CSV file containing credit card transactions.
        boroughs_geojson (str): Path to the GeoJSON file with NYC boroughs boundaries.

    Returns:
        geopandas.GeoDataFrame: The result of the spatial join, with transactions linked to boroughs.
    """
    # Load the transactions data
    transactions_df = pd.read_csv(transactions_csv)
    transactions_gdf = gpd.GeoDataFrame(
        transactions_df,
        geometry=gpd.points_from_xy(transactions_df.Longitude, transactions_df.Latitude),
        crs="EPSG:4326"
    )

    # Load the boroughs data
    boroughs_gdf = gpd.read_file(boroughs_geojson)
    boroughs_gdf = boroughs_gdf.to_crs("EPSG:4326")  # Ensure CRS matches transactions data

    # Perform the spatial join
    joined_gdf = gpd.sjoin(transactions_gdf, boroughs_gdf, how="left", op="within")

    # Rename the column with borough names if necessary
    if 'boro_name' not in joined_gdf.columns and 'BoroName' in boroughs_gdf.columns:
        joined_gdf = joined_gdf.rename(columns={'BoroName': 'boro_name'})

    # Drop any transactions that could not be joined with a borough
    joined_gdf = joined_gdf.dropna(subset=['boro_name'])


    print(f"joined_gdf.columns = {joined_gdf.columns}")

    # Check the first few rows after the join
    print(joined_gdf.head())

    return joined_gdf
