
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Displaying the first few rows of a DataFrame
print("Head of DataFrame:")
print(df.head())

# Renaming columns
df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)
print("\nRenamed columns:")
print(df)

# Filtering rows based on a condition
young_people = df[df['Years'] < 25]
print("\nYoung people:")
print(young_people)

# Sorting DataFrame by a column
sorted_df = df.sort_values(by='Years', ascending=False)
print("\nSorted DataFrame:")
print(sorted_df)

# Grouping and aggregating data
average_age_by_city = df.groupby('City')['Years'].mean()
print("\nAverage age by city:")
print(average_age_by_city)

# Handling missing values
df.loc[1, 'Years'] = None
df.dropna(inplace=True)
print("\nDataFrame after handling missing values:")
print(df)

# Applying a function to a column
df['Name_Length'] = df['Full Name'].apply(len)
print("\nDataFrame with name lengths:")
print(df)

# Creating a new column with conditions
df['Age_Category'] = pd.cut(df['Years'], bins=[0, 25, 40, float('inf')], labels=['Young', 'Adult', 'Senior'])
print("\nDataFrame with age categories:")
print(df)

# Merging DataFrames
df2 = pd.DataFrame({'City': ['New York', 'San Francisco', 'Los Angeles'],
                    'Population': [8_398_748, 883_305, 3_979_576]})
merged_df = pd.merge(df, df2, on='City', how='left')
print("\nMerged DataFrame:")
print(merged_df)

# Pivoting DataFrame
pivoted_df = df.pivot(index='Full Name', columns='City', values='Years')
print("\nPivoted DataFrame:")
print(pivoted_df)

# Stacking and unstacking
stacked_df = df.stack()
unstacked_df = stacked_df.unstack()
print("\nStacked and Unstacked DataFrame:")
print(unstacked_df)

# Resampling time series data
date_rng = pd.date_range(start='2022-01-01', end='2022-01-05', freq='D')
time_series_df = pd.DataFrame(date_rng, columns=['date'])
time_series_df['data'] = range(len(date_rng))
resampled_df = time_series_df.resample('2D', on='date').sum()
print("\nResampled Time Series DataFrame:")
print(resampled_df)
