contacts = {
    "number": 4,
    "students": [
        {"name": "S H", "email": "sh@gmail.com"},
        {"name": "A H", "email": "ah@gmail.com"},
        {"name": "B H", "email": "bh@gmail.com"},
        {"name": "C H", "email": "ch@gmail.com"},
        {"name": "D H", "email": "dh@gmail.com"},
    ],
}

for student in contacts["students"]:
    print(student["email"])
