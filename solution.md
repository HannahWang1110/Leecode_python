### leetcode 刷题

#### 1. 数据结构

- stack

  - 20

  - 144（binary tree）：

    https://www.jianshu.com/p/bf73c8d50dc2

    存储方式：1. 顺序存储（从上至下，从左至右） 2. 二叉链表存储（避免非完全树按照顺序存储浪费存储空间）

    遍历方式： 1. 前序遍历（preorder）节点第一次出现输出 2. 中序遍历 节点第二次出现输出 3. 后序遍历 节点第三次出现输出 4.  层次遍历 从上至下一层一层从左至右输出节点

    continue v.s. break：break 跳出整个循环体，继续执行循环体之后的内容；continue 单纯不执行当次循环中剩余部分并进入下一次循环

  - 150:

     明确truncate toward zero的意思。`//`取整，`%`求余，在正数的应用中没有问题，在存在除数/被除数一方为负的情况下（且除不尽有余数），会发现`//`的取整运算需要`+1`以保证toward zero。

  - 42:

    进栈过程是append的过程，出栈过程是pop的过程

    创建相同元素的list可用 `a = [1] * 10`, list的逆序输出为`a[::-1]`

- Queue 

  - 347:

    使用`counter = collections.Counter([list])`来对list中元素出现次数进行计数。使用`most = counter.most_common(k)`来对前 $k$ 个（按照value从大到小进行排列的字典）进行输出，代替自己使用有序字典。

  - 102:

    二叉树的层次排序。当需要一个list先进先出，并指保持当前的一部分时，用对list赋值代替append和remove。对一个循环中的list（循环该list内容），在循环体中不要进行增删如append（会死循环）、remove（会跳着删除）。对于`[i for i in list for j in i if i]`这一类的`[]`中循环多个`for`和`if`叠加使用是可行的。

  - 279:

    拉格朗日四平方定理，即任何一个正整数都可表示为不超过4个整数的平方之和；

    如果一个正整数只能由4个平方树之和进行表示，则他可写为$4^a(8b+7)$,其中$a$和$b$可为任意非负整数。

    如果一个正整数可整除4, 即 n%4 == 0​，k = n/4，则n和k可用同样多的整数的平方之和表示。 

    关于类似完全平方数类的问题（一个数里有多少个square的情况），可采用暴力破解的方式。比如，此题中当一个数可被两个整数的平方和表示的情况。

  




