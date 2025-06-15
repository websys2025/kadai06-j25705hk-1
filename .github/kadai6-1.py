# kadai6-1.py
# 【データの種類】労働力調査（基本集計） - 完全失業率（総数、男女別）
# 【エンドポイント】https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 【機能】e-Stat が提供する政府統計 API を使って、完全失業率の時系列データを取得

import requests
import json

API_KEY = 'bc125288c3751b99dd2252aaa8dd798d47c90b8d'  # ←e-StatのAPIキーをここに記入
stats_data_id = '0003422211'   # 労働力調査（基本集計） 完全失業率（例）

url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData'
params = {
    'appId': API_KEY,
    'statsDataId': stats_data_id,
    'lang': 'J',
    'metaGetFlg': 'N',
    'cntGetFlg': 'N',
    'explanationGetFlg': 'N'
}

response = requests.get(url, params=params)
data = response.json()

# データの表示（年度と完全失業率を抽出）
for value in data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']:
    time = value['@time']
    val = value['$']
    print(f'{time}: {val}')
