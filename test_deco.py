class a:
    def deco(func):
        def wrapper(self):
            print(func.__name__, '함수 시작')
            func(self)
            print(func.__name__, '함수 끝')
        return wrapper   
    
    @deco
    def func(self):
        print("hi")

obj=a()
obj.func()