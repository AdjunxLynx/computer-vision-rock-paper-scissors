lambda1 = lambda x: x ** 2
print(lambda1(5))

lambda2 = lambda x: x**3
print(lambda2(5))

lambda3 = lambda x,y: x+y
print(lambda3(4,5))

lambda4 = lambda x, y: x*y
print(lambda4(5,6))

test_list = [("jon", 8), ("bob", 4), ("hello", 69), ("why", 420), ("kamil", 4328623)]
print(sorted(test_list, key = lambda x: x[1]))

print(sorted( test_list, key = lambda x: x[0]))

print(sorted(test_list, key = lambda x: len(x[0])))

temp = sorted(test_list, key = lambda x: len(x[0]))
print(temp[::-1])

number_list = [1, 5, 7, 9, 21, 8]
print(list(map(lambda1, number_list)))

print(list(map(lambda2, number_list)))

lambda6 = lambda x: lambda1(x) if x%2==0 else lambda2(x)

print(list(map(lambda6, number_list)))

strings = ["string1", "hello", "why here", "smelly","funny","football","aardvark","xylophone","kamil","python","vscode", "ellodas"]

lambda7 = lambda x: True if len(x) > 5 else False
print(list(filter(lambda7, strings)))

lambda8 = lambda x: True if len(x) > 5 and x[0] in "aieou" else False
print(list(filter(lambda8, strings)))