# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# %%
df = pd.read_csv("dataset/Crop_recommendation.csv")

# %%
df.head()

# %%
print("Rows  columns")
df.shape

# %%
df.isnull().sum()

# %%
# Split features and labels CORRECTLY
x = df.iloc[:, :-1]  # All columns except last as features
y = df.iloc[:, -1]  # Only the last column as labels (crop names)

# %%
# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# %%
model = RandomForestClassifier()

# %%
model.fit(x_train, y_train)

# %%
# Evaluate
accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy:.2%}")

# %%
# Make predictions
predictions = model.predict(x_test)
print("\nSample predictions:")
print(predictions[:10])  # Show first 10 predictions

# %%
x_train.head()

# %%
y_train.head()

# %%
new_feature = [[10, 18, 35, 27.79797651, 99.64573002, 6.381975465, 181.6942283]]
predict_crop = model.predict(new_feature)
print("Predicted crop is: ", predict_crop)

# %%
