class get_info:
    def __init__(self):
        self.__polynomial=[[1,0,0,0,1,1,1,0,1],
                [1,0,0,1,0,1,0,1,1],
                [1,0,0,1,0,1,1,0,1],
                [1,0,1,0,0,1,1,0,1],
                [1,0,1,0,1,1,1,1,1],
                [1,0,1,1,0,0,0,1,1],
                [1,0,1,1,0,0,1,0,1],
                [1,0,1,1,0,1,0,0,1],
                [1,0,1,1,1,0,0,0,1],
                [1,1,0,0,0,0,1,1,1],
                [1,1,0,0,0,1,1,0,1],
                [1,1,0,1,0,1,0,0,1],
                [1,1,1,0,0,0,0,1,1],
                [1,1,1,0,0,1,1,1,1],
                [1,1,1,1,0,0,1,1,1],
                [1,1,1,1,1,0,1,0,1]]
        self.__get_st_num()
        self.__get_poly()
        
    def __get_st_num(self):
        """
        确定学号
        """
        choice=input("当前学号:161520322\n是否使用预设学号?(Y/N) ")
        while True:
            if choice.capitalize()=='N':
                self.__st_num=input("请输入你的学号? ")
                break
            elif choice.capitalize()=='Y':
                self.__st_num="161520322"
                break
            else:
                choice=input("输入有误!请重新输入:")

    def __get_poly(self):
        """
        确定使用的本原多项式
        """
        print("GF(8)中的本原多项式有:\n(格式为:f(x)=cnx^8+(cn-1)x^7...+c2x^2+c1x+1)")
        num=0
        for list in self.__polynomial:
            print(num,list)
            num=num+1
        flag=False
        while flag==False:
            try:
                choice=eval(input("请输入选择的本原多项式序号:"))
            except NameError:
                """
                用户输入了非数字
                """
                print("请输入一个数字!\n")
            except:
                print("Unexcepted Error Occured!\n")
            else:
                try:
                    self.__poly=self.__polynomial[choice]
                except IndexError:
                    """
                    用户输入的地址越界
                    """
                    print("请输入一个0-15的数字!\n")
                except:
                    print("Unexcepted Error Occured!\n")
                else:
                    flag=True

    def re_st_num(self):
        """
        返回学号
        """
        return self.__st_num
    def re_poly(self):
        """
        返回本原多项式系数
        """
        return self.__poly
