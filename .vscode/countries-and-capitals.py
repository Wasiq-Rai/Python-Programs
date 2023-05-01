import requests

# Make a request to the REST Countries API
response = requests.get("https://restcountries.com/v3.1/all")

# Convert the response to a Python dictionary
countries = response.json()

# Loop through the list of countries and print the name, capital, and population
for country in countries:
    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    print(f"{name}: {capital}, Population: {population}")
