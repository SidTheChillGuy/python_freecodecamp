# let
n = 5
while n > 0:
    print(n)
    n = n - 1
print('takeoff!')
print(0)

# let
print(' ')

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

# let
print(' ')
friends = ['dosta', 'mitra', 'bhava']
for friend in friends:
    print('happy new year', friend)


# loop idioms
# find the lagest number
print(' ')
largest_so_far = 'None'
print('before', largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far == 'None':
        largest_so_far = num
    elif num > largest_so_far:
        largest_so_far = num
    
    print(largest_so_far, num)
print('after', largest_so_far)

# counting
print(' ')
the_count = 'None'
print('before', the_count)
for num in [9, 41, 12, 3, 74, 15]:
    if the_count == 'None':
        the_count = 1
    else:
        the_count = the_count + 1
    print(the_count, num)
print('after', the_count)

# summing in the loop
print(' ')
the_sum = 'None'
print('before', the_sum)
for num in [9, 41, 12, 3, 74, 15]:
    if the_sum == 'None':
        the_sum = num
    else:
        the_sum = the_sum + num
    print(the_sum, num)
print('after', the_sum)

# averaging at the end
print(' ')
the_count = 'None'
the_sum = 'None'
print('before', 0)  # <-- the verage  is 0 before any operation
for num in [9, 41, 12, 3, 74, 15]:
    if the_count == 'None' and the_sum == 'None':
        the_count = 1
        the_sum = num    
    else:
        the_count = the_count + 1
        the_sum = the_sum + num
    print(the_count, the_sum, num)
print('after', (the_sum/the_count))

# find results
print('')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large value then 20 is ', value)

# true false stuff
print('')
found = 'false'
print('before', found)
x = int(input('enter the number to find \n'))
for num in [9, 41, 12, 3, 74, 15]:
    if num == x:
        found = 'true'
       # break
    # else:
    #    print('couldnt find ', x)
    # commented out 'else' part to prevent spamming console when value isnt found, so you dont need the 'break' part aswell
if found == 'true':
    print(x, 'was found')
else:
    print(x, 'wasnt found')
print('after', found)
