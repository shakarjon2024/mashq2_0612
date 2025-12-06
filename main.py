#  1 - misol
a = [2, 3, 4]
b = [1, 2, 3]

result = list(map(lambda x, y: x * y, a, b))
print(result)



#  2 - misol
lst = [-2, 3, -5, 7, -1]
result = list(filter(lambda x: x < 0, lst))
print(result)



# 3 - misol
lst = ["1kitob", "salom", "3dunyo", "python"]
result = list(filter(lambda s: s[0].isdigit(), lst))
print(result)



# 4 - misol
import math

lst = [3, 4, 5]
result = list(map(lambda x: math.factorial(x), lst))
print(result)



# 5 - misol
lst = [3, 4, 6, 7, 9]
result = list(map(lambda x: x**2, filter(lambda n: n % 2 == 0, lst)))
print(result)



# 6 - misol
lst = ["level", "python", "madam", "radar", "salom"]
result = list(filter(lambda s: s == s[::-1], lst))
print(result)



# 7 - misol
lst = [1, 2, 3, 4]

result = list(
    map(lambda x: (x**3 if (x**3) % 2 != 0 else (x**3)//2), lst)
)
print(result)






























