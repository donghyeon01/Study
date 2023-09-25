#!python
print("Content-Type: text/html")
print()
import sys,codecs,cgi, os, view

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()

content=''
rootdir='data'




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
'''.format(title=title, cont=content, listStr=view.getList()))
