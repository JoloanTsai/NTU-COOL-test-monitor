# NTU-COOL 線上測驗提醒


利用selenium爬取 NTU COOL上的測驗
一開始會先讀取指定網址的測驗數量，之後會每隔13秒（可自行更改）重新爬取一次<br/>當測驗數量增加時會播放指定路經的音檔

<h3>使用方法</h3>

將程式碼前四行的變數填入NTU COOL的帳密（僅用來登入NTU COOL）
、測驗網址、音檔路徑

<h3>先前設定</h3>

須先pip install selenium 、 pip install pygame

須在同個資料夾內安裝ChromeDriver(下載網址：https://chromedriver.chromium.org/downloads)
將資料夾名稱設為driver
![截圖 2023-12-04 下午1 49 53](https://github.com/JoloanTsai/NTU-COOL-test-monitor/assets/134209558/0a09d3f6-ec0d-40a2-bab6-a50737e415db)



（此程式運行在macOS下）
