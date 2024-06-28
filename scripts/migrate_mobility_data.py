# Use to extract Australia mobility data


header_line = "country_region_code,country_region,sub_region_1,sub_region_2,metro_area,iso_3166_2_code,census_fips_code,place_id,date,retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline\n"

start_line = 523198
end_line = 796184
input_file = '../data/raw/mobility_data.csv'
output_file = '../data/processed/mobility_data_aus.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write(header_line)
    for current_line_number, line in enumerate(infile, start=1):
        if start_line <= current_line_number <= end_line:
            outfile.write(line)
        elif current_line_number > end_line:
            break
