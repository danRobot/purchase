import requests

user1={ "id": 1, "identification": "123456", "name": "alan brito", "address": "CR 34-45", "cellPhone": "311222222", "email": "alanbrito@gmail.com", "password": "Demo123.", "zone": "ZONA 1", "type": "COORD"}
get=requests.post("http://localhost:8080/api/user/new",json=user1)
print(get.json())