def datosHardodeados():
    minerales = ["calcio","H2O","Zinc","Hierro","sodio","potacio","Magnesio"]
    # print(minerales[4])
    minerales.append("Fosforo")
    minerales.insert(5,"Mangaeso")
    #minerales.remove("H2O")
    #minerales.pop()
    #del minerales[3]
    #print(minerales)
    return minerales

minerales = datosHardodeados()

for i in range(3,len(minerales),2):
    print(str(i) + " " + minerales[i])

#for mineral in minerales:
#    print(mineral)

