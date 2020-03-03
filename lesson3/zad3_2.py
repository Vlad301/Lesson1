name = input("Name: ")
surname = input("Surname: ")
date = input("Date: ")
city = input("City: ")
email = input("Email: ")
phone = input("Phone num: ")


def fam(name, surname, date, city, email, phone):
    return "  ".join([name, surname, date, city, email, phone])


print(fam(name, surname, date, city, email, phone))
