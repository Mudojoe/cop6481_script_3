from spatial_analysis import perform_spatial_join
from map_visualization import plot_transactions

def main():
    # Define the paths to your datasets
    transactions_csv = './cc_transactions_2.csv'
    boroughs_geojson = './nyc_boroughs.geojson'

    # Call the perform_spatial_join function
    joined_data = perform_spatial_join(transactions_csv, boroughs_geojson)
    print(joined_data.head())
    print(joined_data.columns)
    # Now visualize the joined data
    plot_transactions(joined_data)
    # Now you can proceed with further analysis on joined_data



if __name__ == "__main__":
    main()
