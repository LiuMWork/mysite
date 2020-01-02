# 变量引用 内存指向
# 局部变量 全局变量 【修改 gl】
g_num = 10;
def methonA():
    # global g_num;
    g_num = 99; # 就近原则
    print(g_num);
def methonB():
    print(g_num);
methonA();
methonB();



