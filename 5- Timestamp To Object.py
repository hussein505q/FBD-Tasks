from datetime import datetime
import json
def timestampToObject(timestamp):
  #1. here timestamp change to datetime object
  time = datetime.fromtimestamp(timestamp)
  #.2 here timeStr will take the year, month, day
  timeStr = time.strftime('{"year": %Y, "month": %m, "day": %d,')
  #3. here week will be added
  timeStr += ' "week": {}{}'.format(time.isocalendar()[1],"}")
  #4. here will loads the timeStr string to be timeObject JSON(JavaScript Object)
  timeObject = json.loads(timeStr)
  return timeObject
#5. here is the timestamp
timestamp = 1545730073
#6. here the timestamp will be printed as JSON
print(timestampToObject(timestamp))