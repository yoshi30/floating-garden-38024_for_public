from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#api key
key = "7e452645c96c7087997e6b978dbb0c62"
secret = "e89dce418b1b9eb5"

#サーバ負荷考慮
wait_time = 1

# コマンドライン引数の 1 番目の値を取得
search_word = "柴犬"
# 画像を保存するディレクトリを指定
savedir = "./" + search_word

# FlickrAPI にアクセス
# FlickrAPI(キー、シークレット、データフォーマット{json で受け取る})
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    # 検索キーワード
    text = search_word,
    # 取得するデータ件数
    per_page = 400,
    # 検索するデータの種類(ここでは、写真)
    media = 'photos',
    # license(creative commonsに限定) 
    license = "1,2,3,4,5,6,9,10",
    # license = "1","2","3","4","5","6","9","10",
    # データの並び順(関連順)
    sort = 'relevance',
    # UI コンテンツを表示しない
    safe_search = 1,
    # 取得したいオプションの値(url_q->画像のアドレスが入っている情報、licence -> ライセンス情報)
    extras = 'url_q, licence'
)

# 結果を表示
# pprint(result)
photos = result['photos']
# pprint(photos,file=f)

# 画像取得
count = 1
for photo in photos['photo']:
    print(count)
    count =+ 1
    try:
        url_q = photo['url_q']
        filepath = savedir + '/' + photo['id'] + '.jpg'
        # ファイルが重複していたらスキップする
        if os.path.exists(filepath): continue
        # データをダウンロードする
        urlretrieve(url_q, filepath)
        # 重要：サーバを逼迫しないように 1 秒待つ
        time.sleep(wait_time)
    except:
        pass