# coding: utf-8

import os,time
import shutil
import datetime

dst = "F:\\data\\EL picture\\测试" #文件存储路径
dirset = set()  #程序访问过的文件夹字典

'''
now=datetime.datetime.now()
month = now.strftime('%m')
day = now.strftime('%d')
'''
today = datetime.date.today()       #获得今天的日期
today_month = today.strftime('%y-%m-%d').split('-')[1]
today_day = today.strftime('%y-%m-%d').split('-')[2]

yesterday = today - datetime.timedelta(days=1)          #用今天日期减掉时间差，参数为1天，获得昨天的日期
yesterday_month = yesterday.strftime('%y-%m-%d').split('-')[1]
yesterday_day = yesterday.strftime('%y-%m-%d').split('-')[2]

def copy_file(path):
    os.chdir(path)                                          # 进入文件夹
    for each_file in os.listdir("."):
        if os.path.isfile(each_file):                       # 如果文件夹内是文件
            shutil.copy(each_file, dst + "\\" + each_file)  # 复制文件至指定路径
            print("Copy file from %s to %s " % (os.getcwd() + each_file, dst + "\\" + each_file))
        else:
            if each_file in dirset:                         # dirset字典是为了防止每次调用 copy_file(path) 函数会出现循环进入某一个文件夹
                continue
            dirset.add(each_file)
            copy_file(each_file)                            # 如果文件夹内的东东是文件夹，那么仍调用此函数继续
            os.chdir("..")                                  # 由于使用了递归，当操作完毕，需返回上一级目录

'''
if __name__ == "__main__" :
    src = "//192.168.0.253//设备工艺//10.23D/L6/24.无规律麻点"   #目标路径
    dst = "F:\\data\\EL picture\\测试" #存储路径
    dirset = set()  #程序访问过的文件夹字典
    copy_file(src)

'''


# 复制today文件夹下的图片内容到本地
def copy_today(el_type):
    dir2 = "//192.168.0.253//设备工艺//%s.%sD"%(today_month,today_day)
    for i in os.listdir(dir2):
        two_dir2 = os.path.join(dir2,i)
        if 'lnk' not in two_dir2:
            for j in os.listdir(two_dir2):
                three_dir2 = os.path.join(two_dir2,j)
                if el_type in three_dir2:
                    #copy_file(three_root)
                    #print(three_root)
                    middle_dir2 = three_dir2.replace('\\', '/')  # '//192.168.0.253//设备工艺//10.23D\L4\24.无规律麻点'替换为'//192.168.0.253//设备工艺//10.23D/L4/24.无规律麻点'
                    #print(middle_root)
                    copy_file(middle_dir2)
    print ('复制完毕')


# 复制yesterday文件夹下的图片内容到本地
def copy_yesterday(el_type):
    dir1 = "//192.168.0.253//设备工艺//%s.%sN"%(yesterday_month,yesterday_day)
    for i in os.listdir(dir1):
        two_dir1 = os.path.join(dir1,i)
        if 'lnk' not in two_dir1:
            for j in os.listdir(two_dir1):
                three_dir1 = os.path.join(two_dir1,j)
                for k in os.listdir(three_dir1):
                    four_dir1 = os.path.join(three_dir1,k)
                    if el_type in four_dir1:
                        '''
                        for m in os.listdir(four_root):
                        five_root = os.path.join(four_root,m)
                        print (five_root)
                        '''
                        middle_dir1 = four_dir1.replace('\\', '/')
                        copy_file(middle_dir1)
    print ('复制完毕')




