import csv

# Constants
COLUMN_NAME = "counts"
INPUT_FILE = "filename1.csv"
OUTPUT_FILE = "filename2.csv"
START_RANGES = [(77.5, 88.5), (98.5, 106.5), (121.5, 130.5)]
REPLACEMENT_CHARACTERS = ['A', 'G', 'T']

def read_csv_column(filename, column_name):
    """Reads a specific column from a CSV file and returns its values."""
    column_values = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                column_values.append(row[column_name])
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return column_values

def replace_range(input_list, start_range, end_range, replacement_char):
    """Replaces values in the input list falling within the specified range with the given replacement character."""
    output_list = []
    for value in input_list:
        try:
            float_value = float(value)
            if start_range <= float_value <= end_range:
                output_list.append(replacement_char)
            else:
                output_list.append(value)
        except ValueError:
            output_list.append(value)  # If value cannot be converted to float, keep it unchanged
    return output_list

def is_list_subset_of_another_list(list1, list2):
    """Checks if list1 is a subset of list2."""
    return set(list1).issubset(set(list2))

if __name__ == "__main__":
    # Read column from the input file
    column_counts = read_csv_column(INPUT_FILE, COLUMN_NAME)

    # Apply range replacements
    for start_range, end_range, replacement_char in zip(START_RANGES, REPLACEMENT_CHARACTERS):
        column_counts = replace_range(column_counts, start_range, end_range, replacement_char)

    # Read first column from the output file
    row_counts = read_csv_column(OUTPUT_FILE, column_name="")  # Assuming the first column is required

    # Check if row_counts is a subset of converted_column
    print("is_list_subset_of_another_list:", is_list_subset_of_another_list(row_counts, column_counts))
