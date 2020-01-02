# 类基本定义
class People:
    # 定义基本属性   对象初始值 None
    name = '' ;
    age = 0 ;
    __weight = 0;
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n;
        self.age = a;
        self.__weight = w;

    def __del__(self):
        print("对象销毁前执行");

    def __str__(self):
        # 格式化代码
        return "格式化代码输出";

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age));

# 实例化类
p = People("张三",20,1);
p.speak();
print(p);

# 类的内置方法    __del__方法 对象销毁之前，自动调用

# 比较对象地址值  is     not is
