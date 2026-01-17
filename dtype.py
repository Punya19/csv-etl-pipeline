# import mysql.connector

# # Database configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'Punya19@2003'  # Replace with your real MySQL root password
# }

#
# try:
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()

#     # Step 2: Create database if it doesn't exist
#     cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
#     print("Database 'my_database' ensured to exist.")

#     cursor.close()
#     conn.close()
# except mysql.connector.Error as err:
#     print(f" Error creating database: {err}")

#
# try:
#     db_config['database'] = 'my_database'  # Add database name to config
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()

#     # Step 4: Create table with appropriate datatypes
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS olist_customers (
#         customer_id VARCHAR(50) PRIMARY KEY,
#         customer_unique_id VARCHAR(50),
#         customer_zip_code_prefix INT,
#         customer_city VARCHAR(100),
#         customer_state CHAR(2)
#     );
#     """

#     cursor.execute(create_table_query)
#     print(" Table 'olist_customers' created successfully in 'my_database'.")

# except mysql.connector.Error as err:
#     print(f" Error creating table: {err}")

# finally:
#     # Step 5: Close connection
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
#     print("Database connection closed.")




import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123'  
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
    print("Database 'my_database' ensured to exist.")

    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f" Error creating database: {err}")

try:
    db_config['database'] = 'my_database'
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()



    # 1. olist_customers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_customers (
        customer_id VARCHAR(50) PRIMARY KEY,
        customer_unique_id VARCHAR(50),
        customer_zip_code_prefix INT,
        customer_city VARCHAR(100),
        customer_state CHAR(2)
    );
    """)
    print(" Table 'olist_customers' created.")

    # 2. olist_geolocation
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_geolocation (
        geolocation_zip_code_prefix INT,
        geolocation_lat FLOAT,
        geolocation_lng FLOAT,
        geolocation_city VARCHAR(100),
        geolocation_state CHAR(2)
    );
    """)
    print(" Table 'olist_geolocation' created.")

    # 3. olist_order_items
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_order_items (
        order_id VARCHAR(50),
        order_item_id INT,
        product_id VARCHAR(50),
        seller_id VARCHAR(50),
        shipping_limit_date DATETIME,
        price FLOAT,
        freight_value FLOAT
    );
    """)
    print(" Table 'olist_order_items' created.")

    # 4. olist_order_payments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_order_payments (
        order_id VARCHAR(50),
        payment_sequential INT,
        payment_type VARCHAR(50),
        payment_installments INT,
        payment_value FLOAT
    );
    """)
    print("Table 'olist_order_payments' created.")

    # 5. olist_sellers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_sellers (
        seller_id VARCHAR(50) PRIMARY KEY,
        seller_zip_code_prefix INT,
        seller_city VARCHAR(100),
        seller_state CHAR(2)
    );
    """)
    print(" Table 'olist_sellers' created.")

    # 6. product_category_name_translation
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_category_name_translation (
        product_category_name VARCHAR(50) PRIMARY KEY,
        product_category_name_english VARCHAR(50)
    );
    """)
    print(" Table 'product_category_name_translation' created.")

    #7.olist_reviews
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_reviews (
         review_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    review_score INT,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
    );
    """)
    print(" Table 'olist_reviews' created.")

     #8 olist_orders 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_orders (
         order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    order_status char(50),
    order_purchase_timestamp  VARCHAR(50),
   order_approved_at  TEXT,
  order_delivered_carrier_date VARCHAR(50),
  order_delivered_customer_date  VARCHAR(50),
     order_estimated_delivery_date  VARCHAR(50)            
    );
    """)
    print(" Table 'olist_orders' created.")

# 9 olist_products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS olist_products (
         product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(100),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT           
    );
    """)
    print("Table 'olist_orders' created.")


except mysql.connector.Error as err:
    print(f" Error creating tables: {err}")

finally:

    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print(" Database connection closed.")
