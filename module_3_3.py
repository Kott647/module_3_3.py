#Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, c)
    print()

print_params()
print_params(b = 25) # yes
print_params(c = [1,2,3]) #yes

#Распаковка параметров:

values_list = [1, "text", False]
values_dict = {"a":1, "b":'строка', "c":True}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:

values_list_2 = [54.32, "Строка" ]
print_params(*values_list_2, 42)