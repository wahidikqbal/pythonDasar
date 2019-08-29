Data = [1,2,5,776,7,76,23]
Subdata = Data[0]

print(Subdata)


#menggabungkan array
Data1 = [1,4,5,7,4,8]
Data2 = [43,21,54,12,64]
Data3 = Data1 + Data2
print(Data3)

#mengganti data
Data3[1] = 100
print(Data3)

#list dalam 
Data4 = [1,2,3,4,5]
Data5 = [6,7,8,91,10]

x = [Data4,Data5]
print(x)
#akses list dalam multidimensional list
y = x[0][3]
print(y)

#menambahkan data
Data6 = [10,11,12,13]
Data6.append(14)
print(Data6)

#menghitung panjang data
panjangData = len(Data6)
print(panjangData)