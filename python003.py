###狗的年龄计算判断：

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
	print("你是在逗我吧!")
elif age == 1:
	print("相当于 14 岁的人。")
elif age == 2:
	print("相当于 22 岁的人。")
elif age > 2:
	human = 22 + (age -2)*5
	print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")


###数字是否可以整除2或3
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

###计算1到100的和
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))


for letter in 'Running':
   if letter == 'g':
      break
   print ('当前字母为 :', letter)

for letter in 'Running':
   if letter == 'i':        # 字母为 i 时跳过输出
      continue
   print ('当前字母 :', letter)




#斐波纳契数列
# 两个元素的总和确定了下一个数
print('斐波纳契数列')
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

#输出水仙花数
#取数字的个位，十位，百位，千位：n/1%10,n/10%10,n/100%10,n/1000%10
print('100-999之间的水仙花数有：')
for i in range(100,999):
    p= int(i/1%10)  #取个位
    q= int(i/10%10)  #取十位
    m= int(i/100%10)   # 取百位

    if i==(p**3+q**3+m**3):
        print(i)


##输出1000以内的完美数（如果一个数恰好等于他的因子之和，则称完美数）
print('1000以内的完美数有：')
for j in range(1,1000):
    s=0
    for k in range(1,j):
        if j%k ==0:
            s=s+k
    if j==s:
        print(j)



