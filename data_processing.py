import pandas as pd
import glob

# Step A: Find the three data files
files = glob.glob('data/daily_sales_data_*.csv')
print(f"Found {len(files)} files.")

# Step B: Read them into a list
df_list = []
for file in files:
    df_list.append(pd.read_csv(file))

# Step C: Combine them into one big table
combined_df = pd.concat(df_list, ignore_index=True)

# 1. Keep ONLY Pink Morsels
df = combined_df[combined_df['product'] == 'pink morsel'].copy()

# 2. Clean the price column (remove the '$' so we can do math)
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

# 3. Create the 'sales' column (quantity * price)
df['sales'] = df['quantity'] * df['price']

# 4. Keep only the 3 columns they asked for
df = df[['sales', 'date', 'region']]

# 5. Save it to a new file
df.to_csv('formatted_sales_data.csv', index=False)

print("Success! 'formatted_sales_data.csv' has been created.")