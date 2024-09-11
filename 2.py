name = "Влад"
surname = "Вірний"
age = 16
list1=(name, surname, age)
list2=(type(name), type(surname), type(age))
print(list1, list2)
if type(name) == type(surname) and type(name) == type(age):
    print("Усі типи даних однакові - str")
elif type(name) == type(surname) != type(age):
    print("Дві з трьох змінних мають тип данних str")
else:
    print("Тип данних переважно int")
