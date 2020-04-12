**易错点总结**  
1.for循环后记得打“：”，因为Python不需要用花括号，所以经常容易忘记  

2.有关print函数  
其中，在print（）中添加end=''可以保证下一个print不用换行  
如
```
    for i in range(3):
        print('*', end='')
```
输出结果为：  
```
***
```

3.遇到的作业难点  
输出如下三角形图形：  
经过参考后得到答案：  
```
row = int(input('lines number '))
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print('\n')
```
