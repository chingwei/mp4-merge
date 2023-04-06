import os

# 不斷請求使用者輸入存在的目錄
while True:
    directory = input("請輸入目錄名稱：")
    if os.path.exists(directory):
        break
    else:
        print("目錄不存在，請重新輸入。")

# 列出目錄下所有 MP4 檔案
mp4_files = sorted([f for f in os.listdir(directory) if f.endswith('.mp4')])

# 取得輸出檔名及輸出目錄
output_dir = os.path.abspath(directory)
output_filename = input("請輸入輸出檔名：")

# 將檔案清單寫入 merge.txt
with open("mp4-merge.txt", "w") as f:
    for file in mp4_files:
        f.write(f"file '{os.path.join(directory, file)}'\n")

# 執行 ffmpeg 指令
command = f"ffmpeg -f concat -safe 0 -i mp4-merge.txt -c copy \"{os.path.join(output_dir, output_filename)}\""
os.system(command)

# 顯示合併完成的檔案位置
print(f"已合併完成，輸出檔案位置：{os.path.abspath(os.path.join(output_dir, output_filename))}")
