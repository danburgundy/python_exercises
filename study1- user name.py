# Study1- take the user name with strip and title function
name = '' # False
while not name.strip():
    name = input('Enter your name: ')
    
print(f'Hello, {name.title()}')
