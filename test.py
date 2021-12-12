import requests


get=requests.delete("http://localhost:8080/api/user/all")
print(get.status_code)
user1={ "id": 1, "identification": "123123", "name": "CARLOS ALBERTO GARCIA", "address": "CR 34-45", "cellPhone": "311222222", "email": "cgarcia@gmail.com", "password": "Demo123.", "zone": "ZONA 2", "type": "ADM" }
get=requests.post("http://localhost:8080/api/user/all",json=user1)
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
get=requests.put("http://localhost:8080/api/user/all",json=user1)
result=get.json()=={'id': 1, 'identification': '123123', 'name': 'ALBERTO GARCIA', 'address': 'CR 90-25', 'cellPhone': '2222222', 'email': 'agarcia@gmail.com', 'password': 'Agarcia', 'zone': 'ZONA 1', 'type': 'ADM'}
print("TEST PUT",result)
if(result==False):
    print(get.json())

get=requests.delete("http://localhost:8080/api/clothe/all")
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
get=requests.post("http://localhost:8080/api/clothe/all",json=user1)
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
get=requests.put("http://localhost:8080/api/clothe/all",json=user1)
result=get.json()=={'reference': 'AP-903', 'category': 'BELT', 'size': 'M', 'description': ' LEATHER BELT FOR MAN', 'availability': True, 'price': 350000.0, 'quantity': 20, 'photography': 'www.catalog.com/belt11.png'}
print("TEST PUT",result)
if(result==False):
    print(get.json())
    print({'reference': 'AP-903', 'category': 'BELT', 'size': 'M', 'description': ' LEATHER BELT FOR MAN', 'availability': True, 'price': 350000.0, 'quantity': 20, 'photography': 'www.catalog.com/belt11.png'})