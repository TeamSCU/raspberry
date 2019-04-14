# raspberry
树莓派端
# 环境要求
Python2.7
# 所需硬件
树莓派2，pi camera

# 安装说明
#### 安装树莓派
1.	官方网站下载系统
2.	格式化sd卡后使用win32diskimager将系统镜像写入sd卡
3.	接电后即可开启树莓派
#### 配置人脸检测程序运行环境
1.	连接wifi
2.	开启picamera
    > sudo raspi-config  
3.	安装python拓展包
    > sudo apt-get install python-pip  
    > sudo apt-get install python-dev   
    > sudo pip install picamera  
    > sudo apt-get install python-opencv  
4.	下载1.xml文件作为人脸检测的HaarCascade
#### 开启人脸检测
1.	使用python运行camera.py文件即可开启服务
