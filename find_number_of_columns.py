import csv


def find_mumber_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    return len(list(csv.reader(data))[0])

# Read the csv file
f = open("data.csv")
print(find_mumber_of_columns(f))