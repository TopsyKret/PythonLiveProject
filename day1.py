import matplotlib.pyplot as plt

""" Day 1 """

ditc1 = {}
print("A simple data analysis program")
f = open(r"C:\Users\Jag\Documents\guru99\liveproject1\Emissions.csv", "r")
# if f.mode == 'r':
#     contents =f.read()
# print(contents)

for data in f.read().split('\n'):
    ditc1.update({data.split(",")[0]: data.split(',')[1:]})

# print(ditc1.items())
# At this point, everything is segregated as a string due to the split function

# for x, y in ditc1.items():
#     print(x, end=" - ")
#     print(y)

print("All data from Emissions.csv has been read into a dictionary.")

""" Day 2 """

user_input = input("Select a year to find statistics (1997 - 2010): ")
# print(user_input)
index_year = None
emissions_in_that_year = []
i = 0
sum = 0

# Extracting index of the year inputted by the user from the first entry into the dictionary - Values
# year_value = list(ditc1.values())[0]
# print(year_value)

year_value = next(iter(ditc1.items()))[1]
# print(year_value)
for items in year_value:
    if user_input == items:
        index_year = (year_value.index(items))
        # print(index_year)

# Finding the entries of the column for the year input by the user. Iterate through the values of a list
for value in ditc1.values():
    # For the first loop skip the code because in our case it contains Column Names and Years
    if i != 0:
        sum += float(value[index_year])
        emissions_in_that_year.append(list(ditc1.values())[i][index_year]) #It will generate a list of strings
    i += 1
# Need the length to calculate the average 
n = len(emissions_in_that_year)
# print(n)
average = float(sum/n) 
# print(average)
# print(emissions_in_that_year)
# Have generated a list that has all the emissions entry of the selected index from the year inputted by the year but the entries are strings
# Further analysis - worldwide statistics (min, max, average) for a user-entered year

min_country_index = int(emissions_in_that_year.index(str(min(float(str_value) for str_value in emissions_in_that_year))))
max_country_index = int(emissions_in_that_year.index(str(max(float(str_value) for str_value in emissions_in_that_year))))

max_country = list(ditc1.keys())[max_country_index+1]
min_country = list(ditc1.keys())[min_country_index+1]

print(f"In {user_input}, countries with minimum and maximum CO2 levels were: [{min_country}] and [{max_country}] respectively.")
print(f"Average CO2 emissions in {user_input} were {average}")

""" Day 3 """
"""
Name: Python Data Analysis
Purpose: Plotting emission graph for country

Algorithm:

Step 1: Take the input from user to visualize data
Step 2: Getting the index of Country and passing it to plot function, Setting the Title and Label of Plot
Algo:
Title : Year vs Emissions in Capita
x axis = Year
y axis = Emission in India, Input is the country India then 


"""
# country_name = input("Select the country to visualize: ")

# # Index of the country from the user entered country
# country_index = list(ditc1.keys()).index(country_name)
# # Plotting x and y axis using the plot function
# plt.plot(list(map(float, list(ditc1.values())[0])), list(map(float, list(ditc1.values())[country_index])))
# plt.title("Year vs Emissions in Capita")
# plt.xlabel("Year")
# plt.ylabel("Emission in " + country_name.title())
# plt.show()
# print()

# """
# Day 4
# Name: Python Data Analysis
# Purpose: Plotting comparison graph for two countries

# Algorithm:

# Step 1: Take two comma-separated countries input from user
# Step 2: Extracting the Index number for both countries
# Step 3: Passing the value to plot function and setting up label for country
# Algo:
# """

# country1, country2 = input("Write two comma-separated countries for which you want to visualize data: ").split(", ")
# # print(country2)
# # print(country1)
# # # print(country1, country2)
# index_num_1 = list(ditc1.keys()).index(country1)
# index_num_2 = list(ditc1.keys()).index(country2)
# # print(index_num_2)
# # print(index_num_1)

# # # Combine two plots in one:
# plt.plot(list(map(float, list(ditc1.values())[0])), list(map(float, list(ditc1.values())[index_num_1])), label=country1)
# plt.plot(list(map(float, list(ditc1.values())[0])), list(map(float, list(ditc1.values())[index_num_2])), label=country2)
# plt.title("Year vs Emissions in Capita")
# plt.xlabel("Year")
# plt.ylabel("Emission in")
# plt.legend
# plt.show()
# print()

# """
# Day 5

# """

three_countries = input("Write upto three comma-separated countries for which you want to extract data: ")
country_list = three_countries.split(" ")
def extract_data(country):
    if len(country_list) > 3:
        print("ERR: Sorry, at most 3 countries can be entered.")

for country in three_countries.split(" "):
    # print(country)
    for key in (ditc1.keys()):
        # print(key)
        if country == key:
            print("hey")
    #         three_countries_data = ditc1["key"]
    #         print(three_countries_data)

# Function def approach: for the countries in three countries, capture the values corresponding to the key/country and save in a csv file

def extract_data(country):




