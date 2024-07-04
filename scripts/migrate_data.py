import os

def get_country_from_user():
    country = input("Enter the country name for extraction: ").strip()
    return country

def is_valid_country(input_file, country, column_name):
    with open(input_file, 'r', encoding='utf-8') as infile:
        header = infile.readline().strip().split(',')
        column_index = header.index(column_name)
        for line in infile:
            columns = line.strip().split(',')
            if columns[column_index] == country:
                return True
    return False

def extract_covid_data(country):
    header_line = "location,date,total_cases,total_deaths,total_tests,new_cases,new_deaths,new_tests,population\n"
    input_file = '../data/raw/covid_data.csv'
    output_file = f'../data/processed/covid_data_{country.lower().replace(" ", "_")}.csv'

    # Ensure the processed directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Extract lines where the location matches the country
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(header_line)
        for line in infile:
            if line.startswith(f"{country},"):
                outfile.write(line)

    print(f"COVID data extraction for {country} completed successfully.")

def extract_mobility_data(country):
    header_line = "country_region_code,country_region,sub_region_1,sub_region_2,metro_area,iso_3166_2_code,census_fips_code,place_id,date,retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline\n"
    input_file = '../data/raw/mobility_data.csv'
    output_file = f'../data/processed/mobility_data_{country.lower().replace(" ", "_")}.csv'

    # Ensure the processed directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Extract lines where the country_region matches the country
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(header_line)
        for line in infile:
            if line.startswith(header_line.strip()):
                continue
            columns = line.split(',')
            if columns[1].strip() == country:
                outfile.write(line)

    print(f"Mobility data extraction for {country} completed successfully.")

def main():
    covid_input_file = '../data/raw/covid_data.csv'
    mobility_input_file = '../data/raw/mobility_data.csv'

    while True:
        country = get_country_from_user()
        if is_valid_country(covid_input_file, country, 'location') and is_valid_country(mobility_input_file, country, 'country_region'):
            break
        else:
            print(f"'{country}' is not a valid country name in the dataset. Please enter a valid country name.")

    extract_covid_data(country)
    extract_mobility_data(country)

if __name__ == "__main__":
    main()
