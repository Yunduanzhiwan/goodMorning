from datetime import datetime
import os


today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
sendKey = os.environ['SEND_KEY']
resTitle = os.environ['TITLE']
