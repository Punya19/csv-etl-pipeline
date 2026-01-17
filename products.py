
import pandas as pd
import os

input_file = "olist_products_dataset.csv"
output_folder = "C:/Users/User/Desktop/assignment/"
file_path = os.path.join(output_folder, input_file)


df = pd.read_csv(file_path)
mode_value = df['product_category_name'].mode()[0]
df['product_category_name'].fillna(mode_value, inplace=True)
df['product_category_name'].head()
df['product_description_lenght'].fillna(df['product_description_lenght'].median(), inplace=True)
df['product_name_lenght'].fillna(df['product_name_lenght'].median(), inplace=True)
df['product_photos_qty'].fillna(0, inplace=True)
for col in ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']:
    df[col].fillna(df[col].median(), inplace=True)
print(df.isnull().sum())


output_path = os.path.join(output_folder, "cleaned_" + input_file)
df.to_csv(output_path, index=False)
print(f" Cleaned data saved to: {output_path}")
