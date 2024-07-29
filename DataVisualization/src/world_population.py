import json

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
