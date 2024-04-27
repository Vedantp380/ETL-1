import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
path_train = r"C:\Users\pandeyv1581\OneDrive - ARCADIS\Desktop\uploadfiles\train.csv"
path_test = r"C:\Users\pandeyv1581\OneDrive - ARCADIS\Desktop\uploadfiles\test.csv"
train_df = pd.read_csv(path_train)
test_df = pd.read_csv(path_test)

# Separate features and target variable
X = train_df.drop('Rings', axis=1)  # Assuming 'Rings' is the target variable
y = train_df['Rings']

# Define column transformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Length', 'Diameter', 'Height', 'Whole weight', 'Whole weight.1', 'Whole weight.2', 'Shell weight']),
        ('cat', OneHotEncoder(), ['Sex'])
    ])

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = model.predict(X_val)

# Evaluate the model
mse = mean_squared_error(y_val, y_pred)
print(f'Mean Squared Error: {mse}')

# Make predictions on the test set
test_predictions = model.predict(test_df)

# Save predictions to a CSV file
submission_df = pd.DataFrame({'id': test_df['id'], 'Rings': test_predictions})
submission_df.to_csv('submission1.csv', index=False)
