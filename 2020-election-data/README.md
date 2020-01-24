###### tags: `PTS`,`P#新聞實驗室`,`election`,`資料新聞`
# readme

## Overview

這些資料用於2020公視P#新聞實驗室透視大選專題：
- 選後分析
    - [2020總統立委大選亮點一次看](https://www.facebook.com/pnnpts/posts/10158084357153833)

- 補助款專題相關
    - 《P#新聞實驗室》透視大選系列專題「[選票變現金-200億補助款一次看](https://newmedia.pts.org.tw/subsidy/)」，分析1994年至今政黨、個人補助款概況。
    - 帶職參選分析「[不只韓國瑜！2020有56立委候選人帶職參選](https://newmedia.pts.org.tw/subsidy/article-2/)」
    - 帶職參選2020選後分析「[選舉補助款超支　14.6億流向一次看](https://newmedia.pts.org.tw/subsidy/article-3/)」

## Note


### 立委資料
- 本資料為python爬取版本，詳細請參考`legislatorAll.py`

### 帶職參選計算
- 帶職參選的計算依據為先前的補助款專題資料，經過google spreadsheet的vlookup及樞紐分析完成（可參考此[資料](https://github.com/ptstaiwan/pts-data/tree/master/subsidy-data)）
        

## Datasets

* legislatorAll（除不分區）：第3屆至第10屆的立委選舉資料
    * 計算方式：
        * 依據中選會資料庫彙整資料與設定欄位
    * 資料來源：中選會
    * 欄位名稱：`region,name,number,gender,birthYear,party,number of votes,percentage of votes,elected,incumbent,type of election,identity`


## License
- 所有資料為 CC-0
