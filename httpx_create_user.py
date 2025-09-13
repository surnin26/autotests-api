import httpx

from tools.fakers import get_random_email

playload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=playload)

print(response.status_code)
print(response.json())