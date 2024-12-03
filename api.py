from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/run_query', methods=['GET'])
def run_query():
    from mainmenu import MainPage 
    query_id = request.args.get('query_id')
    query_quantity = request.args.get('query_quantity')

    print(query_id)
    if not query_id:
        return "No query_id provided", 400

    # Connect to your database
    conn = sqlite3.connect('db/inventory.db')
    cursor = conn.cursor()

    # Example query (customize as needed)
    try:
        cursor.execute("SELECT name,price FROM inventory_stock WHERE id = ?", (query_id,))
        result = cursor.fetchone()

        if result:
            item_name = result[0]
            item_price = result[1]  # Extract the item name from the result
              # Extract the item name from the result

            # Step 2: Update the quantity in inventory_stock
            cursor.execute("UPDATE inventory_stock SET quantity = quantity - ? WHERE id = ?", (query_quantity, query_id))
            
            # Commit the update
            conn.commit()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Step 3: Insert the item name into another table (e.g., inventory_log)
            cursor.execute("INSERT INTO inventory_purchase (item, quantity,price,purchase_at) VALUES (?, ?,?,?)", (item_name, query_quantity,item_price,timestamp))
            
            # Commit the insert
            conn.commit()
            return "Sucessfully Purchase", 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
