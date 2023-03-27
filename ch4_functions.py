def func1():
    print("hello")


# def (define) 'name the function' ': colon to denote start the function body'
# '  ' indent to define that the next lines belong to upper body
# un indent to define that body has ended

# def also indicates start of a function and that the indented code is to be stored for later calling/referencing

func1()
print(func1())  # <-- note this will also output a 'none'
# calling the function
print(' ')

# two types A- inbuilt functions like print B- definded functions

print('hello')


def func2():
    print('line 1')
    print('line 2')


print('i will print 2 lines')
func2()
print('haha see i printed two lines')

# few use cases
print(' ')


def greet(x):
    if x == 'en':
        print('hi')
    elif x == 'fr':
        print('bonjour')
    elif x == 'es':
        print('hola')
    else:
        print('namaste')


greet('en')
greet('es')
greet('fr')
greet('anything else')

# exercise
hours = int(input('enter the amount of hours \n'))
rate = int(input('enter the pay rate per hour \n'))
print(" ")

# simple method


def computepaysimpli(hours, rate):
    payout = hours * rate
    return payout #<-- importnat where we are getting an output


def computepayComplexi(hours, rate):
    if hours > 40:
        payout = ((hours - 40) * rate) + (40 * rate)
    else:
        payout = (hours * rate)
    return payout

print(computepaysimpli(hours , rate))
print(computepayComplexi(hours , rate))