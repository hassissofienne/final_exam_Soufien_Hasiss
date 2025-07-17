#task 1 

# Loop through numbers from 4 to 40 (inclusive)
for i in range(4, 41):
    # Print the square of the current number
    print(f"{i} squared is {i**2}")

# task 2 

# Define the function that takes a list of grades
def check_grades(grades):
    # Loop through each grade in the list
    for grade in grades:
        # Check if grade is greater or equal to 75
        if grade >= 75:
            print("Pass")
        else:
            print("No")

# Test the function with a sample list
check_grades([60, 80, 90, 70, 75])

# task 3 

# Define the function that takes a string
def count_vowels(text):
    vowels = "aeiou"  # All lowercase vowels
    counts = {}  # Dictionary to store count of each vowel
    total = 0  # Total vowels

    # Convert text to lowercase for case-insensitive matching
    text = text.lower()

    # Loop through each character in the text
    for char in text:
        if char in vowels:
            # Count the total vowels
            total += 1
            # Update the count of each vowel
            counts[char] = counts.get(char, 0) + 1

    # Print the results
    print(f"Total vowels: {total}")
    for vowel, count in counts.items():
        print(f"{vowel}: {count}")

# Test with example text
count_vowels("Data Scientist (n.): Person who is better at statistics than any software engineer")

#task 4 

# Initialize an empty list to store valid numbers
numbers = []

# Start an infinite loop
while True:
    # Ask user for input
    entry = input("Enter a number (or 'done' to finish): ")

    # Check if user wants to finish
    if entry.lower() == "done":
        break

    # Try converting input to float
    try:
        number = float(entry)
        numbers.append(number)
    except ValueError:
        # If input is not a number, show error
        print("Invalid input. Try again.")

# Calculate and display results
count = len(numbers)
if count > 0:
    avg = sum(numbers) / count
    print(f"Total numbers entered: {count}")
    print(f"Average: {avg:.2f}")
else:
    print("No valid numbers were entered.")
    
# task 5

# Sample list of purchases
purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]

# Create an empty dictionary to store totals
totals = {}

# Iterate through each purchase
for name, amount in purchases:
    # Add amount to existing total or start at 0
    totals[name] = totals.get(name, 0) + amount

# Print total spent per customer
for customer, total in totals.items():
    print(f"{customer} spent ${total}")

# task 6 
 # Import necessary libraries
import wbdata
import pandas as pd
import datetime

# Set country and indicator
country = "RO"  
indicator = {"SP.POP.TOTL": "Population"}

# Set date range
data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2020, 12, 31))

# Fetch the data from World Bank
df = wbdata.get_dataframe(indicator, country=country, data_date=data_date)

# Reset index to make year a column
df = df.reset_index()

# Sort by year
df = df.sort_values("date")

# Print the results
print(df)






