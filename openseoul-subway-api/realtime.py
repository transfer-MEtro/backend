import os
import requests
import datetime

# Get key here: https://data.seoul.go.kr/dataList/OA-12764/F/1/datasetView.do
user_key = 'your_key_here'
station = '신촌'
url = f'http://swopenAPI.seoul.go.kr/api/subway/{user_key}/json/realtimeStationArrival/0/30/{station}'

response = requests.get(url)

# Get the directory of the current script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Define the new directory
new_dir = 'json_responses/realtime'

# Join the directory with the new directory
new_dir_path = os.path.join(dir_path, new_dir)

# Check if the new directory exists, if not, create it
if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

# Get the current time
now = datetime.datetime.now()

# Format the current time into a string
time_str = now.strftime('%Y%m%d_%H%M%S')

# Join the new directory with the filename
file_path = os.path.join(new_dir_path, f'realtime_{station}-{time_str}.json')

# Save to new file
with open(file_path, 'wb') as file:
    # Write the content of the response to the file
    file.write(response.content)
