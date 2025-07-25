# Import required libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load your dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")  # Update path if needed

# 2. Prepare data (exactly as in your notebook)
X = df.drop('label', axis=1)  # Features
y = df['label']               # Target

# 3. Initialize and train model (use same parameters as notebook)
model = RandomForestClassifier(
    n_estimators=100,  # Example parameter - use your notebook values
    random_state=42
)
model.fit(X, y)

# 4. Save the model to .pkl file
with open('crop_model.pkl', 'wb') as file:  # 'wb' = write binary
    pickle.dump(model, file)

print("Model successfully saved as crop_model.pkl")