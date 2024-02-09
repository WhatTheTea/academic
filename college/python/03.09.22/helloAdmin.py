def login(name):
    if(name == 'admin'):
        message = "Hello " + name + ", access to control panel granted."
    else:
        message = "Hello " + name + ", have a nice day"
    
    print(message)

#users = ['admin', 'Alex', 'Vika', 'Oleg', 'Pavel']
users = []

if len(users) == 0:
    print("We need to find some users")
else:
    for user in users:
        login(user)