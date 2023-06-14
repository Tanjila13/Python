
aliens = []
for a in range(30):
   
      
   if a <10:
      color = 'Red'
      point = 10
      
   elif 10<= a <20:
      color ='yellow' 
      point = 5
   
   else:
      color = 'green'
      point = 10   
      
   all_aliens = {'color':color,'point': point}
   aliens.append(all_aliens)
   
for alien in aliens:
   print(aliens)     
   
   