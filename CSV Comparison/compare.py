import csv

def compare_csv_files(file1_path, file2_path):
    """
    Compare the CSV Files & Redirect the Comparison to the Output File.

    1.) Check File Path 1 for Data
    2.) If Data Not in File Path 2, Redirect Data to Output CSV.

    Arg:
        file1_path: File Path we need checking
        file2_path: File path we checking against
    """

    try:
        with open(file1_path, 'r', newline='') as file1, open(file2_path, 'r', newline='') as file2:
            
            # Read CSV files into lists of rows
            reader1 = list(csv.reader(file1))
            reader2 = list(csv.reader(file2))

            with open('output.csv', 'w', newline='') as output:
                writer = csv.writer(output)

                # Write rows that are in file1 but not in file2
                for row in reader1:
                    if row not in reader2:
                        writer.writerow(row)

            print("Comparison complete. Differences written to output.csv")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    compare_csv_files("csv1.csv", "csv2.csv")
