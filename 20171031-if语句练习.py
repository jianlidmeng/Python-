# 需求
# 定义一个整数变量记录年龄
# 判断是否满 18 岁 （>=）
# 如果满 18 岁，允许进网吧嗨皮

age=18
if age>=18:
  print("可以进入网吧！")
print("这句什么时候执行？")

# if else

age=18
if age>=18:
  print("可以进入网吧！")
else:
  print("未成年，不能进入。")
# 改进需求

# 输入用户年龄
# 判断是否满 18 岁 （>=）
# 如果满 18 岁，允许进网吧嗨皮
# 如果未满 18 岁，提示回家写作业

age=int(input("输入用户年龄："))
if age>=18:
  print("允许进入网吧")
else:
  print("回家写作业吧")
print("文明上网")

# 逻辑运算 and or not

# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确。要求人的年龄在 0-120 之间
age=100
if age>=0 and age<=120:
  print("正确")
else：
  print("不正确")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩要求只要有一门成绩 > 60 分就算合格
python_score=46
c_score=88
if python_score>60 or c_scroe>60:
  print("成绩合格")
else:
  print("成绩不合格")

# 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工，如果不是提示不允许入内

is_employee=true
if not is_employee:
  print("非公入内")

# elif

# 需求
# 定义 holiday_name 字符串变量记录节日名称
# 如果是 情人节 应该 买玫瑰／看电影
# 如果是 平安夜 应该 买苹果／吃大餐
# 如果是 生日 应该 买蛋糕
# 其他的日子每天都是节日啊……

holiday_name="平安夜"
# holiday_name=input（"平安夜"）
if holiday_name=="情人节"：
  print("买玫瑰")
  print("看电影")
elif holiday_name=="平安夜"：
  print("买苹果")
  print("吃大餐")
elif holiday_name=="生日"：
  print("买蛋糕")
else：
  print("每一天都是过节啊")

# 火车站安检 需求

# 定义布尔型变量 has_ticket 表示是否有车票
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 首先检查是否有车票，如果有，才允许进行 安检
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 如果超过 20 厘米，提示刀的长度，不允许上车
# 如果不超过 20 厘米，安检通过
# 如果没有车票，不允许进门

has_ticket=True
knife_length=43
if has_ticket:
  print("可以检票")
  if knife_length>20:
    print("不允许携带%d厘米的刀上车"% knife_length)
else：
  print("通过安检")
else：
  print("请先买票")

# 石头剪刀布 需求

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 比较胜负
player=int(input("请出拳 石头（1）/剪刀（2）/布（3）："))

#假设电脑只能出石头
computer=1
if ((player==1 and computer==2)or
 (player==2 and computer==3)or
 (player==3 and computer==1)):
  print("你赢了")
elif player==computer:
  print("平手")
else：
  print("再来")
# 随机数  import random  导入随机数模块
# random.randint(1,3)

# 升级版
player=int(input("请出拳 石头（1）/剪刀（2）/布（3）："))

#电脑随机出
computer=random.randint(1,3)
if ((player==1 and computer==2)or
 (player==2 and computer==3)or
 (player==3 and computer==1)):
  print("你赢了")
elif player==computer:
  print("平手")
else：
  print("再来")









