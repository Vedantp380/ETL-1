import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\pandeyv1581\OneDrive - ARCADIS\Desktop\Python-ETL\datafile (1).csv"
data = pd.read_csv(file_path)

# Calculate the threshold for 80% non-null values
threshold = len(data) * 0.9

# Keep columns where the count of non-null values is at least the threshold
filtered_df = data[[col for col in data.columns if data[col].notnull().sum() >= threshold]]

filtered_df['date_collection'] = pd.to_datetime(filtered_df['date_collection'])

def plot_column(df, column_name):
    df.plot(x='date_collection', y=column_name, kind='line', marker='o', linestyle='-')
    plt.title(f'{column_name} Variation Over Time')
    plt.xlabel('Date')
    plt.ylabel(column_name)
    plt.grid(True)
    plt.show()

# Example usage
columns_to_plot = ['PH.1', 'CALCIUM(mg/L)', 'CHLORIDE', 'CARBONATE(mg/L)', 'ELECTRICAL CONDUCTIVITY(?S/CM) at 25?','BICARBONATE(mg/L)',	
                   'MAGNESIUM(mg/L)',	'SODIUM',	'SULPHATE(mg/L)',	'TEMPERATURE']
for column in columns_to_plot:
    plot_column(filtered_df, column)


# Grouping the data by block_name, basin_name, and sub_basin_name and calculating the mean values for each chemical
grouped_df = filtered_df.groupby(['block_name', 'basin_name', 'sub_basin_name']).agg({
    'CALCIUM(mg/L)': 'mean',
    'CHLORIDE': 'mean',
    'CARBONATE(mg/L)': 'mean',
    'ELECTRICAL CONDUCTIVITY(?S/CM) at 25?': 'mean',
    'BICARBONATE(mg/L)': 'mean',
    'MAGNESIUM(mg/L)': 'mean',
    'SODIUM': 'mean',
    'PH.1': 'mean',
    'SULPHATE(mg/L)': 'mean',
    'TEMPERATURE': 'mean'
}).reset_index()

# Plotting the data
fig, ax = plt.subplots(figsize=(16, 8))
grouped_df.plot(ax=ax, kind='bar', x='sub_basin_name', y=[
    'CALCIUM(mg/L)', 'CHLORIDE', 'CARBONATE(mg/L)', 'ELECTRICAL CONDUCTIVITY(?S/CM) at 25?',
    'BICARBONATE(mg/L)', 'MAGNESIUM(mg/L)', 'SODIUM', 'PH.1', 'SULPHATE(mg/L)', 'TEMPERATURE'
], width=0.8, position=1.5, colormap='tab10')

plt.xlabel('Sub-basin Name')
plt.ylabel('Mean Chemical Levels')
plt.title('Mean Chemical Levels Across Sub-basin')
plt.xticks(rotation=45)
plt.legend(title='Chemical', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
