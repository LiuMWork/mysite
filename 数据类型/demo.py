import random;
# 导包使用
var = random.randint(1,10);
# 循环 for in
# 函数定义
def mathPlay(num1,num2):
    """
    求两数之和
    @param num1:
    @param num2:
    @return:
    """
    return num1 + num2;

# print(mathPlay(1,2));
# 模块 【类】 导入模块

# 方法默认值  参数=默认值true 【必须在末尾】
def addNum(num1, num2, num3=1):
    """
    求三数之和 【有默认值】
    @param num1:
    @param num2:
    @param num3:
    @return:
    """
    return num1 + num2 + num3;
# print(addNum(1,2));

# 多值参数 * **

# 异常
try:
    print(5/0);
except Exception as error:
    print(error);
else:
    print("没有异常执行code");
finally:
    print("无论有无异常执行code");
print("之后代码");




