# Python으로 JS 따라하기



# def calculator(fun,a,b):
#     if fun == 'add':
#         rlt = a+b
#     elif fun == 'mul':
#         rlt = a*b
#     return rlt

# print(calculator('add',1,2))
# print(calculator('mul',3,4))

# def add(x,y):
#     return x+y
# def mul(x,y):
#     return x*y

# calculator = {
#     'add' : add,
#     'mul' : mul
# }


calculator = {
    'add' : lambda x, y : x + y,
    'mul' : lambda x, y : x * y
}

print(calculator['add'](1,2))
print(calculator['mul'](3,4))