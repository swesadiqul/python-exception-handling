# num2 = input('Enter a number: ')

'''it will print type error, because there are different types of value'''
# result = 20 / num2
# print(result)
# print('Done!')



# num2 = int(input('Enter a number: '))

'''it will be print ZeroDivisionError, if user provides wrong input.'''
# result = 20 / num2
# print(result)
# print('Done!')


# list_a = ['Sadiqul','Julfiker','Zubayer']
'''it will be print IndexError, if user provides index out of range'''
# print(list_a[3])
# print('Done!')



'''it will be print also ZeroDivisionError, but now we will handle this error.'''
try:
    list = [20,0,30]
    # result0 = list[0] / list[1]
    result1 = list[0] / list[3]
    # print(result0)
    print(result1)
    print('Done!')

except ZeroDivisionError:
    print('Division by zero is not possible.')
# except IndexError:
#     print('This is not possible. Because list index out of range')

finally:
    print('Successful!')
