# try:
#     num1 = int(input('Enter the first number: '))
#     num2 = int(input('Enter the second number: '))

#     result = num1 / num2
#     print(result)

# except (ValueError,ZeroDivisionError):
#     print('You have entered incorrect input.')

# finally:
#     print('Thanks....')


def voter(age):
    if age <= 18:
        raise ValueError('Invalid Voter.')
    return 'You are allowed to vote.'


try:
    print(voter(17))

except ValueError as e:
    print(e)
