import os

header_line = "location,date,total_cases,total_deaths,total_tests,new_cases,new_deaths,new_tests,population\n"

# Input and output file paths
input_file = '../data/raw/covid_data.csv'
output_file = '../data/processed/covid_data_aus.csv'

# Ensure the processed directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Extract lines where the location is "Australia"
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write(header_line)
    for line in infile:
        if line.startswith("Australia,"):
            outfile.write(line)

print("Extraction completed successfully.")
