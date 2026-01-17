
import pandas as pd
import os

input_file = "olist_orders_dataset.csv"
output_folder = "C:/Users/User/Desktop/assignment/"
file_path = os.path.join(output_folder, input_file)

df = pd.read_csv(file_path)
df['order_approved_at'].fillna('pending', inplace=True)
df['order_delivered_carrier_date'].fillna('pending', inplace=True)
df['order_delivered_customer_date'].fillna('pending', inplace=True)
print("Null values after processing:\n", df.isnull().sum())

output_path = os.path.join(output_folder, "cleaned_" + input_file)
df.to_csv(output_path, index=False)
print(f" Cleaned data saved to: {output_path}")
