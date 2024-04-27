import json
import pandas as pd


with open('customer.json', 'r') as file:
    customer_data = json.load(file)
    print(customer_data)

# Read customer purchase data from JSON file
with open('customerpurchasedata.json', 'r') as file:
    customer_purchase_data = json.load(file)
    print(customer_purchase_data)

# Read ethnic wear data from JSON file
with open('ethnicwear.json', 'r') as file:
    ethnic_wear_data = json.load(file)


# Convert JSON data to Python dictionaries or lists
customer_data = json.loads(customer_data)
customer_purchase_data = json.loads(customer_purchase_data)
ethnic_wear_data = json.loads(ethnic_wear_data)

# Create pandas DataFrames
customer_df = pd.DataFrame(customer_data)
customer_purchase_df = pd.DataFrame(customer_purchase_data)
ethnic_wear_df = pd.DataFrame(ethnic_wear_data)

# Data Exploration
# For example, display the first few rows of each DataFrame
print("Customer Data:")
print(customer_df.head())

print("\nCustomer Purchase Data:")
print(customer_purchase_df.head())

print("\nEthnic Wear Data:")
print(ethnic_wear_df.head())

# Data Visualization
# For example, create a histogram of customer ages
import matplotlib.pyplot as plt
plt.hist(customer_df['age'])
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Ages')
plt.show()

# Analysis
# For example, calculate the average age of customers
average_age = customer_df['age'].mean()
print("\nAverage Age of Customers:", average_age)