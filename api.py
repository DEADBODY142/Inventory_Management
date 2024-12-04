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

    try:
        cursor.execute("SELECT name,price FROM inventory_stock WHERE id = ?", (query_id,))
        result = cursor.fetchone()

        if result:
            item_name = result[0]
            item_price = result[1]  
            quan = int(query_quantity)
            total_price = (item_price) * (quan)

            # print(item_price, total_price)
            print(f"item_price: {item_price}, type: {type(item_price)}")
            print(f"query_quantity: {query_quantity}, type: {type(query_quantity)}")

            cursor.execute("UPDATE inventory_stock SET quantity = quantity - ? WHERE id = ?", (query_quantity, query_id))
            
            conn.commit()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO inventory_purchase (item, quantity,price,purchase_at) VALUES (?, ?,?,?)", (item_name, query_quantity,item_price,timestamp))
            
            conn.commit()
            return f"""
                    <div style="text-align: justify; font-size: 50px;">
                        Successfully Purchased!<br>
                        Item name: <b>{item_name}</b><br>
                        Quantity: {query_quantity}<br>
                        Total price: {total_price}<br>
                        Purchased at: {timestamp}
                    </div>
                """, 200


            # return "Sucessfully Purchased", 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
