# Use to extract Australia data
start_line = 523198
end_line = 796183
input_file = 'mobility_data.csv'
output_file = 'mobility_data_aus.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for current_line_number, line in enumerate(infile, start=1):
        if start_line <= current_line_number <= end_line:
            outfile.write(line)
        elif current_line_number > end_line:
            break
