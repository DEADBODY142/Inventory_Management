from flask import Flask, request
import sqlite3
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/run_query', methods=['GET'])
def run_query():
    # Parse the timestamp
    timestamp = request.args.get('timestamp', type=int)

    # Validate the timestamp
    if not timestamp:
        return "Missing timestamp", 400

    current_time = int(time.time())
    if current_time - timestamp > 30:  # 30-second validity
        print("\nBARCODE EXPIRED\n")
        return "This URL has expired. Please generate a new QR code.", 404

    # Parse items and quantities from query parameters
    items = {}
    for key, value in request.args.items():
        if key.startswith("id_"):
            item_id = key[3:]  # Extract the item ID after "id_"
            try:
                items[item_id] = int(value)  # Quantity for the item
            except ValueError:
                return f"Invalid quantity for item {item_id}: {value}", 400

    if not items:
        return "No items provided", 400

    # Connect to your database
    conn = sqlite3.connect('db/inventory.db')
    cursor = conn.cursor()

    try:
        total_price = 0
        purchased_items = []

        # Process each item
        for item_id, quantity in items.items():
            cursor.execute("SELECT name, price, quantity FROM inventory_stock WHERE id = ?", (item_id,))
            result = cursor.fetchone()

            if result:
                item_name, item_price, available_quantity = result

                if available_quantity < quantity:
                    return f"Not enough stock for item {item_name} (ID: {item_id})", 400

                item_total_price = item_price * quantity
                total_price += item_total_price

                # Update stock and log the purchase
                cursor.execute("UPDATE inventory_stock SET quantity = quantity - ? WHERE id = ?", (quantity, item_id))
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(
                    "INSERT INTO inventory_purchase (item, quantity, price, purchase_at) VALUES (?, ?, ?, ?)",
                    (item_name, quantity, item_total_price, timestamp)
                )

                purchased_items.append(f"{item_name} (Quantity: {quantity}, Total: {item_total_price})")

            else:
                return f"Item with ID {item_id} not found", 404

        conn.commit()

        # Generate a summary of the purchase
        purchased_items_summary = "<br>".join(purchased_items)
        return f"""
                <div style="text-align: justify; font-size: 20px;">
                    <b>Successfully Purchased!</b><br><br>
                    {purchased_items_summary}<br>
                    <b>Total Price:</b> {total_price}<br>
                    <b>Purchased At:</b> {timestamp}
                </div>
            """, 200

    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
