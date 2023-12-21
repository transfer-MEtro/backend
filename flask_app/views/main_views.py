import os
from flask import Blueprint, jsonify, redirect

from ..domain.station_by_line import get_station_by_line
from ..external_api.RealtimeArrival import RealtimeArrival
from ..database.database import get_db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def redirect_root():
    REDIRECT_URL = os.environ.get('REDIRECT_URL')
    return redirect(REDIRECT_URL, code=301)


@bp.route('/lines')
def get_lines():
    return jsonify(get_station_by_line())


@bp.route('/station/<station>')
def get_realtime_arrival_by_station(station: str):
    with get_db().cursor() as cursor:
        sql = '''SELECT btrainNo, subwayId, statnFid, statnTid, statnId, statnNm, barvlDt FROM metro_db.Subway WHERE statnNm = %s;'''
        cursor.execute(sql, (station,))
        result = cursor.fetchall()

        # Convert the result into a list of dictionaries
        result_list = []
        for item in result:

            # Convert the tuple into a dictionary
            item_dict = {
                'trainNumber': item[0],
                'subwayId': item[1],
                'previousStationId': item[2],
                'nextStationId': item[3],
                'stationId': item[4],
                'stationNumber': item[5],
                'estimatedTimeArrival': item[6],
            }
            result_list.append(item_dict)

        return jsonify(result_list)


def insert_data(station):
    # Get the realtime arrival list
    arrival_list = RealtimeArrival().get_realtime_arrival_by_station(station)

    with get_db().cursor() as cursor:
        # Insert data into the table
        insert_sql_template = '''INSERT INTO metro_db.Subway
                    (btrainNo, subwayId, statnFid, statnTid, statnId, statnNm, barvlDt)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    subwayId = VALUES(subwayId),
                    statnFid = VALUES(statnFid),
                    statnTid = VALUES(statnTid),
                    statnId = VALUES(statnId),
                    statnNm = VALUES(statnNm),
                    barvlDt = VALUES(barvlDt);'''

        for item in arrival_list:
            # Extract variables from each dictionary in the list
            btrainNo = item['btrainNo']
            subwayId = item['subwayId']
            statnFid = item['statnFid']
            statnTid = item['statnTid']
            statnId = item['statnId']
            statnNm = item['statnNm']
            barvlDt = item['barvlDt']

            # Print the SQL statement
            cursor.execute(insert_sql_template, (btrainNo, subwayId,
                                                 statnFid, statnTid, statnId, statnNm, barvlDt))
            # Commit the transaction
            cursor.connection.commit()
        return f"Number of rows inserted: {cursor.rowcount}"


@bp.route('/insert')
def insert():
    insert = insert_data("신촌")
    return insert


@bp.route('/insert/<line>')
def insert_line(line):
    # List of stations for each line
    line_map = get_station_by_line()
    # Decide which line's data to insert based on the URL parameter
    if line not in ('2', '3'):
        return "Invalid line number"

    for station in line_map[line]['stations']:
        insert_data(station)
    return f"Data inserted for line {line}"
