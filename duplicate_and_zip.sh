#!/bin/bash
#SBATCH --mem=100G           
#SBATCH --time=3:0:0
#SBATCH -J midterm # job name
#SBATCH --output=%x-%j.out


# Define the original file and the names for the duplicate files
original_file="stackoverflow_javascript_pyhon_qa.csv"
duplicate_file="duplicated.csv"
sorted_duplicate_file="duplicated_sorted.csv"

# Create a new file that is a duplicate of the original file 10 times
echo "Duplicating file..."
time {
  for i in {1..10}; do
    cat "$original_file" >> "$duplicate_file"
  done
}

# Sort the duplicated file
echo "Sorting duplicated file..."
time sort "$duplicate_file" > "$sorted_duplicate_file"

# Compress the original file
echo "Compressing original file..."
time zip "${original_file}.zip" "$original_file"

# Compress the duplicated file
echo "Compressing duplicated file..."
time zip "${duplicate_file}.zip" "$duplicate_file"

# Compress the sorted duplicated file
echo "Compressing sorted duplicated file..."
time zip "${sorted_duplicate_file}.zip" "$sorted_duplicate_file"
echo "Compression completed."
