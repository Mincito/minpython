#for i in range(5):
    # print (hola)


# for i in range(1,6):
#     print(1)

# for i in range(5):
#     print (i+1)    


# for j in range (1,11):
#     print ("la tabla del", j)
#     for i in range (1,11):
#         print (j, "x", i, "=", i*j)

# ## Ipreguntas la cantidad de notas y promediar


# cantN=int(input("Ingrese la cantidad de notas"))
# suma=0
# for i in range(cantN):
#     print(f"ingrese la nota numero {i + 1}" )
#     nota=float(input())
#     suma=suma+nota

# prom=suma/cantN

# print (f"El promedio es {prom}")

# if prom>=4:
#     print("Aprobado")

# else:
#     print("Desaprobado")

# cant=int(input("Ingrese la cantidad de productos que queire"))
# total=0
# for i in range (cant):
#     print('''
#     Que producto llevará?
#        1) Diazepam
#        2) Betametasona
#        3) Oblea china
#     ''')
# op=int(input())
# if op==1:
#     print("Usted lleva diazepam")
#     total=total+9000
# elif op==2:
#     print("Usted lleva betametasona")
#     total=total+18500
# elif op==3:
#     print ("LLeva oblechina")
#     total=total+1000
# else:
#     print("ERROR DEL SISTEMA, SELECCIONE OPCION VALIDA")


# print ("El total de su compra es", total)
# print ("El total de su compra + iva es", total*1.19)


#VOTATOON
#ELIJA 2 CANDIDATOS. PREGUNTE CUANTOS VOTANTES SON. POR CADA VOTANTE DEBE PREGUNTAR POR QUIEN VOTARÁ
#CUENTE LA CANTIDAD DE VOTOS Y MUESTRE LOS RESULTADOS
#DEFINIR QUIEN GANÓ LA VOTACIÓN CONSIDERANDO EL EMPATE

c1="Shaggy"
c2="Dexter"
vc1=0
vc2=0
v
cant=int(input("Ingrese la cantidad de votantes"))

for i in range (cant):
    print(f"Seleccione su candidato: 1){c1}, 2){c2}")
    voto=int(input)
    if voto==1:
        #vc1=vc1+1
        vc1+=1
    else:
        vc2+=1
print(f"La cantidad de votos de {c1} es: {vc1}")
print(f"La cantidad de votos de {c2} es: {vc2}")

if vc1>vc2:
    print (f"El ganador es {c1}")
elif:
    print (f"El ganador es {c2}")  
else:
    print ("EMpate")  


