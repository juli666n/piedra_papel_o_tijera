print ("Bienvenido a piedra papel o tijera.\n para elegir piedra ecribe el numero 1 \n para elegir papel ecribe el numero 2 \n para elegir tijera ecribe el numero 3")
jugador1 = input ("Jugador uno digita el numero correspondiente a tu eleccion:")
jugador2 = input ("Jugador dos digita el numero correspondiente a tu eleccion:")

if jugador1==1 and jugador2==3 or jugador1==2 and jugador2==1 or jugador1==3 and jugador2==2:
    print("jugador uno gana")
elif jugador1==3 and jugador2==1 or jugador1==1 and jugador2==2 or jugador1==2 and jugador2==3:
    print ("jugador dos gana")
else:
    print ("no valido")
