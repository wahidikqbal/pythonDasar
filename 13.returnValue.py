#fungsi dengan return value
def kuadrat(argument):
    total = argument**2
    print('nilai kuadrat dari',argument,'adalah',total)
    return total

a = kuadrat(3)
print(a)


print(10*'--')


#FUNSI DENGAN RETURN VALUE DAN MULTIPLE ARGUMENT
def tambah(a,b):
    total = a+b
    print(a, '+' ,b , '=', total)
    return total

def kali(a,b):
    total = a*b
    print(a, '*' ,b , '=', total)
    return total


#a = tambah(2,5)
b = kali(3,tambah(2,5))

print(b)