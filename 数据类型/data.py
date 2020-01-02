from 数据类型 import demo

print(demo.mathPlay(1, 2));
if False:
    print("可以执行");
else:
    print("不可执行");

# 等待用户输出
# input("\n\n按下 enter 键后退出。")

# 不换行输出
print("张三", end=" ");
print("李四");

# \n换行   加r当作普通字符
print("我是\n小明");
print(r"我是\n小明");

print("========数据类型========");
# 数据类型
x, y, z = 1, 2, 3;
a, b, c, d = 20, 5.5, True, 4 + 3j;
print(x, y, z);
print(type(a), type(b), type(c), type(d));
print(isinstance(a, int));  # 认为子类是父类

print("========字符串========");
str = "zhangsan";
print(str);
print(str[0:-1]);  # 0开始  -1开始
print(str[0]);
print(str[1:]);
print(str + "你好");

print("========List列表========");
# list值可以直接更改
list = ['abcd', 786, 2.23, 'runoob', 70.2];
tinylist = [123, 'runoob'];
print(list);
print(list[0]);
print(list[1:5:3]);  # 最后一个表示长度
print(list[2:]);
print(tinylist * 2);  # 输出两次
print(list + tinylist);  # 连接列表

print("========Tuple元组========");
#    元祖元素不能修改
t = ('abcd', 786, 2.23, 'runoob', 70.2);

print("========Set集合========");  # 有序 无重复
s = {'abcd', 786, 2.23, 'runoob', 70.2};
set();  # 创建空集合时必须set()
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'};
print(student);  # 自动去重
if 'Tom' in student :  # 成员测试
    print("Tom存在");
else:
    print("Tom不存在");
# set集合运算 交集,并集等
a = set('abracadabra');
b = set('alacazam');
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

print("========Dictionary字典========");  # 无序 【map】
dict = {};
dict['one'] = "一号字典";
dict[2] = "二号字典";
dict2 = {"name" : "liumiao","age" : 18};
print(dict["one"]);
print(dict[2]);
print(dict2);
print(dict2.keys());
print(dict2.values());


