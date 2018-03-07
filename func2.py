import zerorpc

class hitung2(object):
    def kali(self,x,y):
        print "kali"
        return x*y

    def bagi(self,x,y):
        print "bagi"
        return x/y

s = zerorpc.Server(hitung2())
s.bind("tcp://0.0.0.0:4242")
s.run()