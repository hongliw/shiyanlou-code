# 默认值只被赋值一次
def func1(a, data=[]):
    data.append(a)
    return data

def func2(a, data=None):
    if data is None:
        data = []
    data.append(a)
    return data 
    
if __name__ == '__main__':
    print('---------------func1()------------------')
    print(func1(1))
    print(func1(2))
    print(func1(3))
    print('---------------func2()-------------------')
    print(func2(1))
    print(func2(2))
    print(func2(3))

