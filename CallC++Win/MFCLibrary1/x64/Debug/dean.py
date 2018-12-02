from ctypes import *

lib = cdll.LoadLibrary('MFCLibrary1.dll')

def calldll():

    lib.Hello()

    hello = lib.hello
    print(hello() , ": dean\n")

    add = lib.add
    add.argtypes = [c_double, c_double]
    add(1.0,634634.0)

    a = c_double()
    b = c_double()
    a.value = 12
    print(a, b)
    add(a,b)

    c = create_string_buffer(b'\000' * 32)
    print(repr(c.value))
    c.value = b"dean"
    print(repr(c.value))

    
    cov = lib.cov
    cov.restype = c_char_p
    print((cov(b"asljgioe")))

class DLL(object):
    def __init__(self):
        self.obj = lib.Hello_New()

    def pri(self):
        lib.Hello_print(self.obj)


class POINT(Structure):
    _fields_ = [("x", c_double),
              ("y", c_double)]

class RECT(Structure):
    _fields_ = [("upperleft", POINT),
              ("lowerright", POINT)]

def deal_struct():
    point = POINT(10.2, 34.5)
    print(point.x, point.y)
    
    rect = RECT(point, POINT(3, 5))
    print(rect.upperleft.x)
    
    
if __name__ == '__main__':
    calldll()
    f = DLL()
    f.pri()
    deal_struct()
