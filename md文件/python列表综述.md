# "列表(list)"综述

## 一、**列表基本知识**

(1)用【】将需要放入列表中的元素包裹起来。

(2)列表可以容纳不同类型的数据。

(3)列表中每个元素要用逗号(",")隔开。

(4)列表可以被命名。

`list=[1,2,3,4,5,"whx"]`

(5)如要访问列表中某一个元素，使用下标索引。

访问列表第一个元素

`list[0]`

访问列表最后一个元素

`list[-1]`

访问列表倒数第二个元素

`list[-2]`

![图1.1](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE1.1.png?raw=true)

## 二、**列表切片**

(1)列表的切片功能可以获取某个范围内的全部元素。格式为 list[i:j:k] 其中i是起始索引，j是结束索引（包含i而不包含j），k为间隔。

(2)如果从头开始获取元素，到第n个元素为止，可使用代码

`list[:n-1]`

如果从第n个元素开始获取元素，可使用代码

`list[n-1:]`

获取全部元素，可使用代码

`list[:]`

按间隔为3获取元素，可使用代码

`list[::3]`

![图2.1](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE2.1.png?raw=true)

## 三、**列表的增、删、改、查**

### **1.增**

(1)列表可使用append()、extend()两种方法随时往列表最后位置添加数据

extend()方法的参数必须是一个可迭代对象，新的内容追加到原列表最后一个元素后面

append()方法的参数不需要可迭代对象，但每次只能增加一个元素

```
heroes=["美国队长","钢铁侠"]
heroes.extend(["雷神","鹰眼"])
heroes
```

![图3.11](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.1.png?raw=true)

(2)使用insert(i,j)方法往列表任意位置添加数据,i表示插入位置的下标，j表示插入的元素

```
s=[1,2,4,5]
s.insert(2,3)
s
```

![图3.12](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.12.png?raw=true)

### **2.删**

(1)使用remove()方法将指定的元素删除

```
heroes.remove("钢铁侠")
heroes
```

![图3.21](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.21.png?raw=true)

(2)如果列表中存在多个匹配的元素，则只会删除第一个元素

如果指定的元素不存在，程序会报错

(3)如果要删除某一位置的元素，使用pop()方法，()内为元素下标

```
heroes.pop(2)
heroes
```

![图3.23](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.23.png?raw=true)

(4)如果要删除列表中全部元素，使用clear()

```
heroes.clear()
heroes
```

![图3.23](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.24.png?raw=true)

### **3.改**

列表是可变的，而字符串是不可变的

(1)使用下标索引的方法，用赋值运算符将新的元素替换进列表中

```
nums=[1,2,3,4,5,6]
nums[3:]=[3,2,1]    #将4，5，6替换为3，2，1
nums
```

![图3.31](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.31.png?raw=true)

### **4.查**

(1)查找列表中某一元素值共有几个，使用count()方法

```
nums=[1,2,3,3,3,4,5]
nums.count(3)
```

(2)查找列表中某个元素的索引值，使用index()方法
如果有多个元素值一样，则只返回第一个找到的下标值

```
nums=[1,2,3,3,3,4,5]
nums.index(3)
```

![图3.4](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE3.4.png?raw=true)

## 四、**列表的加法和乘法**

(1)要求列表加号两边都是列表才可以相加

```
s=[1,2,3]
t=[4,5,6]
s+t
s*3
```

![图4.1](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE4.1.png?raw=true)

## 五、**嵌套列表**

`matrix=[[1,2,3],[4,5,6],[7,8,9]]`

要访问嵌套列表，使用matrix[i][j]方法，i是索引的行，j是索引的列

```
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix[1][1]
```

![图5.1](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE5.1.png?raw=true)

## 六、**列表拷贝**

### 1.**浅拷贝**

(1)copy对象拷贝的是整个列表对象，不仅仅是变量的引用

```
x=[1,2,3]
y=x.copy()
x[1]=1
x
y
```

![图6.11](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE6.11.png?raw=true)

(2)如果是嵌套列表，浅拷贝只能拷贝外层的对象，对于嵌套对象只能拷贝其引用

```
x=[[1,2,3],[4,5,6],[7,8,9]]
y=x.copy()
x[1][1]=0
x
y
```

![图6.12](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE6.12.png?raw=true)

### 2.**深拷贝**

(1)使用深拷贝要使用copy模块，包含浅拷贝和深拷贝

(2)浅拷贝仍然使用copy()方法  y=copy.copy(x)

(3)深拷贝使用deepcopy()方法，y=copy.deepcopy(x)

```
import copy
x=[[1,2,3],[4,5,6],[7,8,9]]
y=copy.copy(x)
x[1][1]=0
x
y
```

![图6.21](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE6.21.png?raw=true)

```
import copy
x=[[1,2,3],[4,5,6],[7,8,9]]
y=copy.deepcopy(x)
x[1][1]=0
x
y
```

![图6.22](https://github.com/Aireloli/picture/blob/main/%E5%88%97%E8%A1%A8md/%E5%9B%BE6.22.png?raw=true)

(4)对于深拷贝，是对所有引用的子对象一并进行拷贝


# **列表与数组的异同**

(1)列表是以方括号“[]”包围的数据集合，不同成员以“，”分隔

数组是以圆括号“()”包围的数据集合,括号（）可以省略，不同元素以逗号“,”分隔

(2)列表是可变的数据类型【可进行增删改查】，列表中可以包含任何数据类型，也可以包含另一个列表

数组是不可变序列，即数组一旦创建，数组中的数据一旦确立就不能改变，不能对数组中的元素进行增删改操作，因此数组没有增加元素append、修改元素、删除元素pop的相关方法

(3)列表可以通过下标索引访问列表中元素，序号从0开始

数组只能通过下标索引访问数组中的元素,序号从0开始
