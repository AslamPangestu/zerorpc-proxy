import zerorpc

class hitung1(object):
    def tambah(self,x,y):
        print "tambah"
        return x+y

    def kurang(self,x,y):
        print "kurang"
        return x-y

s = zerorpc.Server(hitung1())
s.bind("tcp://0.0.0.0:4141")
s.run()