#!python
print("content-type:text/html; charset=UTF-8\n")
print()
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi, os
form = cgi.FieldStorage()

listStr=''


rootdir='data'
'''
for file in os.listdir(rootdir):
    d=os.path.join(rootdir, file)
    if os.path.isdir(d):
        dlist=d +"/"+ d[5:]
        dsplit=dlist.split('/')
        print(len(dsplit))
        print(dsplit[-1])
print('---')
print(dlist)
'''
'''     
for file in os.listdir(rootdir):
    d=os.path.join(rootdir, file)
    if os.path.isdir(d):
        dlist=d +"\\"+ d[5:]
        dsplit=dlist.split('\\')
        print(len(dsplit))
        print(dsplit[-1])
    else:
        filename=d
        print('not dir--'+filename)
'''

for file in os.listdir(rootdir):
    dr=os.path.join(rootdir,"Python")
    
    print(file)

