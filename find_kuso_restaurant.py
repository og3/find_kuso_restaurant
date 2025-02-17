import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 指定する地域のURL（例：東京 -> tokyo）
BASE_URL = "https://tabelog.com/tokyo/A1303/A130301/rstLst/{page}?SrtT=rvcn&LstReserve=0&LstSmoking=0&svd=20250217&svt=1900&svps=2&vac_net=0&Srt=D"

# 取得するページ数（仕様上60件が最大）
MAX_PAGES = 60
# 食べログのスコアの閾値
MIN_SCORE = 3.10

# データ格納用リスト
restaurants = []

# User-Agent（Bot対策用）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# ページごとにスクレイピング
for page in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page)
    print(f"ページ取得中: {url}")
    
    # HTTPリクエスト
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"⚠ ページ取得失敗 (ステータスコード: {response.status_code}): {url}")
        continue
    
    # HTML解析
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 店舗情報を取得
    shop_list = soup.select("div.list-rst")
    
    for shop in shop_list:
        try:
            # 店舗名とURLを取得
            name_tag = shop.select_one("a.list-rst__rst-name-target")
            if not name_tag:
                print("⚠ 店舗名の取得に失敗")
                continue
            name = name_tag.text.strip()
            link = name_tag["href"]
            
            # 星評価を取得
            score_tag = shop.select_one("span.c-rating__val, span.c-rating-v3__val")
            if not score_tag:
                print(f"⚠ 星評価なし: {name}")
                continue
            
            try:
                score = float(score_tag.text.strip())
            except ValueError:
                print(f"⚠ 星評価の取得に失敗: {name}")
                continue
            
            print(f"{name} | {score}")
            
            # 星3.00以下のみをリストに追加
            if score <= MIN_SCORE:
                restaurants.append([name, score, link])
                print(f"⭐ {name} | {score} | {link}")
        
        except Exception as e:
            print(f"⚠ データ取得エラー: {e} (店舗: {name if 'name' in locals() else '不明'})")
            continue
    
    # 1ページ取得ごとにスリープ（Bot対策）
    time.sleep(3)

# CSVに保存
df = pd.DataFrame(restaurants, columns=["店名", "星の数", "URL"])
df.to_csv("low_rating_restaurants.csv", index=False, encoding="utf-8-sig")

print("✅ CSVに保存完了！")
