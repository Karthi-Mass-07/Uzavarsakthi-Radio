import base64
import requests
import json
import os

# Function to convert mp3 to base64
def convert_mp3_to_base64(file_path):
    try:
        # Open the MP3 file in binary read mode
        with open(file_path, "rb") as mp3_file:
            # Read the binary data
            binary_data = mp3_file.read()
            # Encode the binary data to Base64
            base64_bytes = base64.b64encode(binary_data)
            # Convert Base64 bytes to a string
            base64_string = base64_bytes.decode('utf-8')
            # Print the Base64 string
            return base64_string
    except Exception as e:
        print(f"Error converting file {file_path}: {e}")
        return None
    
def call_bhashini_api(base64_string):
    url = 'https://dhruva-api.bhashini.gov.in/services/inference/pipeline'
    headers ={
              'Content-Type': 'application/json',
              'userID'      : 'YOUR USER ID',
              'ulcaApiKey'  : 'YOUR API KEY',
              'Authorization': 'YOUR AUTHORIZATION'
}
    data = {
        "pipelineTasks": [
{
"taskType": "asr",
"config": {
"language": {
"sourceLanguage": "ta"
},
"serviceId":"ai4bharat/conformer-multilingual-dravidian-gpu--t4",
"audioFormat": "mp3",
"samplingRate": 16000
}
}
],
"inputData": {
    "audio": [
{
"audioContent":  base64_string
}
]
}
}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = response.json()
        # Print the response from the API
        print(response_data)
        return response_data
    except Exception as e:
        print(f"Error calling Bhashini API: {e}")
        return None

def write_to_file(file_name, text_output):
    try:
        # Create a text file with UTF-8 encoding and write permissions
        output_file = os.path.splitext(os.path.basename(file_name))[0] + '_output.txt'
        with open("output.txt", "a", encoding="utf-8") as output_file:
            output_file.write(f"File: {file_name}\n")
            output_file.write(f"Text: {text_output}\n\n")
            print(f"Successfully wrote results of {file_name} to output.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")
        
audio_folder = r"(Your Recording files Path)"
        
def process_all_files():
    # Loop through all files in the folder
    for file_name in os.listdir(audio_folder):
        if file_name.endswith(".mp3"):
            file_path = os.path.join(audio_folder, file_name)
            print(f"Processing {file_name}")
            base64_string = convert_mp3_to_base64(file_path)
            if base64_string:
                response = call_bhashini_api(base64_string)
                if response:
                    write_to_file(file_name, response)

# Call the function to process all files
process_all_files()

