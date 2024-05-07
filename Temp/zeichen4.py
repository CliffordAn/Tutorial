import pandas as pd

# Define the file path
file_path = "c:\\python\\Diagnosen.csv"
file_ICD = "c:\\python\\ICD.csv"


# Load the CSV file into a DataFrame
df = pd.read_csv(file_path, sep=";", encoding='utf-8')
df_ICD = pd.read_csv(file_ICD, sep=";", encoding='utf-8')


# Split each line into words, remove commas, and convert to lower case
#df['Words'] = df['Diagnose'].apply(lambda x: x.replace(',', '').lower().split())

df['Words'] = df['Diagnose'].apply(lambda x: x.replace(',', '').replace('(', ' ( ').replace(')', ' ) ').lower().split())

# new cloumn in df 
df = df.assign(ICDBoolean=False)

# Convert df_ICD to a list
icd_list = df_ICD.iloc[:, 0].str.lower().tolist()

#print(icd_list)

print(df.head(10))

# Check if any word in the 'Words' column is in the icd_list
#df['ICDBoolean'] = df['Words'].apply(lambda words: any(word in icd_list for word in words))

#print(df.head(10))



