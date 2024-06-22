import qrcode

# The text that you want to convert into a QR code
input_text = input("\nEnter the text you want to print in the QR code:\n\n--> ") 
generated_qr_name = input("\nWhat is the name of the generated qr code:\n\n--> ")

# Create a QR Code object with the given settings
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each module (box) in the QR code
    border=4,  # Number of border modules around the QR code
)

# Add the text to the QR code object
qr.add_data(input_text)

# Generate the QR code
qr.make(fit=True)

# Create an image object from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save(f"/Users/mark85/Desktop/{generated_qr_name}.png")
