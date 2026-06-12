import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()  # parsing automatico del JSON
print(data)

# accesso ai campi
print(data["userId"])   # 1
print(data["id"])       # 1
print(data["title"])    # "sunt aut facere..."
print(data["body"])     # "quia et suscipit..."

# accesso sicuro (non lancia errore se il campo non esiste)
print(data.get("title"))        # "sunt aut facere..."
print(data.get("campo", "n/a")) # "n/a"

'''
#con parametrri
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}  # → ?userId=1
)
posts = response.json()
for post in posts:
    print(post["title"])
'''

'''
#post
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Hello", "body": "World", "userId": 1}
)
print(response.status_code)  # 201 Created
print(response.json())
'''