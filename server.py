#ini server rpc
import zerorpc
import func1
import func2
import gevent

#export modul func
s1 = zerorpc.Server(func1)
#remote service akan stay di socket adress berapa dgn protokol apa
s1.bind("tcp://0.0.0.0:4242")

s2 = zerorpc.Server(func2)

s2.bind("tcp://0.0.0.0:8484")
#jalankan
gevent.joinall([gevent.spawn(s1.run),gevent.spawn(s2.run)])