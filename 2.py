name = "Влад"
surname = "Вірний"
age = 16
a = type(name)
b = type(surname)
c = type(age)
list1=[name, surname, age]
list2=[a, b, c]
list_string=[]
list_int=[]
print(list1, list2)

if a==str:
    list_string.append(a)
elif a==int:
    list_int.append(a)
if b==str:
    list_string.append(b)
elif b==int:
    list_int.append(b)
if c==str:
    list_string.append(c)
elif c==int:
    list_int.append(c)

print(list_string)
print(list_int)

if len(list_string) > len(list_int):
    print("Тип даних str переважає")
elif len(list_int) > len(list_string):
    print("Тип даних int переважає")