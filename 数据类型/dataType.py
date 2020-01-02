# 数据类型demo

# 列表list 【数组】 元素可以直接更改
list1 = ['Google', 12.1, 11];
list2 = ["newList", "ll", "ll", "mm"];
list1.index(11)
list1.append("liumiao");  # 追加
list1.insert(3, "LIUMIAO");  # 插入
list1.extend(list2);  # 将list插入
list1.remove("liumiao");  # 删除列表第一次出现数据
list1.pop(3);  # 默认删除最后一位
# list1.clear(); # 清空列表
# del list1[1]; # 关键字删除 【变量从内存中删除】
len(list2);
list2.count("ll");  # 统计
list2.sort(reverse=True);
list2.reverse();
for name in list1:
    print(name);
for i in range(len(list1)):
    print(list1[i]);

# 元祖Tuple 【list集合】 元素不能修改 【保证数据安全】
tuple1 = ('小明', 786, 2.23,);  # 只有一个时 +,
print("%s 年龄是 %d 身高是 %.2f" % tuple1);  # 应用场景
# list() tuple() 互相转换

# Dictionary字典 【map集合】 无序
dict1 = {"name" : "liumiao","age" : 18};
dict2 = {"newData": 0};
print(dict1["name"]);
dict1.update(dict2); # 合并字典
dict1.clear();
for key in dict1.keys():
    print(dict1[key]);

# 字符串
# len() count("字符串") index()
# 完整for循环  else 循环完执行

