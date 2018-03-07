#ini server rpc
import zerorpc

#export modul func
c1 = zerorpc.Client()
#export
c2 = zerorpc.Client()
#remote service akan stay di socket adress berapa dgn protokol apa
c1.connect("tcp://127.0.0.1:4141")
#remote service akan stay di socket adress berapa dgn protokol apa
c2.connect("tcp://127.0.0.1:4242")

class Hitung(object):
    def pilih_menu(self,a,b,menu):
        if (menu == 1):
            return c1.tambah(a,b)
        elif (menu == 2):
            return c1.kurang(a,b)
        elif (menu == 3):
            return c2.kali(a,b)
        elif (menu == 4):
            return c2.bagi(a,b)

#export
s = zerorpc.Server(Hitung())
#remote service akan stay di socket adress berapa dgn protokol apa
s.bind("tcp://0.0.0.0:4040")
#jalankan
s.run()
# gevent.joinall([gevent.spawn(s.run),gevent.spawn(c1.connect),gevent.spawn(c2.connect)])