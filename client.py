#ini client rpc
import zerorpc

c = zerorpc.Client()
#masukkan ip target
c.connect("tcp://10.107.208.40:4040")

a = eval(input ('Masukkan nilai x = '))
b = eval(input ('Masukkan nilai y = '))

print("Pilih operasi yang akan digunakan[1-4] : ")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
menu = eval(input('Menu yang dipilih : '))
print(c.pilih_menu(a,b,menu))
# if(menu == 1):
#     print c1.tambah(a,b)
# elif(menu == 2):
#     print c1.kurang(a,b)
# elif(menu == 3):
#     print c2.kali(a,b)
# elif(menu == 4):
#     print c2.bagi(a,b)