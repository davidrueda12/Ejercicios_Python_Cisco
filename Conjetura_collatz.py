co = int(input("Ingrese un numero natural: "))
	
while co != 1:
    if co%2 == 0:
        co = co // 2  
        print(co)
    else: 
        co = 3*co+1
        print(co)  
       
