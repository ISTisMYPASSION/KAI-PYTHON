print('Enter correct username and password to continue')

count=0

while count < 3:

    username = input('Enter username: ')

    password = input('Enter password: ')
    
    if password=='1234' and username=='gowanbrae_admin':
    
        print('Welcome To Gowan Brae School,')
        
        break
    
    else:
        print('Access denied. Try again.')
        count += 1
