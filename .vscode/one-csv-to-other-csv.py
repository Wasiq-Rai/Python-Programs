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
# Define a function to calculate some statistics on the data
def analyze_data(data):
    num_female = 0
    num_male = 0
    total_income = 0
    for row in data:
        if row['gender'] == 'Female':
            num_female += 1
        elif row['gender'] == 'Male':
            num_male += 1
        total_income += row['income']
    avg_income = total_income / len(data)
    return {
        'num_female': num_female,
        'num_male': num_male,
        'avg_income': avg_income
    }