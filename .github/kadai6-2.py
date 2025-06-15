# kadai6-2.py
# 【参照するオープンデータ】横浜市オープンデータポータル - 環境放射線データ
# 【概要】横浜市内の放射線量を観測した時系列データ（リアルタイム）
# 【エンドポイント】https://ckan.open-governmentdata.org/api/3/action/datastore_search
# 【機能】指定されたデータセット（リソースID）から最新の環境放射線データを取得

import requests

resource_id = 'ceacb273-4c70-44cd-a24d-1fbdc3a99f07'  # 環境放射線のリアルタイムデータ
url = 'https://ckan.open-governmentdata.org/api/3/action/datastore_search'

params = {
    'resource_id': resource_id,
    'limit': 5  # 最新の5件を取得
}

response = requests.get(url, params=params)
data = response.json()

# 放射線量と測定時刻の表示
for record in data['result']['records']:
    print(f"{record['測定日時']} - {record['測定値']} {record['単位']}")
