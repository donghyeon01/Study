#!python
print("Content-Type: text/html")
print()
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    content=open('data/'+pageId,'r',encoding='utf-8').read()
else:
    pageId="Main"
    content=open('data/Main','r',encoding='utf-8').read()

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
    <li><a href="index.py?id=Html">HTML</a></li>
    <li><a href="index.py?id=Python">Python</a></li>
    <li><a href="index.py?id=Note">Note</a></li>
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
'''.format(title=pageId, cont=content))
