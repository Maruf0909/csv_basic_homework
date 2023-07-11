#Define function,Get coloumn names from a csv file
import csv

def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    
    column=[]
    for row in list(reader)[0]:
        column.append(row)
    return column
    
# Read the csv file
f=open('data.csv')
reader=csv.reader(f)
print(get_column_names(f))

