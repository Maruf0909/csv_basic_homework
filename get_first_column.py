import csv

def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    first_column=[]
    for column in list(reader)[:]:
        id=column[0]
        first_column.append(id)

    
    return first_column
    
# Read the csv file
f=open('data.csv')
reader=csv.reader(f)
print(get_first_column(f))
