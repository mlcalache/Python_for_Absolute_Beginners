def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")


prints_four()
prints_four()
prints_four()
prints_four()


def function_name(param1):
    print("function_name")
    print(type(param1))


function_name("Matheus")
function_name(1)


def function_sum(param1, param2):
    print("function_sum")
    print(param1 + param2)


function_sum(1, 2)


def function_with_default_values(num1=1, num2=2):
    print("function_with_default_values")
    print(num1 + num2)


function_with_default_values()
function_with_default_values(2,3)


def function_with_return(num1=1, num2=2):
    print("function_with_return")
    return num1 + num2


result = function_with_return(3,4)
print(result)
