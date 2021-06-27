dic = {"hola":4,"adios":5,"jeje":3}

llave = sorted(dic, reverse=True)

print(llave)

for i in llave:
    print(i[0],"->",i[1])