# AutoComparePickup-with-ITAM ![VERSION](https://img.shields.io/badge/Version-3.6.1-green.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
# 領貨清單與KB上的BataBase做比對
## 此程式可實現
  - 自動打卡
  - 自動填入溫度
  - 配合 Linux Crontab 可排程每日自動打卡，每日自動填寫溫度。

## Logs
   * ver V3.6.1
     - 新增MR類型處理。需在地區欄位輸入 "MR-****" *字號為自動匹配 "專案名稱"。
     - 新增地區 "END" 選項。當偵測到END字樣，即會結束程式，不會再往下方執行，方便在表格下方放一些常用內容快速貼上使用。
   * ver V3.6
     - 配合Selenium棄用舊版語法，大改網頁互動語法，並升級編譯至 Python 3.10，有Bug幫忙回報3Q。
     - 新增多瀏覽器支援。
     - Windows 預設使用 Chrome
     - Linux 預設使用 Chrome 不帶GUI
     - MacOS 預設使用 Firefox

   * ver 3.5.5
     - 配合PPMS網頁框架調整，修正無法使用問題。以往版本並不相容。
     - 增強功能:Excel中的送出資料欄位。
     - 現在可以填寫下面三種參數。
     - "y" 代表填資料並送出。
     - "n" 代表填資料但不送出，適合測試有沒有填寫錯誤。
     - "s" 代表略過，已經成功送出過的資料就不需要再重複跑。
   * V3.5.5-2 
     - 修正更新敘述，強化部分判斷邏輯，原先xpath鎖定元素，改為link文字判斷。
   * V3.5.5-3
     - 加入靜默模式，不開啟瀏覽器。採用WebDriver直接處理數據。
   * 3.5.4
     - 新增功能:如果表格中有帶N表示不送出資料的話，會直接略過。



## Useage
    #Init for Virtual Env 建立虛擬環境。
    virtualenv venv
    
    #Active Virtual Env 進入虛擬環境。
    source ./venv/bin/activate
    
    #Install Requirements 安裝所需要之套件。
    pip install -r requirements.txt
    
    #Use it 準備就緒，可以直接執行，看看結果再行調整。
    python ./main.py
    
    or （如果想要打包為單一執行檔，下面就是打包的指令。）
    pyinstaller -F ./main.py -n ./AutoPPMS-v3.6 -i ico.ico
    or pyinstaller -F ./main.py -n ./AutoPPMS-v3.6.1.b -i pain.ico (胖神ico)
    
    #運作結束後，離開虛擬環境。
    deactivate
