import requests
from pprint import pprint
#from requests.api import options

ip={'l':"localhost",'s':'155.248.209.25'}

op=input("local?")

if(op=='y'):
    option='l'
else:
    option='s'

hostUser="http://"+ip[option]+":8080/api/user"
hostClothe="http://"+ip[option]+":8080/api/clothe"
hostOrder="http://"+ip[option]+":8080/api/order"

get=requests.delete(hostUser+'/all')
get=requests.delete(hostClothe+'/all')

get=requests.get(hostUser+'/all')
print(get.content.decode())
get=requests.get(hostClothe+'/all')
print(get.content.decode())

test={
"id": 3,
"identification": "46669989",
"name": "BLODY MARRY",
"birthtDay": "1996-11-15T05:00:00.000+00:00",
"monthBirthtDay": "11",
"address": "CR 34-45",
"cellPhone": "3174565625",
"email": "stellez@gmail.com",
"password": "Demo123.",
"zone": "ZONA 2",
"type": "ASE"
}
expected=[{'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}]
get=requests.post(hostUser+"/new",json=test)
get=requests.get(hostUser+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 1 PASS")
else:
    print(result)

test={
"id": 6,
"identification": "213456789",
"name": "PEDRO CAPAROSA",
"birthtDay": "1966-02-15T05:00:00.000+00:00",
"monthBirthtDay": "02",
"address": "CR 34-45",
"cellPhone": "3168965645",
"email": "pcaparosa@gmail.com",
"password": "Demo123.",
"zone": "ZONA 1",
"type": "ASE"
}
expected=[{'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}, {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}]
get=requests.post(hostUser+"/new",json=test)
get=requests.get(hostUser+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 2 PASS")
else:
    print(result)

test={
"reference": "AP-903",
"category": "CATEGORIA 1",
"size": "M",
"description": "DESCRIPCION 1",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg"
}
expected=[{'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}]
get=requests.post(hostClothe+"/new",json=test)
get=requests.get(hostClothe+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 3 PASS")
else:
    print(result)

test={
"reference": "AP-904",
"category": "CATEGORIA 2",
"size": "S",
"description": "DESCRIPCION 2",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-007.jpg"
}
expected=[{'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}, {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}]
get=requests.post(hostClothe+"/new",json=test)
get=requests.get(hostClothe+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 4 PASS")
else:
    print(result)

get=requests.get(hostUser+"/3")
expected={'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}
result=get.json()
if(result==expected):
    print("TEST GET 1 PASS")
else:
    print(result)

test={
"id": 1,
"registerDay": "2021-09-15T05:00:00.000+00:00",
"status": "Pendiente",
"salesMan": {
"id": 3,
"identification": "46669989",
"name": "BLODY MARRY",
"birthtDay": "1996-11-15T05:00:00.000+00:00",
"monthBirthtDay": "11",
"address": "CR 34-45",
"cellPhone": "3174565625",
"email": "stellez@gmail.com",
"password": "Demo123.",
"zone": "ZONA 2",
"type": "ASE"
},
"products": {
"AP-904": {
"reference": "AP-904",
"category": "CATEGORIA 2",
"size": "S",
"description": "DESCRIPCION 2",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-007.jpg"
},
"AP-903": {
"reference": "AP-903",
"category": "CATEGORIA 1",
"size": "M",
"description": "DESCRIPCION 1",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg"
}
},
"quantities": {
"AP-904": 1,
"AP-903": 1
}
}
expected=[{'id': 1, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}]
get=requests.post(hostOrder+"/new",json=test)
get=requests.get(hostOrder+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 5 PASS")
else:
    pprint(result)
    pprint(expected)


test={
"id": 2,
"registerDay": "2021-09-15T05:00:00.000+00:00",
"status": "Pendiente",
"salesMan": {
"id": 6,
"identification": "213456789",
"name": "PEDRO CAPAROSA",
"birthtDay": "1966-02-15T05:00:00.000+00:00",
"monthBirthtDay": "02",
"address": "CR 34-45",
"cellPhone": "3168965645",
"email": "pcaparosa@gmail.com",
"password": "Demo123.",
"zone": "ZONA 1",
"type": "ASE"
},
"products": {
"AP-904": {
"reference": "AP-904",
"category": "CATEGORIA 2",
"size": "S",
"description": "DESCRIPCION 2",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-007.jpg"
},
"AP-903": {
"reference": "AP-903",
"category": "CATEGORIA 1",
"size": "M",
"description": "DESCRIPCION 1",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg"
}
},
"quantities": {
"AP-904": 1,
"AP-903": 1
}
}
expected=[{'id': 1, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}, {'id': 2, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}]
get=requests.post(hostOrder+"/new",json=test)
get=requests.get(hostOrder+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 6 PASS")
else:
    print(result)


test={
"id": 3,
"registerDay": "2021-11-15T05:00:00.000+00:00",
"status": "Pendiente",
"salesMan": {
"id": 6,
"identification": "213456789",
"name": "PEDRO CAPAROSA",
"birthtDay": "1966-02-15T05:00:00.000+00:00",
"monthBirthtDay": "02",
"address": "CR 34-45",
"cellPhone": "3168965645",
"email": "pcaparosa@gmail.com",
"password": "Demo123.",
"zone": "ZONA 1",
"type": "ASE"
},
"products": {
"AP-904": {
"reference": "AP-904",
"category": "CATEGORIA 2",
"size": "S",
"description": "DESCRIPCION 2",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-007.jpg"
},
"AP-903": {
"reference": "AP-903",
"category": "CATEGORIA 1",
"size": "M",
"description": "DESCRIPCION 1",
"availability": True,
"price": 150000,
"quantity": 10,
"photography": "https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg"
}
},
"quantities": {
"AP-904": 1,
"AP-903": 1
}
}
expected=[{'id': 1, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}, {'id': 2, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}, {'id': 3, 'registerDay': '2021-11-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}]
get=requests.post(hostOrder+"/new",json=test)
get=requests.get(hostOrder+"/all")
result=get.json()
if(result==expected):
    print("TEST POST 7 PASS")
else:
    print(result)

get=requests.get(hostOrder+"/zona/ZONA 1")
expected=[{'id': 2, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}, {'id': 3, 'registerDay': '2021-11-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 6, 'identification': '213456789', 'name': 'PEDRO CAPAROSA', 'birthtDay': '1966-02-15T05:00:00.000+00:00', 'monthBirthtDay': '02', 'address': 'CR 34-45', 'cellPhone': '3168965645', 'email': 'pcaparosa@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 1', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}]
result=get.json()
if(result==expected):
    print("TEST GET 2 PASS")
else:
    print("CUSTOM MAL")
    pprint(result)
    pprint(expected)

get=requests.get(hostOrder+"/1")
expected={'id': 1, 'registerDay': '2021-09-15T05:00:00.000+00:00', 'status': 'Pendiente', 'salesMan': {'id': 3, 'identification': '46669989', 'name': 'BLODY MARRY', 'birthtDay': '1996-11-15T05:00:00.000+00:00', 'monthBirthtDay': '11', 'address': 'CR 34-45', 'cellPhone': '3174565625', 'email': 'stellez@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ASE'}, 'products': {'AP-904': {'reference': 'AP-904', 'category': 'CATEGORIA 2', 'size': 'S', 'description': 'DESCRIPCION 2', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-007.jpg'}, 'AP-903': {'reference': 'AP-903', 'category': 'CATEGORIA 1', 'size': 'M', 'description': 'DESCRIPCION 1', 'availability': True, 'price': 150000.0, 'quantity': 10, 'photography': 'https://www.avasoluciones.com/uploads/2021/09/910-006127.jpg'}}, 'quantities': {'AP-904': 1, 'AP-903': 1}}
result=get.json()
if(result==expected):
    print("TEST GET 3 PASS")
else:
    print(result)


get=requests.delete(hostUser+'/all')
print(get.status_code)
get=requests.delete(hostClothe+'/all')
print(get.status_code)
get=requests.delete(hostOrder+'/all')
print(get.status_code)

get=requests.get(hostUser+'/all')
print(get.content.decode())
get=requests.get(hostClothe+'/all')
print(get.content.decode())
get=requests.get(hostOrder+'/all')
print(get.content.decode())