class newprops(object):
    def getage(self):
        return 40
    def setage(self,value):
        print('set agt:',value)
        self._age = value
    age = property(getage,setage,None,None)

