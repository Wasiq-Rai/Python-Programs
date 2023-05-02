import csv

# Define a function to read the data from a CSV file
def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        data = []
        for row in reader:
            data.append({
                'name': row[0],
                'age': int(row[1]),
                'gender': row[2],
                'income': int(row[3])
            })
        return data