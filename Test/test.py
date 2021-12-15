import requests
import json
import ast
import argparse

def str2ent(string):
    if(len(string)==1):
        return ''
    try:
        obj=json.loads(string)
    except:
        obj=ast.literal_eval(string)
    return obj
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--host',help='sitio del backend',default="local")
parser.add_argument('--reto',help='numero del reto',default="3")
parser.add_argument('--limpiar',help='numero del reto',default="si")

args = parser.parse_args()

ip={'local':"localhost",'cloud':'155.248.209.25'}

host="http://"+ip[args.host]+":8080/"


reto='testR'+args.reto
cases=open("cases/"+reto+".txt").readlines()
options=json.load(open("options/"+reto+".json"))
cases=list(map(str2ent,cases))
import string

req={"GET":requests.get,"POST":requests.post,"PUT":requests.put,"DELETE":requests.delete}

for step in(string.ascii_letters):
    try:
        method=options[step]['method']
        endpoint=options[step]['endpoint']
        check=options[step]['check']
        send_data=cases.pop(0)
        expected=cases.pop(0)
        result=req[method](url=host+endpoint,json=send_data)
        if(method!="GET"):
            result=req["GET"](url=host+check)
        try:
            result=result.json()
            if(result==expected):
                print("TEST PASS")
            else:
                print(endpoint)
                print('DATA',result)
                print('expected',expected)
        except:
            print(result)
        #wait=input("siguiente?")
    except:
        pass

if(args.limpiar=="si"):
    get=requests.delete(host+'api/user/all')
    print(get.status_code)
    get=requests.delete(host+'api/clothe/all')
    print(get.status_code)
    get=requests.delete(host+'api/order/all')
    print(get.status_code)

    get=requests.get(host+'api/user/all')
    print(get.content.decode())
    get=requests.get(host+'api/clothe/all')
    print(get.content.decode())
    get=requests.get(host+'api/order/all')
    print(get.content.decode())