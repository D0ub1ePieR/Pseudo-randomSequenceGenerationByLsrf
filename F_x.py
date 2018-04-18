from copy import deepcopy

class func:
    def __init__(self,list):
        self.maxlen=16
        self.flist=[]
        for i in range(self.maxlen):
            if i<len(list):
                self.flist.append(list[i])
            else:
                self.flist.append(0)

    @classmethod
    def fx_add(cls,fx1,fx2):
        tlist=[]
        maxlen=16
        for i in range(maxlen):
            tlist.append(fx1.flist[i]+fx2.flist[i])
        return func(tlist)

    @classmethod
    def fx_multiply(cls,fx1,fx2):
        tlist=[]
        maxlen=16
        if fx1.flist[0]!=0:
            for i in range(maxlen):
                tlist.append(fx2.flist[i]*fx1.flist[0])
            return func(tlist)
        else:
            for i in range(1,maxlen):
                tlist=deepcopy(fx2.flist)
                if fx1.flist[i]!=0:
                    try:
                        for j in range(maxlen):
                            if tlist[maxlen-1-j]!=0:
                                tlist[maxlen-1-j+i]=tlist[maxlen-1-j]
                                tlist[maxlen-1-j]=0
                        for j in range(i):
                            tlist[j]=0
                    except IndexError:
                        print("Error Occured!\n")
                    except:
                        print("Unexcept Error Occured!\n")
                    break
        return func(tlist)

    @classmethod
    def fx_copy(cls,fx1):
        return func(fx1.flist)
    
    def get_flist(self):
        """
        获得自身函数系数序列
        """
        return self.flist
