import base64

  # Open the MP3 file in binary read mode
with open(r'C:\Users\Admin\Desktop\Uzavarsakthi Project\recording_files\4185343 qus.mp3', "rb") as mp3_file:
            # Read the binary data
     binary_data = mp3_file.read()
            # Encode the binary data to Base64
     base64_bytes = base64.b64encode(binary_data)
            # Convert Base64 bytes to a string
     base64_string = base64_bytes.decode('utf-8')
            # Print the Base64 string
     print(base64_string)