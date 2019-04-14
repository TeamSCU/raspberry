# raspberry
树莓派端
# 环境要求
Python2.7
# 所需硬件
树莓派2，pi camera

# 安装说明
首先安装好树莓派系统，连接树莓派摄像头，并开启摄像头
> sudo raspi-config  

之后选择摄像头并开启  
安装python拓展包，并下载人脸识别的XML到同级目录下

> sudo apt-get install python-pip  
> sudo apt-get install python-dev   
> sudo pip install picamera  
> sudo apt-get install python-opencv  

使用python2运行代码，即可成功开启树莓派人脸检测
