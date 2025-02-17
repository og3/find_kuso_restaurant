## find_kuso_restaurant
 食べログから評価の低い店を探して、そのリストを作るスクリプト

## 使い方
- ブラウザから検索条件を指定してURLをコピーする
```
https://tabelog.com/rstLst/?pcd=13&LstPrf=A1323&LstAre=A132305&station_id=&Cat=&RdoCosTp=2&LstCos=0&LstCosT=0&vac_net=0&search_date=2025%2F2%2F17%28%E6%9C%88%29&svt=1900&svps=2&svd=20250217&LstRev=0&LstSitu=0&LstReserve=0&LstSmoking=0&PG=1&from_search=&voluntary_search=1&SrtT=rvcn&Srt=D&sort_mode=&LstRange=&keyword=&from_search_form=1&lid=&ChkNewOpen=&hfc=1
```
- URLのrstLstの後ろに{page}を入れてBASE_URLに入れる
```
BASE_URL = "https://tabelog.com/rstLst/{page}?pcd=13&LstPrf=A1323&LstAre=A132305&station_id=&Cat=&RdoCosTp=2&LstCos=0&LstCosT=0&vac_net=0&search_date=2025%2F2%2F17%28%E6%9C%88%29&svt=1900&svps=2&svd=20250217&LstRev=0&LstSitu=0&LstReserve=0&LstSmoking=0&PG=1&from_search=&voluntary_search=1&SrtT=rvcn&Srt=D&sort_mode=&LstRange=&keyword=&from_search_form=1&lid=&ChkNewOpen=&hfc=1"
```
- 以下でスクリプトを実行
```
python find_kuso_restaurant.py
```
以上
## 調査のTips
- 食べログの仕様で、検索結果は20件60ページしか表示されない。
- 「口コミが多い順」でソートすると炎上してるお店が見つかるかも！
- 低評価順でソートすることはできない。
- 評価3.00を下回る店は検索しても見つからない模様。（要検証だが、少なくとも簡単には見つからない）
