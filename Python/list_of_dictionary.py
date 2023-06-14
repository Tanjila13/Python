user = {
  'reza' : {
    'first' : 'Rizve Rahman',
    'last' : 'Reza',
    'home' : 'Magura'
  },

  'humaira' : {
    'first' : 'Humayra',
    'last' : 'Honey',
    'home' : 'Gazipur'
  },
  
}

for name,info in user.items():
    print(f'Name: {name}')
    for key, value in info.items():
        print(f'full name: {key} : {value}')