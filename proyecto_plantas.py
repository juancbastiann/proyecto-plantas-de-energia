consumo_energia = {
    'Coca Codo Sinclair': {
        'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
        'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
    },
}

plantas = {
    'Quito': ('Coca Codo Sinclair', 'Sopladora'),
    'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
    'Loja': ('Sopladora')
}

informacion = {
    'costa': ('Guayaquil', 'Manta'),
    'sierra': ('Quito', 'Ambato', 'Loja'),
    'oriente': ('Tena', 'Nueva Loja')
}

def menu_principal ():
    print('<1> MWh planta/ciudad\n<2> MWh plantas/ciudad\n<3> Dinero recaudado por región\n<4> Terminar programa')

def primer_menu ():
    p = str(input('Ingrese el nombre de la planta(mayus): '))
    c = str(input('Ingrese el nombre de la ciudad(mayus): '))

    if p == 'COCA CODO SINCLAIR' and c =='QUITO':
    #COCA QUITO
        tarifa_coca_quito = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']

        print('Consumo total:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')

    elif p == 'COCA CODO SINCLAIR' and c == 'GUAYAQUIL':
        #COCA GUAYAQUIL
        tarifa_coca_guayaquil = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']

        print('Consumo total:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')

    elif p == 'SOPLADORA' and c == 'GUAYAQUIL':
    #SOPLADORA GUAYAQUIL
        tarifa_sopladora_guayaquil = consumo_energia['Sopladora']['Guayaquil']['tarifa']

        print('Consumo total:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')

    elif p == 'SOPLADORA' and c == 'QUITO':
    #SOPLADORA QUITO
        tarifa_sopladora_quito = consumo_energia['Sopladora']['Quito']['tarifa']
        
        print('Consumo total:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')

    elif p == 'SOPLADORA' and c == 'LOJA':
    #SOPLADORA LOJA
        tarifa_sopladora_loja = consumo_energia['Sopladora']['Loja']['tarifa']

        print('Consumo total:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')

    else:
        print('¡DATOS ERRONEOS!\nINGRESE NUEVAMENTE LOS DATOS DE LA PLANTA Y LA CIUDAD')

def segundo_menu ():
    c = str(input('Ingrese el nombre de la ciudad(mayus): '))
    if c == 'QUITO':
        print('Las plantas que producen energia en esta ciudad son', plantas['Quito'])
        print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')
        print('SOPLADORA:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')

    elif c == 'GUAYAQUIL':
        print('Las plantas que producen energia en esta ciudad son', plantas['Guayaquil'])
        print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')
        print('SOPLADORA:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')

    elif c == 'LOJA':
        print('SOPLADORA:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')
    else:
        print('¡LA CIUDAD DE LA QUE DESEA OBTENER INFORMACION NO RECIBE ENERGIA!')

def tercer_menu ():
    r = str(input('Ingrese el nombre de una region(mayus): '))
    if r == 'SIERRA':
        q_c_a = sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])
        q_c_b = sum(consumo_energia['Sopladora']['Quito']['consumos'])
        q_t_a = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
        q_t_b = consumo_energia['Sopladora']['Quito']['tarifa']

        l_c_a = sum(consumo_energia['Sopladora']['Loja']['consumos'])
        l_t_a = consumo_energia['Sopladora']['Loja']['tarifa']
        print('LOS INGRESOS DE LA REGION SIERRA:', '$',((q_c_a*q_t_a) + (q_c_b*q_t_b)) + (l_c_a*l_t_a))
    elif r == 'COSTA':
        g_c_a = sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])
        g_c_b = sum(consumo_energia['Sopladora']['Guayaquil']['consumos'])
        g_t_a = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
        g_t_b = consumo_energia['Sopladora']['Guayaquil']['tarifa']
        print('LOS INGRESOS DE LA REGION COSTA:', '$',((g_c_a*g_t_a) + (g_c_b*g_t_b)))
    elif r == 'ORIENTE':
        print('¡LA REGIÓN NO CUENTA CON REGISTROS!')
    else:
        print('¡ERROR!')


op = -1
while op != 0:
    menu_principal()
    m1 = int(input('Ingrese una opción: '))
    while m1 == 1:
        primer_menu ()
        print('¡REGRESANDO AL MENU PRINCIPAL!')
        break
    while m1 == 2:
        segundo_menu ()
        print('¡REGRESANDO AL MENU PRINCIPAL!')
        break
    while m1 == 3:
        tercer_menu ()
        print('¡REGRESANDO AL MENU PRINCIPAL!')
        break
    while m1 == 4:
        print('¡TERMINANDO PROGRAMA!')
        quit ()