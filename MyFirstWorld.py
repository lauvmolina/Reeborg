'''
Este programa indica al robot ir por una manzana y 
recogerla, luego dejar una banana en su lugar y
finalmente devolverse a su casa

Autor: Laura Molina
Fecha: 29/07/2019
'''

print("Hola soy reeborg")
print("Voy para una misiòn")
repeat 4: #repite el movimiento 4 veces
    move() #realiza movimiento el linea recta
#pause() se detiene el robot
take() #toma el objeto
#pause()
put("banana") #pone el objeto
#pause()
repeat 2: #repite el movimiento 2 veces
    turn_left() #gira hacie la izquierda
#pause()
repeat 4:
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
