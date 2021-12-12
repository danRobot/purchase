import requests
#from requests.api import options

ip={'l':"localhost",'s':'155.248.209.25'}

op=input("local?")

if(op=='y'):
    option='l'
else:
    option='s'

hostUser="http://"+ip[option]+":8080/api/user/all"
hostClothe="http://"+ip[option]+":8080/api/clothe/all"
get=requests.delete(hostUser)
print(get.status_code)
user1={ "id": 1, "identification": "123123", "name": "CARLOS ALBERTO GARCIA", "address": "CR 34-45", "cellPhone": "311222222", "email": "cgarcia@gmail.com", "password": "Demo123.", "zone": "ZONA 2", "type": "ADM" }
get=requests.post(hostUser,json=user1)
print("TEST POST",get.json()=={'id': 1, 'identification': '123123', 'name': 'CARLOS ALBERTO GARCIA', 'address': 'CR 34-45', 'cellPhone': '311222222', 'email': 'cgarcia@gmail.com', 'password': 'Demo123.', 'zone': 'ZONA 2', 'type': 'ADM'})


user1={
"id": 1,
"identification": "123123",
"name": "ALBERTO GARCIA",
"address": "CR 90-25",
"cellPhone": "2222222",
"email": "agarcia@gmail.com",
"password": "Agarcia",
"zone": "ZONA 1",
"type": "ADM"
}
get=requests.put(hostUser,json=user1)
result=get.json()=={'id': 1, 'identification': '123123', 'name': 'ALBERTO GARCIA', 'address': 'CR 90-25', 'cellPhone': '2222222', 'email': 'agarcia@gmail.com', 'password': 'Agarcia', 'zone': 'ZONA 1', 'type': 'ADM'}
print("TEST PUT",result)
if(result==False):
    print(get.json())

get=requests.delete(hostClothe)
print(get.status_code)
user1={
"reference": "AP-903",
"category": "TSHIRT",
"size": "M",
"description": "SPORT TSHIRT",
"availability": True,
"price": 350000,
"quantity": 20,
"photography": "www.catalog.com/spiderman.png"
}
get=requests.post(hostClothe,json=user1)
result=get.json()=={'reference': 'AP-903', 'category': 'TSHIRT', 'size': 'M', 'description': 'SPORT TSHIRT', 'availability': True, 'price': 350000.0, 'quantity': 20, 'photography': 'www.catalog.com/spiderman.png'}
print("TEST POST",result)
if(result==False):
    print(get.json())

user1={
"reference": "AP-903",
"category": "BELT",
"material": "LEATHER",
"description": " LEATHER BELT FOR MAN",
"availability": True,
"price": 350000,
"quantity": 20,
"photography": "www.catalog.com/belt11.png"
}
get=requests.put(hostClothe,json=user1)
result=get.json()=={'reference': 'AP-903', 'category': 'BELT', 'size': 'M', 'description': ' LEATHER BELT FOR MAN', 'availability': True, 'price': 350000.0, 'quantity': 20, 'photography': 'www.catalog.com/belt11.png'}
print("TEST PUT",result)
if(result==False):
    print(get.json())
    print({'reference': 'AP-903', 'category': 'BELT', 'size': 'M', 'description': ' LEATHER BELT FOR MAN', 'availability': True, 'price': 350000.0, 'quantity': 20, 'photography': 'www.catalog.com/belt11.png'})

get=requests.delete(hostUser)
print(get.status_code)
get=requests.delete(hostClothe)
print(get.status_code)

get=requests.get(hostUser)
print(get.content)
get=requests.get(hostClothe)
print(get.content)