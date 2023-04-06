# MP4 檔案合併程式

這是一個使用 Python 撰寫的 MP4 檔案合併程式，使用 FFMPEG 將多個 MP4 檔案合併成一個檔案。

## 使用方法

1. 下載程式原始碼，打開終端機，切換至程式所在目錄。

2. 輸入以下指令執行程式：

~~~
python merge_mp4.py
~~~

3. 程式會要求輸入 MP4 檔案所在的目錄，請輸入存在的目錄。

4. 程式會自動將目錄下所有的 MP4 檔案按檔名由小到大排序，並寫入 merge_video.txt 中。

5. 程式會使用以下指令執行 FFMPEG 合併 MP4 檔案：

~~~
ffmpeg -f concat -safe 0 -i merge_video.txt -c copy output.mp4
~~~

合併完成後，檔案會存放在原始目錄下，檔名為 output.mp4。

6. 程式會顯示合併完成的檔案位置。

## 螢幕截圖

![image](https://github.com/chingwei/mp4-merge/blob/main/mp4-merge.jpg?raw=true)

## 環境要求

- Python 3.6+
- FFMPEG

## 常見問題

- Q: 程式出現 "No such file or directory" 錯誤訊息怎麼辦？
- A: 請確認輸入的目錄是否存在，以及目錄內是否有 MP4 檔案。

- Q: 程式出現 "Unknown encoder 'copy'" 錯誤訊息怎麼辦？
- A: 請確認您已安裝 FFMPEG，並將 FFMPEG 的 bin 目錄加入系統環境變數 PATH 中。

- Q: 程式出現 "Input buffer exhausted before END element found" 錯誤訊息怎麼辦？
- A: 請確認您的 MP4 檔案是否正常，並且沒有被損壞。

## 作者

- Ching-Wei

## 授權

本專案採用 MIT 授權，詳細內容請參閱 LICENSE 檔案。
