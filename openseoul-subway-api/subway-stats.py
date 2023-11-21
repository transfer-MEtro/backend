import os
import requests

date = '20231117'
time = '235959'
url = f'http://openapi.seoul.go.kr:8088/sample/json/CardSubwayStatsNew/1/5/{date}'

response = requests.get(url)

# Get the directory of the current script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Define the new directory
new_dir = 'json_responses/subway-stats'

# Join the directory with the new directory
new_dir_path = os.path.join(dir_path, new_dir)

# Check if the new directory exists, if not, create it
if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

# Join the directory with the filename
file_path = os.path.join(new_dir_path, f'sample_response_{date}_{time}.json')

# Save to new file
with open(file_path, 'wb') as file:
    # Write the content of the response to the file
    file.write(response.content)
