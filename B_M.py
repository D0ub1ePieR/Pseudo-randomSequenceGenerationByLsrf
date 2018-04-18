from F_x import func

class solve:
    def __init__(self,list):
        self.__list=list
        self.__result=[]
    def figure_out(self):
        """
        反解出线性综合解
        """
        a=[]        #序列an
        d=[]        #序列dn
        l=[]        #序列ln
        fx=[]       #序列函数fn(x)
        #初始化B-M算法中所有用到的序列
        for element in self.__list:
            a.append(element)
            d.append(0)
            l.append(0)
            fx.append(None)
        l.append(0)
        fx.append(None)
        #找到第一个an!=0
        for index in range(len(a)):
            if a[index]!=0:
                d[index]=1
                l[index+1]=index+1
                for i in range(1,index+1):
                    fx[i]=func([1])
                templist=[]
                templist.append(1)
                for i in range(1,index+1):
                    templist.append(0)
                templist.append(-1)
                fx[index+1]=func(templist)
                break
        #开始迭代
            #求dn
        for n in range(index+1,len(a)):
            for i in range(n+1):
                d[n]=d[n]+a[i]*fx[n].flist[n-i]
                d[n]=d[n]%2
                #print(n)
                #print(a[i],fx[n].flist[n-i])
            #求m
            for i in range(1,n+1):
                if l[n-i]<l[n]:
                    m=n-i
                    break
            #print(m)
            if d[n]!=0:
                #求f(n+1)x
                tlist=[]
                for i in range(16):
                    tlist.append(0)
                tlist[n-m]=1
                fx[n+1]=func.fx_add(fx[n],func.fx_multiply(func([d[n],]),func.fx_multiply(func([1/d[m],]),func.fx_multiply(func(tlist),fx[m]))))
                l[n+1]=max(l[n],n+1-l[n])
            else:
                fx[n+1]=func.fx_copy(fx[n])
                l[n+1]=l[n]
        self.__result=fx[16].flist
        #print("an序列为: ",a)
        #print("dn序列为: ",d[:16])
        #print("ln序列为: ",l[:16])
        
    def get_result(self):
        """
        得到所求得的线性综合解
        """
        return self.__result
