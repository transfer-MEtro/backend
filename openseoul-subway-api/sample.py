import os
import requests

date = '20220301'
url = f'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayStatsNew/1/5/{date}'

response = requests.get(url)

# Get the directory of the current script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Join the directory with the filename
file_path = os.path.join(dir_path, f'sample_response_{date}.xml')

# Save to new file
with open(file_path, 'wb') as file:
    # Write the content of the response to the file
    file.write(response.content)
