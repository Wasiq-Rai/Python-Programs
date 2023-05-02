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
# Define a function to write the results to a CSV file
def write_results(filename, results):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Statistic', 'Value'])
        for key, value in results.items():
            writer.writerow([key, value])

# Main program
if __name__ == '__main__':
    data = read_data('input.csv')
    results = analyze_data(data)
    write_results('output.csv', results)
    print('Results written to output.csv')