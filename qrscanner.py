# import tkinter as tk
# from PIL import Image, ImageTk
# import qrcode
# import requests

# # Generate QR code
# def generate_qr(quantity,id):
#     # Data for the QR code
#     base_url = "https://f7dx2w3w-5000.inc1.devtunnels.ms/run_query"

#     # Example query parameters (can be dynamic)
#     query_id =id
#     full_url = f"{base_url}?query_id={id}&query_quantity={quantity}"

#     # Generate QR code
#     qr = qrcode.QRCode(version=1, box_size=10, border=5)
#     qr.add_data(full_url)
#     qr.make(fit=True)

#     # Save the QR code as an image    # Create the QR code image in memory
#     qr_img = qr.make_image(fill_color="black", back_color="white")
    
#     # Convert the image to a format usable in Tkinter
#     tk_img = ImageTk.PhotoImage(qr_img)
#     return tk_img

# # Display QR code in Tkinter window
# def display_qr(root,quantity,id):
#     qr_image = generate_qr(quantity,id)
#     label = tk.Label(root, image=qr_image)
#     label.image = qr_image  # Keep a reference to avoid garbage collection
#     label.pack()


import time
import tkinter as tk
from PIL import Image, ImageTk
import qrcode

# Generate QR code for a cart
def generate_qr(cart):
    if not isinstance(cart, list) or not all(isinstance(item, dict) for item in cart):
        raise ValueError("Cart must be a list of dictionaries with 'id' and 'quantity' keys.")

    # Base URL for the API
    base_url = "https://f7dx2w3w-5000.inc1.devtunnels.ms/run_query"

    # Current timestamp
    timestamp = int(time.time())

    # Combine the cart items into query parameters
    query_params = "&".join(
        [f"id_{item['id']}={item['quantity']}" for item in cart]
    )
    # full_url = f"{base_url}?{query_params}"
    full_url = f"{base_url}?{query_params}&timestamp={timestamp}"

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(full_url)
    qr.make(fit=True)

    # Create the QR code image in memory
    qr_img = qr.make_image(fill_color="black", back_color="white")
    tk_img = ImageTk.PhotoImage(qr_img)
    return tk_img

# Display QR code in Tkinter window
def display_qr(root, cart):
    if not cart:
        tk.messagebox.showerror("Error", "Cart is empty! Add items before generating QR.")
        return
    
    qr_image = generate_qr(cart)
    label = tk.Label(root, image=qr_image)
    label.image = qr_image  # Keep a reference to avoid garbage collection
    label.pack()
