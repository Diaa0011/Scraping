import requests
import json
import pandas as pd
url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2023014"

payload = {}
headers = {
  'User-Agent': 'put Your user agent here',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.afl.com.au/',
  'x-media-mis-token': '5cbef72ae761e3946a307dc35f2b40c0',
  'Origin': 'https://www.afl.com.au',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'Connection': 'keep-alive',
  'Cookie': 'JSESSIONID=BE7FE5953881BEE2DF3A02AF6316F220'
}


r = requests.get( url, headers=headers)

playerData = r.json()

df = pd.json_normalize(playerData['players'])
# print(df.head())
df.to_csv('playerdata.csv',index=False)

df.to_json('playerdata.json')
