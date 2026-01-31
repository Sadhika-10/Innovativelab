import pandas as pd
import sqlite3

print("🚀 Food Delivery Dataset Analysis")

# Load datasets (orders.csv, users.json, restaurants.sql)
orders = pd.read_csv('orders.csv')
users = pd.read_json('users.json')

conn = sqlite3.connect(':memory:')
with open('restaurants.sql', 'r') as f:
    conn.executescript(f.read())
restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
conn.close()

# Merge using LEFT JOIN (retains ALL orders)
final_df = orders.merge(users, on='user_id', how='left').merge(restaurants, on='restaurant_id', how='left')

# Save FINAL dataset
final_df.to_csv('final_food_delivery_dataset.csv', index=False)

print(f"✅ FINAL DATASET CREATED!")
print(f"📊 Rows: {final_df.shape[0]} | Columns: {len(final_df.columns)}")
print(f"💰 Total Revenue: ₹{final_df['total_amount'].sum():,.0f}")
print(f"👥 Distinct Users: {final_df['user_id'].nunique()}")
print("🎉 READY FOR GITHUB!")
