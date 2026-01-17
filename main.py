# import pandas as pd
# import os
# input_file = "cleaned_olist_order_reviews_dataset.csv"  
# output_folder = "C:/Users/User/Desktop/assignment/cleaned/"
# df = pd.read_csv(input_file)
# See what is actually present in those "empty" cells


# print(df.info())
# print(df.duplicated())
# print(df[df['review_comment_title'].isna()])
# print(df[df['review_comment_message'].isna()])

# print(df.isnull().sum())
# print(df.dtypes)
# output_file = "cleaned_customer_data.csv" 
# df.to_csv(output_file, index=False)
# print(f"\n Cleaned data: {output_file}")




# import pandas as pd
# import os

# input_files = [
#     "olist_customers_dataset.csv",
#     "olist_geolocation_dataset.csv",
#     "olist_order_items_dataset.csv",
#     "olist_order_payments_dataset.csv",
#     "olist_sellers_dataset.csv",
#     "product_category_name_translation.csv"
# ]

# output_folder = "C:/Users/User/Desktop/assignment/"

# for file in input_files:
#     file_path = os.path.join(output_folder, file)
    

#     df = pd.read_csv(file_path)
    
   
#     print(f"\n File: {file}")
#     print(df.info())
#     print("Duplicated rows:", df.duplicated().sum())
#     print("Null values:\n", df.isnull().sum())
#     print("Data types:\n", df.dtypes)
    
#     # Save cleaned file (if needed, you can change filename like 'cleaned_' + file)
#     output_path = os.path.join(output_folder, "cleaned_" + file)
#     df.to_csv(output_path, index=False)
#     print(f" Cleaned data saved to: {output_path}")

