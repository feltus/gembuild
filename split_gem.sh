###split_gem.sh
#!/bin/bash


# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_file> <output_file_70> <output_file_30>"
    exit 1
fi


# Assign input arguments to variables
input_file="$1"
output_file_70="$2"
output_file_30="$3"


# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi


# Count the total number of lines in the input file
total_lines=$(wc -l < "$input_file")


# Calculate the number of lines for the 70% file (excluding header)
lines_70=$((($total_lines - 1) * 70 / 100))


# Extract the header
head -n 1 "$input_file" > "$output_file_70"
head -n 1 "$input_file" > "$output_file_30"


# Shuffle the remaining lines and distribute them
tail -n +2 "$input_file" | shuf | awk -v lines_70="$lines_70" '
    NR <= lines_70 {print >> "'$output_file_70'"}
    NR > lines_70 {print >> "'$output_file_30'"}
'


echo "Processing complete."
echo "70% of data (including header) written to: $output_file_70"
echo "30% of data (including header) written to: $output_file_30"
