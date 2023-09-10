#!D:/CodingPrograms/Python311/python
print("Content-Type: text/html")
print()
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!DOCTYPE html>
<html>
<head>
    <title>문자열 정리</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1><a href="index.html">메인</a></h1>
    <h3><a href="python.html">돌아가기</a></h3>
    <h2>{title}</h2>
    <ul>
      <pre>파이썬에서 문자
        " "사이에 있는 내용들이 문자로 취급된다.
        ' '사이에 있는 내용들이 문자로 취급된다.
        "를 문자열로 취급하고 싶으면 \"를 사용하면 문자로 취급된다.
        print('Hello')
        print('World')를 작성하면 Hello와 World 사이에 엔터(줄 바꿈)이 적용된다.
        파이썬에서 엔터를 하려면 "\n"을 사용하면 엔터(줄바꿈)가 적용된다.
        """로 시작하고 """로 끝내면 html에서의 &lt;pre&gt;와 같은 역할을 한다.
        Ex) print("""Hello
            World""")
      </pre>
      <pre>비교 연산자(관계연산자)
        ==  같으면 true, 틀리면 false
        !=  틀리면 true, 같으면 false
        &lt;  a&lt;b a가 b보다 작으면 true,크면 false
        &gt;  a&gt;b b가 a보다 작으면 true,크면 false
        &lt;=  a&lt;=b a가 b보다 작거나 같으면 true, 크면 false
        &gt;=  a&gt;=b a가 b보다 작거나 같으면 true, 크면 false
      </pre>
    </ul>
</body>
</html>
'''.format(title=pageId))