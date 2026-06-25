#赋值
a = 10
b = 10.0
c = "abcd"
d = a + b
e = {}
f = []
g = ()

#type（）：查看一个变量所指的对象类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#isinstance():判断一个对象是否是一个已知的类型
print(isinstance(a, int))
print(isinstance(b, int))