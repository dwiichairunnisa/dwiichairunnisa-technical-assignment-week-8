from flask import Flask, request
from db_location import locationn
import datetime

app = Flask(__name__)
@@ -9,6 +10,9 @@ def location_api():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    timestamp = datetime.datetime.now()

    locationn(kecepatan=kecepatan,latitude=latitude,longitude=longitude,timestamp=timestamp)

    return{
        "kecepatan": kecepatan,
        "latitude": latitude,
