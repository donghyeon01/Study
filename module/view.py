#!python
import os

'''Index(목차) 생성하는 코드(data 파일에 있는 파일 및 폴더를 목차로 생성/세부 파일이 있으면 폴더를 만들어서 넣을 것 없다면 파일만 넣는다.)'''
def getList():
    rootdir='data'
    listStr=''
    for file in os.listdir(rootdir):
        name=file.split('.')[0]
        listStr = listStr + '<li><a href="index.py?id={dir}">{name}</a></li>'.format(name=name,dir=file)
    return listStr