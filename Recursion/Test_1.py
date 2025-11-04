class Test1(object):
    def fibonacci(self, n):
        if n==0: return 0
        if n==1: return 1

        return fibonacci(n-1) + fibonacci(n-2)

testCase = Test1()
testCase.fibonacci()