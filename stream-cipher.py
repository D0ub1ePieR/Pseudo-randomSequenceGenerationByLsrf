from mlist import lfsr_jk
from info import get_info
from B_M import solve

def output(list):
    nflag=0
    sflag=0
    for element in list:
        print(element,end="")
        if sflag==7:
            print(" ",end="")
            sflag=0
            nflag=nflag+1
        else:
            sflag=sflag+1
        if nflag==8:
            print()
            nflag=0
    print()

def outpoly(result):
    print("线性综合解为: f(x)=1",end="")
    result[0]=int(result[0])%2
    for i in range(1,9):
        result[i]=int(result[i])%2
        if result[i]>0:
            if i==1:
                print("+x",end="")
            else:
                print("+x^",end="")
                print(i,end="")
    print("\n系数为:",list(reversed(result[:9])))

def main(): #主函数 总控程序
    #获取信息
    information=get_info()
    st_num=information.re_st_num()
    poly=information.re_poly()
    print()
    print("当前学号为: ",st_num)
    print("当前使用的本原多项式系数为: ",poly)

    #md5加密并载入lfsr中
    proc=lfsr_jk(st_num,poly)
    proc.run()
    print("当前md5的hash值为: ",proc.get_md5())
    print("当前输出测试序列长度: ",proc.get_total())
    print("当前list1序列为:"),output(proc.get_list1())
    print("list1一个周期的序列为:"),output(proc.get_list1()[:255])
    print("当前list2序列为:"),output(proc.get_list2())
    print("list2一个周期的序列为:"),output(proc.get_list2()[:255])
    print("当前qlist序列为:"),output(proc.get_qlist()[1:])

    #利用B-M算法求出m序列的线性综合解 得到所使用的本原多项式
    for i in range(512):
        if proc.get_list1()[i]==0:
            break
    re=solve(proc.get_list1()[i:i+16])
    #re=solve([0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0])
    re.figure_out()
    result=re.get_result()
    outpoly(result)
    
main()
    
