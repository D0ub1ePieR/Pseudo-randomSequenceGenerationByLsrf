# Pseudo-randomSequenceGenerationByLsrf
通过8位线性移位寄存器伪随机序列生成 
---Cryptography lab
# info
stream-cipher.py为主程序
info.py中获取需要运算的基本信息
mlist.py中将数据放入lsrf中并使用jk触发器处理首先得到255为周期的m序列随后得到无周期的伪随机序列
B_M.py中反解出所使用的本原多项式即它的线性综合解
F_X.py中处理B-M算法中所有fx中的x前面的系数

运行stream-cipher.py根据提示输入 可以得到对应学号以及本元表达式生成的序列以及反解出来得到原本原多项式
