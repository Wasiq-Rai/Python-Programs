from sklearn.ensemble import RandomForestClassifier

# Ask the user for height, weight, and shoe size
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))
shoe_size = int(input("Enter your shoe size: "))

# Height, weight, and shoe size data for a group of people
X = [[175, 70, 42], [160, 60, 38], [180, 80, 44], [155, 50, 36], [185, 90, 46], [170, 75, 41]]

# Corresponding gender data for each person in the group
y = ['Male', 'Female', 'Male', 'Female', 'Male', 'Male']

# Create a Random Forest classifier with 100 trees
clf = RandomForestClassifier(n_estimators=100)

# Fit the classifier to the data
clf.fit(X, y)

# Predict the gender of the user
new_person = [[height, weight, shoe_size]]
prediction = clf.predict(new_person)

# Print the predicted gender
print(f"Based on your input, the predicted gender is: {prediction[0]}")
