import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from dt.csv
data = pd.read_csv('appstore_instagram_reviews_anonymized.csv')

# Check column names and print them out
print(data.columns)

# Create subplots for the specified columns
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot App Id if it exists
if 'appId' in data.columns:
    sns.countplot(x='appId', data=data, ax=axs[0, 0])
    axs[0, 0].set_title('App Id')
else:
    print("'appId' column not found in the DataFrame.")

# Plot Country if it exists
if 'country' in data.columns:
    sns.countplot(x='country', data=data, ax=axs[0, 1])
    axs[0, 1].set_title('Country')
else:
    print("'country' column not found in the DataFrame.")

# Plot Score if it exists
if 'score' in data.columns:
    sns.countplot(x='score', data=data, ax=axs[1, 1])
    axs[1, 1].set_title('Score')
else:
    print("'score' column not found in the DataFrame.")

plt.tight_layout()
plt.show()
