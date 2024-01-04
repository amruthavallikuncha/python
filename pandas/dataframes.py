
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 22, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Basic DataFrame Operations
shape_of_df = df.shape
head_of_df = df.head()
info_of_df = df.info()
describe_of_df = df.describe()

# Accessing columns
name_column = df['Name']
age_and_city_columns = df[['Age', 'City']]

# Creating a new column
df['Country'] = 'USA'

# Modifying values
df.loc[0, 'Age'] = 26

# Filtering data
young_people = df[df['Age'] < 25]

# Sorting DataFrame
sorted_df = df.sort_values(by='Age', ascending=False)

# Grouping and Aggregation
grouped_by_city = df.groupby('City')
average_age_by_city = grouped_by_city['Age'].mean()

# Handling Missing Data
df.loc[1, 'Age'] = None
df.dropna(inplace=True)
df.fillna(0, inplace=True)

# Advanced DataFrame Operations
# Reading from a CSV file
df_from_csv = pd.read_csv('data.csv')

# Writing to a CSV file
df.to_csv('output.csv', index=False)

# Indexing and selecting data
subset_of_data = df.loc[0:1, ['Name', 'Age']]

# Applying functions to DataFrame
df['Name_Length'] = df['Name'].apply(len)

# Concatenating DataFrames
df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Age': [30, 35], 'City': ['Chicago', 'Houston']})
concatenated_df = pd.concat([df, df2], ignore_index=True)

# Merging DataFrames
df3 = pd.DataFrame({'City': ['New York', 'San Francisco', 'Los Angeles'],
                    'Population': [8_398_748, 883_305, 3_979_576]})
merged_df = pd.merge(df, df3, on='City', how='left')

# Pivoting DataFrames
pivoted_df = df.pivot(index='Name', columns='City', values='Age')

# Reshaping DataFrames with melt
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'City'])

# Using applymap to apply a function element-wise
df_numeric = df[['Age']]
squared_df = df_numeric.applymap(lambda x: x**2)

# Creating a datetime column
df['Birthdate'] = pd.to_datetime(['1995-05-15', '2000-02-20', '1994-08-10'])

# Extracting components from datetime
df['Birth_Year'] = df['Birthdate'].dt.year

# Setting and resetting index
df.set_index('Name', inplace=True)
df.reset_index(inplace=True)

# Filtering with boolean conditions
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'New York')]

# Handling duplicates
df.drop_duplicates(subset=['City'], keep='first', inplace=True)

# Using isin for filtering
selected_cities = df[df['City'].isin(['New York', 'Chicago'])]

# Grouping with multiple columns
grouped_by_age_and_city = df.groupby(['Age', 'City'])

# Iterating through DataFrame rows
for index, row in df.iterrows():
    print(row['Age'], row['City'])
