import os
import requests
import datetime

line_2 = ['시청', '을지로입구', '을지로3가', '을지로4가', '동대문역사문화공원', '신당', '상왕십리', '왕십리', '한양대', '뚝섬', '성수', '건대입구', '구의', '강변', '잠실나루', '잠실', '잠실새내', '종합운동장', '삼성', '선릉', '역삼', '강남', '교대', '서초', '방배',
          '사당', '낙성대', '서울대입구', '봉천', '신림', '신대방', '구로디지털단지', '대림', '신도림', '문래', '영등포구청', '당산', '합정', '홍대입구', '신촌', '이대', '아현', '충정로', '용답', '신답', '용두', '신설동', '도림천', '양천구청', '신정네거리', '까치산']


def extract_json():
    # Get key here: https://data.seoul.go.kr/dataList/OA-12764/F/1/datasetView.do
    user_key = '7a56424b6173756e333449616b4563'
    station = '신촌'
    url = f'http://swopenAPI.seoul.go.kr/api/subway/{user_key}/json/realtimeStationArrival/0/30/{station}'

    response = requests.get(url)

    data = response.json()

    # Extracting the 'realtimeArrivalList' part of the data
    realtime_arrival_list = data['realtimeArrivalList']

    return realtime_arrival_list


###############################################
# # SAVING TO NEW FILE
# # Get the directory of the current script
# dir_path = os.path.dirname(os.path.abspath(__file__))

# # Define the new directory
# new_dir = 'json_responses/realtime'

# # Join the directory with the new directory
# new_dir_path = os.path.join(dir_path, new_dir)

# # Check if the new directory exists, if not, create it
# if not os.path.exists(new_dir_path):
#     os.makedirs(new_dir_path)

# # Get the current time
# now = datetime.datetime.now()

# # Format the current time into a string
# time_str = now.strftime('%Y%m%d_%H%M%S')

# # Join the new directory with the filename
# file_path = os.path.join(new_dir_path, f'realtime_{station}-{time_str}.json')

# # Save to new file
# with open(file_path, 'wb') as file:
#     # Write the content of the response to the file
#     file.write(response.content)
