# Use to extract Australian covid data

header_line = "location,date,total_cases,total_deaths,total_tests,new_cases,new_deaths,new_tests,population\n"

start_line = 20967
end_line = 22577
input_file = '../data/raw/covid_data.csv'
output_file = '../data/processed/covid_data_aus.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    outfile.write(header_line)
    for current_line_number, line in enumerate(infile, start=1):
        if start_line <= current_line_number <= end_line:
            outfile.write(line)
        elif current_line_number > end_line:
            break
