import os

header_line = "country_region_code,country_region,sub_region_1,sub_region_2,metro_area,iso_3166_2_code,census_fips_code,place_id,date,retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline\n"

# Input and output file paths
input_file = '../data/raw/mobility_data.csv'
output_file = '../data/processed/mobility_data_aus.csv'

# Ensure the processed directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Extract lines where the country_region is "Australia"
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(header_line)
    for line in infile:
        # Skip the header line in the input file
        if line.startswith(header_line.strip()):
            continue
        # Split the line by commas
        columns = line.split(',')
        # Check if the country_region column is "Australia"
        if columns[1] == "Australia":
            outfile.write(line)

print("Extraction completed successfully.")
