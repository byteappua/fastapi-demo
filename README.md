# windows部署 
## 下载nssm
https://nssm.cc/download
把nssm.exe的文件夹路径设置到path中
## 安装服务
nssm install "xtquant-api" "C:\ProgramData\anaconda3\python.exe" "E:\dev\byteappua\xtquant-api\main.py"
## 启动服务
nssm start xtquant-api