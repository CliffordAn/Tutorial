import pandas as pd
import re

# Load the Excel file
xl_file = pd.ExcelFile("C:\\Python\\sgpt.xlsx")

# Load the sheets into dataframes
sheet_names = xl_file.sheet_names
df1 = xl_file.parse(sheet_names[0])  # Sheet A
df2 = xl_file.parse(sheet_names[1])  # Sheet B

# Split the 'Diagnose' column into words
words_in_diagnose = df1['Diagnose'].str.split(r'[,\s]\s*', expand=True).stack().reset_index(drop=True)

# Prepare the values in the "BeschreibungOhneRechteckklammer" column
df2['BeschreibungOhneRechteckklammer'] = df2['BeschreibungOhneRechteckklammer'].str.lower()

# Create new columns in df1 to store the result, the code and the found word
df1['Vorhanden'] = False
df1['Code'] = None
df1['gefundenesWort'] = None  # New column

# Get unique words in 'BeschreibungOhneRechteckklammer' column of df_B
words_B = set(df2['BeschreibungOhneRechteckklammer'].str.split(r'[,\s]\s*', expand=True).stack())

# Check if each word in 'Diagnose' column of df_A is present in the unique words of 'BeschreibungOhneRechteckklammer' column of df_B
for idx, row in df1.iterrows():
    words = set(str(row['Diagnose']).split())
    if any(word in words_B for word in words):
        df1.loc[idx, 'Vorhanden'] = True

# Find the corresponding 'Code' for each word in 'Diagnose' in df_A from 'BeschreibungOhneRechteckklammer' in df_B
for idx, row in df1[df1['Vorhanden']].iterrows():
    words = set(str(row['Diagnose']).split())
    for word in words:
        match = df2[df2['BeschreibungOhneRechteckklammer'].str.contains(word, regex=False)]  # Set regex=False
        if not match.empty:
            df1.loc[idx, 'Code'] = match.iloc[0]['Code']
            df1.loc[idx, 'gefundenesWort'] = word  # Write the found word
            break

# Display the first few rows of the updated dataframe from df1
print(df1.head())

# Save df1 as a new Excel file
df1.to_excel("C:\\Python\\DiagnosenMitCode.xlsx", index=False)

#was wohl passiert wenn ich den Code ändere in GutHub
print(df1) #nix 2ter Versuch
