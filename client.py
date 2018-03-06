#ini client rpc
import zerorpc

c1 = zerorpc.Client()
c2 = zerorpc.Client()
#masukkan ip target
c1.connect("tcp://192.168.3.142:4242")
#masukkan ip target
c2.connect("tcp://192.168.3.142:8484")

a = input ('Masukkan nilai x = ')
b = input ('Masukkan nilai y = ')

print "Pilih operasi yang akan digunakan[1-4] : "
print "1. Tambah"
print "2. Kurang"
print "3. Kali"
print "4. Bagi"
menu = input('Menu yang dipilih : ')
if(menu == 1):
    print c1.tambah(a,b)
elif(menu == 2):
    print c1.kurang(a,b)
elif(menu == 3):
    print c2.kali(a,b)
elif(menu == 4):
    print c2.bagi(a,b)