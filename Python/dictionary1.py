information ={
    'first_name' : 'Tanjila',
    'lat_name'   : 'Munni',
    'age'        : '25',
    'hometown': 'Rajshahi'
    
    
}
for key,value in information.items():
    print(f"{key} {value}")

x = information.get('first_name','First name is not availabe')
print(f"the result is: {x}")