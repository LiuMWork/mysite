# 类继承
class Father:
    name = '';
    age = 0;

    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def __str__(self):
        print("格式化代码输出");

    def speak(self):
        print("%s说: 我 %d 岁。" % (self.name, self.age))

# 子类继承
class Son(Father):
    teacherName = '';

    def __init__(self, name, age, teacherName):
        self.teacherName = teacherName;
        Father.__init__(self, name, age);

    @staticmethod
    def play():# 方法名不能相同，否则后面覆盖前面
        print("我是一个静态方法");

    @classmethod
    def song(cls):
        print("我是类方法", cls);

    def speak(self):
        print("%s说: 我 %d 岁了，老师是%s " % (self.name, self.age, self.teacherName));

# 继承具有传递性 【多重继承】
s = Son("小明",12,"大明老师");
s.speak();

# 调用父类方法
m = Son("小红",12,"小红老师");
super(Son,m).speak();

# 静态方法 类方法
Son.song();
Son.play();

# 多继承* 类名(,,……)

# 多态 向上造型 【父形引用指向子类对象】
