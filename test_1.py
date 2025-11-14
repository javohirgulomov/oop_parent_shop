students = {
    "998901111111": {
        "name": "Ali",
        "phone": "998901111111",
        "age": 12,
        "email": "Ali@gmail.com"
    },
    "998902222222": {
        "name": "Ahror",
        "phone": "998902222222",
        "age": 13,
        "email": "Ahror@gmail.com"
    },
    "998903333333": {
        "name": "Timur",
        "phone": "998903333333",
        "age": 14,
        "email": "Timur@gmail.com"
    }
}

import re

sss = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
email_check = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


def add_Student(d: dict):
    name = input("name:")

    while True:
        phone = input("phone:")
        if re.match(sss, phone):
            break
        else:
            print("Xato raqam kiritdingiz. Boshidan raqam kiriting")

    age = input("age:")
    while True:
        email = input("email:")
        if re.match(email_check, email):
            break
        else:
            print("Xato email kiritdingiz. Boshidan email kiriting")

    s = {
        "name": name,
        "phone": phone,
        "age": age,
        "email": email
    }
    d[phone] = s
    print("O‘quvchi muvaffaqiyatli qo‘shildi!")


def view_Student(d: dict):
    for k, v in d.items():
        print(f"id: {k} | name: {v['name']} | phone: {v['phone']} | age: {v['age']} | email: {v['email']}")

def student_manager(d: dict):
    while True:
        kod = input(" 1.View student \n 2.Add student \n 3.Break \n")
        if kod == "1":
            view_Student(d)
        elif kod == "2":
            add_Student(d)
        elif kod == "3":
            print("Dastur yakunlandi.")
            break
        else:
            print("Xato raqam")

student_manager(students)
