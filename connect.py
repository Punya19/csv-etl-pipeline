
import mysql.connector
import pandas as pd

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Punya19@2003',
    'database': 'my_database'
}


file_table_mapping = {
    'cleaned_olist_customers_dataset.csv': 'olist_customers',
    'cleaned_olist_geolocation_dataset.csv': 'olist_geolocation',
    'cleaned_olist_order_items_dataset.csv': 'olist_order_items',
    'cleaned_olist_order_payments_dataset.csv': 'olist_order_payments',
    'cleaned_olist_sellers_dataset.csv': 'olist_sellers',
    'cleaned_product_category_name_translation.csv': 'product_category_name_translation',
    'cleaned_olist_order_reviews_dataset.csv': 'olist_reviews',
    'cleaned_olist_orders_dataset.csv':'olist_orders',
    'cleaned_olist_products_dataset.csv':'olist_products',
}

CHUNK_SIZE = 1000  


try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print(" Connected to the database successfully.")

    for csv_file, table_name in file_table_mapping.items():
        print(f"\n Inserting data from '{csv_file}' into '{table_name}' in chunks of {CHUNK_SIZE} rows")

        for chunk in pd.read_csv(csv_file, chunksize=CHUNK_SIZE):
            chunk = chunk.where(pd.notnull(chunk), None) 

          
            placeholders = ', '.join(['%s'] * len(chunk.columns))
            columns = ', '.join(chunk.columns)
            insert_query =  f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"


            
            data = [tuple(row) for row in chunk.values]

            try:
                cursor.executemany(insert_query, data)
                conn.commit()
                print(f" Inserted {len(data)} rows into '{table_name}'.")
            except mysql.connector.Error as err:
                print(f" Error inserting chunk into '{table_name}': {err}")

except mysql.connector.Error as err:
    print(f" Database connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("\n Database connection closed.")
