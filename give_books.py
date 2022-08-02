import json
import csv
from csv import DictReader

with open("users.json", "r") as f:
    users_list = json.load(f)

users = []
for user in users_list:
    user_name = user.get('name')
    user_gender = user.get('gender')
    user_address = user.get('address')
    user_age = user.get('age')

    users.append({'name': user_name, 'gender': user_gender, 'address': user_address, 'age': user_age, 'books': []})

with open('books.csv', 'r') as f:
    books_list = list(csv.DictReader(f))

for books in books_list:
    del books['Publisher']

while len(books_list) > 0:
    for user in users:
        if len(books_list) > 0:
            user['books'].append(books_list.pop())

with open("result.json", "w") as f:
    f.write(json.dumps(users, indent=4))

