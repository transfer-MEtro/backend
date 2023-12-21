from flask import Blueprint, jsonify

from flask_app.domain.station_by_line import get_station_by_line
from flask_app.external_api.RealtimeArrival import RealtimeArrival
from flask_app.database.database import get_db

bp = Blueprint('main', __name__, url_prefix='/')


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
