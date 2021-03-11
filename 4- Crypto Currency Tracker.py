import requests
import time
#1. here is the api's url
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def getLatestBitcoinPrice():
  response = requests.get(url).json()
  return response['bpi']['USD']['rate_float']*3.75

def CryptoCurrencyTracker():
  #2. here, the while loop will loop forever
  while True:
    #2. here is to print the bitcoin in SAR
    print('Bitcoin price = {:.2f} SAR'.format(getLatestBitcoinPrice()))
    #3. here to leep the excution one second to make it print every one second
    time.sleep(1)

CryptoCurrencyTracker()