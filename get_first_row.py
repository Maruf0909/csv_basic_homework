import csv

def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   first_row=[]
   for i in list(reader)[1]:
        first_row.append(i)   
        
   return first_row

# Read the csv file
f=open('data.csv')
reader=csv.reader(f)
print(get_first_row(f))