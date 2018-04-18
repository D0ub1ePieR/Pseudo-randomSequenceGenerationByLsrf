import hashlib

class lfsr_jk:
    def __init__(self,st_num,poly):
        self.__binmap={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
                        '8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
        self.__st_num=st_num
        self.__poly=poly
        self.__md5_hash=''
        self.__list1=[]     #使用md5加密后的后3-4位lfsr生成的序列
        self.__list2=[]     #使用md5加密后的后1-2位lfsr生成的序列
        self.__qlist=[]     #经过jk触发器处理后的序列
        self.__number=512   #生成的序列长度

    def __md5(self):
        self.__md5_hash=hashlib.md5(self.__st_num.encode('utf-8')).hexdigest()
        #print(md5)
        for i in [-4,-3]:
            for j in range(4):
                self.__list1.append(int(self.__binmap[self.__md5_hash[i]][j]))      #预存8bit初始状态至list1
        for i in [-2,-1]:
            for j in range(4):
                self.__list2.append(int(self.__binmap[self.__md5_hash[i]][j]))      #预存8bit初始状态至list2

    def __lfsr(self,list):
        for i in range(self.__number):
            tmp=0
            for j in range(8):
                tmp=tmp+self.__poly[j]*list[i+j]
                #print(poly[j],list1[i+j])
            tmp=tmp%2
            #print(tmp)
            list.append(tmp)
            
    def __check(self,num):
        """
        取反
        """
        if num==0:
            return 1
        else:
            return 0
        
    def __jk(self,list1,list2):
        """
        模拟jk触发器
        """
        self.__qlist.append(0)
        for i in range(self.__number):
            qn=list1[i]*self.__check(self.__qlist[i])+self.__check(list2[i])*self.__qlist[i]
            qn=qn%2
            self.__qlist.append(qn)

    def run(self):
        """
        运行
        """
        self.__md5()
        self.__lfsr(self.__list1)
        self.__lfsr(self.__list2)
        self.__jk(self.__list1,self.__list2)

    def get_md5(self):
        """
        返回md5的hash值
        """
        return self.__md5_hash
    def get_list1(self):
        """
        返回list1
        """
        return self.__list1
    def get_list2(self):
        """
        返回list2
        """
        return self.__list2
    def get_qlist(self):
        """
        返回qlist
        """
        return self.__qlist
    def get_total(self):
        """
        返回序列长度
        """
        return self.__number
