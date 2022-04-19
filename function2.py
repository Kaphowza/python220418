#function2.py
from os import times_result
from unittest import result


x=1
def func(a):
    return a+x

print (func(1))

def func2(a):
    x=2
    return a+x

print (func2(1))

def times(a=10,b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com","80"))
print(connectURI(port="80", server="credu.com"))

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAN", "EGG"))
print(union("HAM", "EGG", "SPAM"))

def userURIBulder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

print(userURIBulder("credu.com", "80", id="kim", passwd = "1234"))
print(userURIBulder("credu.com", "80", id="kim", passwd = "1234", name="mike"))

g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())