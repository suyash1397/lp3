import pandas as pd

# Load your Netflix dataset
data = pd.read_csv('netflix_dataset.csv')

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Set a threshold to determine if ratings are given on the basis of cast
threshold = 0.2  # You can adjust this threshold as needed

# Calculate the correlation between 'Cast' and 'Rating'
cast_rating_correlation = data['Cast'].corr(data['Rating'])

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Print the correlation between 'Cast' and 'Rating'
print("Correlation between 'Cast' and 'Rating':", cast_rating_correlation)

if cast_rating_correlation > threshold:
    print("There is a positive correlation between cast and ratings.")
else:
    print("There is no strong correlation between cast and ratings.")
