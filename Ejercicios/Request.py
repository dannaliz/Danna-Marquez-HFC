import requests

x = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(x.text)
y = x.json()
print("title: " + y["title"] + "\n" + "body: " + y["body"])

a = requests.post('https://jsonplaceholder.typicode.com/posts' , data = {"title": "Holi, este es el titulo", "body": "Holi, este es el cuerpo", "userid":"29122003"})
print(a.status_code)

b = requests.post('https://jsonplaceholder.typicode.com/users', {"title": "Danna", "body": "Holi, este es el cuerpo 2", "userid":"abcde"})
print(b.status_code)

# Me quede en el ultimo unu
c = requests.post('https://regres.in')