import json
import pandas as pd
import matplotlib.pyplot as plt

# Read customer data from JSON file
with open('customer.json', 'r') as file:
    customer_data = json.load(file)

# Read customer purchase data from JSON file
with open('customerpurchasedata.json', 'r') as file:
    customer_purchase_data = json.load(file)

# Read ethnic wear data from JSON file
with open('ethnicwear.json', 'r') as file:
    ethnic_wear_data = json.load(file)

# Create pandas DataFrames
customer_df = pd.DataFrame(customer_data)
customer_purchase_df = pd.DataFrame(customer_purchase_data)
ethnic_wear_df = pd.DataFrame(ethnic_wear_data)


plt.hist(customer_df['age'])
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Ages')
plt.show()

# Analysis
# For example, calculate the average age of customers
average_age = customer_df['age'].mean()
# print("\nAverage Age of Customers:", average_age)
