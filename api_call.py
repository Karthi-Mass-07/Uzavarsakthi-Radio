import requests
import base64
import os
    
api_url = 'https://dhruva-api.bhashini.gov.in/services/inference/pipeline'
headers = {
    'Content-Type': 'application/json',
    'userID'      : '2ec037103f7e4f138f3e7f85fef43801',
    'ulcaApiKey'  : '2209f0ecb5-4cc7-40d5-9c7c-985076ec1258',
    'Authorization': '1gbQu9Urun_SmtAahp5MhMdOJiCPLXMMrxlPvdyRK7xYUyG40CRvCLrmYJomAuGd'
}
file_path = r'C:\Users\Admin\Desktop\Uzavarsakthi Project\recording_files\4132801 qus.mp3'
with open(file_path, 'rb') as audio_file:
    audio_content = base64.b64encode(audio_file.read()).decode('utf-8')
    
payload = {
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
"audioContent":  audio_content
}
]
}
}
try:
   response = requests.post(api_url, headers=headers, json=payload)
   if response.status_code == 200:

    print(response.json())
   else:
        print(f'Error: {response.status_code} - {response.text}')

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
    
output_file = os.path.splitext(os.path.basename(file_path))[0] + '_output.txt'
with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Recording File: {os.path.basename(file_path)}\n\n")
            file.write("Bhashano API Transcription:\n")
            file.write("--------------------------\n")
            file.write(response.text)

print(f"Data for {file_path} has been written to {output_file}")


