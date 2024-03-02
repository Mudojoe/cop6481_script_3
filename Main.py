from spatial_analysis import perform_spatial_join
from map_visualization import plot_transactions
from interactive_map import plot_interactive_map
from interactive_map_2 import plot_interactive_map_2
from interactive_map_3 import plot_interactive_map_3
from interactive_map_4 import plot_interactive_map_4

def main():
    # Define the paths to your datasets
    transactions_csv = './cc_transactions.csv'
    boroughs_geojson = './nyc_boroughs.geojson'

    # Call the perform_spatial_join function
    joined_data = perform_spatial_join(transactions_csv, boroughs_geojson)
    # Now visualize the joined data
    plot_transactions(joined_data)
    # Now you can proceed with further analysis on joined_data




    plot_interactive_map(joined_data)
    plot_interactive_map_2(joined_data)
    plot_interactive_map_3(joined_data)
    plot_interactive_map_4(joined_data)

    print("Done. Goodbye")

if __name__ == "__main__":
    main()
