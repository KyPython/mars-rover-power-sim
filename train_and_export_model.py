import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from micromlgen import port

# Load your CSV data
df = pd.read_csv('sensor_data.csv')
X = df.drop('label', axis=1).values
y = df['label'].values

# Train model
model = RandomForestClassifier(n_estimators=20, max_depth=10).fit(X, y)

# Export to C code
c_code = port(model)
with open('include/model.h', 'w') as f:
    f.write(c_code)
print("Model exported to include/model.h")
