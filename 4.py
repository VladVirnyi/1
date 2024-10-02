# Створити функцію яка приймає список [3,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда'].
# Ця функція видаляє всі елементи які повторюються  та повертає список без повторень.
# створюєм функцію яка на вхід буде приймати наш список без повторень та сортувати його.

# Сортування відбувається від від найменшого до найбільшого якщо є типи данних типу стр їх в алфавітному порядку встановити після цифр в томуж самомому списку.

anaconda_list = [3,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']
right_list = []

def anaconda(anaconda_list):
    for chislo in anaconda_list:
        if chislo not in right_list:
            right_list.append(chislo)
    return right_list

result_anaconda = anaconda(anaconda_list)

def sort_anaconda(anaconda):
    num_list = []
    str_list = []
    for i in anaconda:
        if type(i) == int:
            num_list.append(i)
        elif type(i) == str:
            str_list.append(i)
    num_list.sort()
    str_list.sort()
    return num_list + str_list

result_anaconda = anaconda(anaconda_list)
sorted_anaconda = sort_anaconda(result_anaconda)


        
print(anaconda(anaconda_list))
print(sort_anaconda(result_anaconda))

