#DemoTupleDict.py
#Tuple
from __future__ import print_function


tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result)

args=(5,6)
print(calc(*args))

a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))

a={1,2,3}
b=list(a)
print(b)
print(type(b))
b.append(4)
print(b)

device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
print(type(device))
print(len(device))
print(device["아이폰"])

device["갤럭시폴더"]=15
device["아이폰"]=6
print(device)

del device["아이폰"]
print(device)

for item in device.items():
    print(item)