import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("processed_medal_predictions.csv")

# Feature selection
X = df[['Sport_Code', 'Total_Country_Medals']]
y = df['Medal_Percentage']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)
y_pred = [min(100, max(0, val)) for val in y_pred]  # Ensure percentage is between 0 and 100

# Classification report
classification_labels = [1 if val >= 50 else 0 for val in y_test]
predicted_labels = [1 if val >= 50 else 0 for val in y_pred]
class_report = classification_report(classification_labels, predicted_labels, output_dict=False)

# Save model and classification report
with open("rf_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

with open("classification_report.txt", "w") as f:
    f.write(class_report)

print("Model and classification report saved!")
