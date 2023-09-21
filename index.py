#!python
print("Content-Type: text/html")
print()
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi, os
form = cgi.FieldStorage()

listStr=''
content=''
'''Index(목차) 생성하는 코드(data 파일에 있는 파일 및 폴더를 목차로 생성/세부 파일이 있으면 폴더를 만들어서 넣을 것 없다면 파일만 넣는다.)'''
rootdir='data'
for file in os.listdir(rootdir):
    name=file.split('.')[0]
    listStr = listStr + '<li><a href="index.py?id={dir}">{name}</a></li>'.format(name=name,dir=file)



'''id가 존재 할 때 = 처음 들어온 페이지가 아님./id가 없을 때 = 처음들어 온 거임 : 메인페이지'''
if 'id' in form: 
    pageId = form["id"].value
    idsp=pageId.split('-')
    idlen=len(idsp)

    if idlen==1:
        idfile=os.path.join(rootdir,pageId)
        if os.path.isdir(idfile):
          for file in os.listdir(idfile):
             name=file.split('-')[1]
             content=content+'<li><a href="index.py?id={subindex}">{name}</a></li>'.format(subindex=file,name=name.split('.')[0])
             title=pageId.split('.')[0]
        else:
           content=open(rootdir+'/'+pageId,'r',encoding='utf-8').read()
           title=pageId.split('.')[0]
    elif idlen==2:
       content=open(rootdir+'/'+idsp[0]+'/'+pageId,'r',encoding='utf-8').read()
       title=pageId.split('.')[0]


else: 
    pageId="Main"
    content=open('data/Main.txt','r',encoding='utf-8').read()
    title='Main'

print('''<!DOCTYPE html>
<html>
<head>
  <title>코딩 공부일지</title>
  <meta charset="utf-8">
  <link href="css/index.css" rel="stylesheet">
</head>
<body>
  <h1 class="main"><a href="index.py?id=Main">메인</a></h1>
  <hr>
  <div class="index">
  <ol>
    <p>목차</p>
      {listStr}
  </ol>
  </div>
  <div class="content">
    <h2>{title}</h2>
    {cont}
  </div>
  <div class="right">

  </div>
  
</body>
</html>
'''.format(title=title, cont=content, listStr=listStr))
