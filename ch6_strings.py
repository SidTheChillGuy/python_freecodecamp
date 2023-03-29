for n in "banana":
    print(n)

print('')
# slicing
s = 'Sid The Chill Guy'

print(s)
print(s[0:5])  # <-- slice from 0 upto (but not including) 5 ie only till 4
print(s[7:8])
# 75 characters arent present in the string, so it will end when string ends without errors
print(s[9:75])
print(s[4:])  # 0 to end
print(s[:8])  # start to 8-1
print(s[:])  # start to end note s[:] = s

# concatenation
a = 'Hello'
b = a + 'There'
c = a + ' ' + 'There'

print('')
print(a)
print(b)
print(c)

# few functions
print('')

greet = 'Hello There'

f1 = greet.lower()
print(f1)

print('WELCOME'.lower())
print('qwertyuiopasdfghjklzxcvbnm'.upper())

f2 = greet.replace('There', 'Sid The Chill Guy')
print(f2)

f3 = f2.replace('l', 'Q')
print(f3)

greet_two = '   Whitespace  '
print(greet_two.lstrip())
print(greet_two.rstrip())
print(greet_two.strip())
# strip removes the blank space aat start/end of the string, 'strip' function removes fro both sides

print('')

greet = 'Please tighten your seatbelts before the plane takes off!'

print(greet.startswith('Please'))
print(greet.startswith('p'))
print(greet.startswith('P'))

# some usage like pasing and extracting  :thumbs_up:
print('')
# example we would extract the email container from here
data = 'From siddhantmahajan@imaginaryemail.com Tue Mar 28 20:53:45 2023'

position = data.find('@') # finds @ position
space_position = data.find(' ',position) # finds the space after the email container
host_extension = data[position+1 : space_position] # slicing the data (container starts from @ + 1 and ends upto but nnot including space)

print(position)
print(space_position)
print(host_extension)
