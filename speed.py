import speedtest   # 导入speedtest_cli

print("=====================","\n開始測試您的網路速度...")

# 创建实例对象
test = speedtest.Speedtest()
# 获取可用于测试的服务器列表
print("正在取得伺服器列表...")
test.get_servers()
print("成功！")


# 筛选出最佳服务器
print("正在篩選最佳伺服器...")
best = test.get_best_server()
print("成功！")

print("正在測試(1/2)...")

# 下载速度 
download_speed = int(test.download() / 1024 / 1024)
print("正在測試(2/2)...")
# 上传速度
upload_speed = int(test.upload() / 1024 / 1024)

print("測試完畢！","\n")
print("您的結果為：")
# 输出结果
print("下载速度：" + str(download_speed) + " Mbits")
print("上傳速度：" + str(upload_speed) + " Mbits")
print('延遲：',str(test.results).split(',')[2].split(':')[1].strip(),' ms')

