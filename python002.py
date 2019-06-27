
#华氏温度与摄氏温度转换
C=input("请输入摄氏温度(数字):")
f=((int(C)*9)/5)+32
F = str(f)+"F"
print("华氏温度:%s"%F)

#输入圆的半径计算周长和面积
r=int(input("请输入圆的半径（m）:"))
L1=2*3.14*r
L=str(L1)+"m"

s=3.14*r**2
S=str(s)+"m²"
print("圆的周长为：%s"%L)
print("圆的面积为：%s"%S)

#判断年份是否为闰年
T=int(input("请输入年份（数字）:"))
y=T%4
if y==0:
    print("您输入的年份为闰年")
else:
    print("您输入的年份为平年")



