# CSV-based ETL Pipeline

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python to process raw CSV datasets.  
It extracts data from multiple CSV files, performs cleaning and transformations, and loads the processed data into new analytics-ready CSV files.

## Tech Stack
- Python
- Pandas

## Project Structure
assignment/
│
├── olist_customers_dataset.csv
├── olist_geolocation_dataset.csv
├── olist_order_items_dataset.csv
├── olist_order_payments_dataset.csv
├── olist_order_reviews_dataset.csv
├── olist_orders_dataset.csv
├── olist_products_dataset.csv
├── olist_sellers_dataset.csv
├── product_category_name_translation.csv
│
├── cleaned_olist_customers_dataset.csv
├── cleaned_olist_geolocation_dataset.csv
├── cleaned_olist_order_items_dataset.csv
├── cleaned_olist_order_payments_dataset.csv
├── cleaned_olist_order_reviews_dataset.csv
├── cleaned_olist_orders_dataset.csv
├── cleaned_olist_products_dataset.csv
├── cleaned_olist_sellers_dataset.csv
├── cleaned_product_category_name_translation.csv
│
├── main.py
├── orders.py
├── products.py
├── reviews.py
├── connect.py
└── dtype.py

## Features
- Extracts data from multiple raw CSV files
- Cleans and transforms data (handles missing values, data types, formatting)
- Loads transformed data into new CSV files ready for analysis
- Modular pipeline design for scalability and reusability

