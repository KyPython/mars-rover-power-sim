import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load your CSV data
print("Loading sensor_data.csv...")
df = pd.read_csv('sensor_data.csv')
X = df.drop('label', axis=1).values
y = df['label'].values

# Train model (same as before)
model = RandomForestClassifier(n_estimators=20, max_depth=10).fit(X, y)

# Simulate predictions on test data
print("\nSimulating embedded decision loop on test data:")
for i, (features, label) in enumerate(zip(X, y)):
    pred = model.predict([features])[0]
    print(f"Sample {i+1}: Input={features}, True Label={label}, Predicted={pred}")

# Optionally, test on new synthetic data
import numpy as np
print("\nSimulating on new synthetic sensor data:")
for i in range(3):
    sample = np.random.uniform(0, 1, X.shape[1])
    pred = model.predict([sample])[0]
    print(f"Synthetic Sample {i+1}: Input={sample}, Predicted={pred}")
