import os
import requests
import datetime


class RealtimeArrivalApi:
    SEOUL_API_KEY = os.environ.get('SEOUL_API_KEY')
    SK_API_KEY = os.environ.get('SK_API_KEY')

    def get_realtime_arrival_by_station(self, station):
        '''
        Document: https://data.seoul.go.kr/dataList/OA-12764/F/1/datasetView.do
        '''
        user_key = RealtimeArrivalApi.SEOUL_API_KEY
        url = f'http://swopenAPI.seoul.go.kr/api/subway/{user_key}/json/realtimeStationArrival/0/30/{station}'

        response = requests.get(url)

        data = response.json()

        # Extracting the 'realtimeArrivalList' part of the data
        realtime_arrival_list = data['realtimeArrivalList']

        return realtime_arrival_list

    def get_congestion_by_line_number_and_train_id(self, line_number: str, train_id: str) -> list[int]:
        url = f'https://apis.openapi.sk.com/puzzle/subway/congestion/rltm/trains/{line_number}/{train_id}'

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "appKey": RealtimeArrivalApi.SK_API_KEY,
        }

        response = requests.get(url, headers=headers)

        data = response.json()

        print(data)

        congestions = data['data']['congestionResult']['congestionCar'] \
            .split('|')

        return list(map(int, congestions))
