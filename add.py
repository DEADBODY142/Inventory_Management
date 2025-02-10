from tkinter import messagebox
from build_scratch import get_what_label
import sqlite3

# Get detected labels
detected_labels = get_what_label()
print("detected_labels: ", detected_labels)
message=""
labels = [data for data in detected_labels.split()]

# Connect to the database once outside the loop
db_connection = sqlite3.connect('db/inventory.db')
connection = db_connection.cursor()

if not labels:  # Check if the labels list is empty
    messagebox.showerror("Error", "No items found")
else:
    try:
        for label in labels:
            if label == "":
                messagebox.showerror("Error", "No items found")
                break
            # Check if price exists
            connection.execute("select price from inventory_price where name=?", (label,))
            result = connection.fetchone()
            if result is None:
                messagebox.showerror("Error", f"No price defined for item: {label}")
                message+=f"No price defined for item: {label}\n"
                continue
            
            price_details = result[0]

            # Check stock details
            connection.execute("select quantity from inventory_stock where name=?", (label,))
            stock_result = connection.fetchone()

            if stock_result:
                # Update quantity if item exists
                quantity = stock_result[0] + 1
                connection.execute("update inventory_stock set quantity=?, price=? where name=?", (quantity, price_details, label))
                print(f"Data updated successfully for {label}")
                message+=f"Data updated successfully for {label}\n"
            else:
                # Insert new item if it doesn't exist
                connection.execute("insert into inventory_stock (name, quantity, price) values (?, ?, ?)", (label, 1, price_details))
                print(f"Data inserted successfully for {label}")
                message+=f"Data inserted successfully for {label}\n"
        
        # Show success message after the loop
        messagebox.showinfo("Success", message)

    # Commit changes to the database
        db_connection.commit()

    except sqlite3.Error as e:
        # Handle database errors
        messagebox.showerror("Database Error", str(e))
    finally:
        # Ensure the database connection is closed
        connection.close()
        db_connection.close()
