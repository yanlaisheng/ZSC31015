a, b = 0, 1
while a < 1000: # 输出不大于1000 的序列
    print(a, end=',')
    a, b = b, a + b
