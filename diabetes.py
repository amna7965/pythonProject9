import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame loaded from your dataset
# For demonstration, I'll create a sample DataFrame with random data
data = {
    'Pregnancies': [6, 1, 8, 1, 0],
    'Glucose': [148, 85, 183, 89, 137],
    'BloodPressure': [72, 66, 64, 66, 40],
    'SkinThickness': [35, 29, 0, 23, 35],
    'Insulin': [0, 0, 0, 94, 168],
    'BMI': [33.6, 26.6, 23.3, 28.1, 43.1],
    'DiabetesPedigreeFunction': [0.627, 0.351, 0.672, 0.167, 2.288]
}

df = pd.DataFrame(data)

# Plot histograms for each column
fig, axs = plt.subplots(3, 3, figsize=(15, 10))

for i, col in enumerate(df.columns):
    ax = axs[i // 3, i % 3]
    ax.hist(df[col], bins=10)
    ax.set_title(col)

plt.tight_layout()
plt.show()