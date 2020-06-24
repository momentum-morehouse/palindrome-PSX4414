name = input('Please enter your name  ')
print(name)
if name == name[::-1]:
  print(name, 'is a palindrome.')
else:
  print(name,'is not a palindrome.')