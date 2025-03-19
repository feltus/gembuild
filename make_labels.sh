###make_labels.sh
#!/bin/bash


# Check if the input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi


input_file=$1
output_file="$input_file.label"


# Process the file, starting from the second line
awk 'NR > 1 {
    # Extract the first column
    first_column = $1
    
    # Extract the part before the first dash
    split(first_column, parts, "-")
    before_dash = parts[1]
    
    # Print the first column and the part before the dash, separated by a tab
    print first_column "\t" before_dash
}' "$input_file" > "$output_file"


echo "Processing complete. Output saved to $output_file"
