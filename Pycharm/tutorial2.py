# closure.py
class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))  # 30 출력
    print(mul5.mul(10))  # 50 출력


# closure.py
class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력


def mul(m):
    def wrapper(n):
        return m * n
    return wrapper
import time


if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력


    def elapsed(original_func):  # 기존 함수를 인수로 받는다.
        def wrapper():
            start = time.time()
            result = original_func()  # 기존 함수를 수행한다.
            end = time.time()
            print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
            return result  # 기존 함수의 수행 결과를 리턴한다.

        return wrapper


    def myfunc():
        print("함수가 실행됩니다.")


    decorated_myfunc = elapsed(myfunc)
    decorated_myfunc()

import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간: %f 초" % (end-start))

myfunc()




class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        value = self.data[self.position]
        self.position += 1
        return value
    
    #def __back__(self):
       ##    raise StopIteration
      #  value = self.data[self.position]
     #   self.position -= 1
     #   return value

if __name__ == "__main__":
    i = MyItertor([1, 2, 3,4,2,6])
    for x in i:
        print(x)
        
        
        
        
class MyBidirectionalIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        value = self.data[self.position]
        self.position += 1
        return value

    def back(self):
        self.position -= 1
        if self.position < 0:
            self.position = 0
            raise StopIteration
        return self.data[self.position]

if __name__ == "__main__":
    i = MyBidirectionalIterator([1, 2, 3, 4, 5])
    
    # 정방향 순회
    print("Forward iteration:")
    for x in i:
        print(x, end=' ')
    print()

    # 역방향 순회
    print("\nBackward iteration:")
    try:
        while True:
            print(i.back(), end=' ')
    except StopIteration:
        pass
    print()

    # 다시 정방향 순회
    print("\nForward iteration again:")
    i = MyBidirectionalIterator([1, 2, 3, 4, 5])  # 이터레이터 재초기화
    for x in i:
        print(x, end=' ')
    print()



# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])

# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))






