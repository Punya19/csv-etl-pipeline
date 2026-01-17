
import pandas as pd
import os
import emoji  

input_file = "olist_order_reviews_dataset.csv"
output_folder = "C:/Users/User/Desktop/assignment/"
file_path = os.path.join(output_folder, input_file)

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='') if isinstance(text, str) else text


df = pd.read_csv(file_path)

columns_to_clean = ['review_comment_title', 'review_comment_message']
for col in columns_to_clean:
    df[col] = df[col].apply(remove_emoji)  
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True)  
    df[col] = df[col].str.strip()  

df['review_comment_title'].replace(r'^\s*$', pd.NA, regex=True, inplace=True)
df['review_comment_message'].replace(r'^\s*$', pd.NA, regex=True, inplace=True)


df['review_comment_title'].fillna('no comments', inplace=True)
df['review_comment_message'].fillna('no comments', inplace=True)


print("\nNull values after final filling:\n", df.isnull().sum())


output_path = os.path.join(output_folder, "cleaned_" + input_file)
df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to: {output_path}")
