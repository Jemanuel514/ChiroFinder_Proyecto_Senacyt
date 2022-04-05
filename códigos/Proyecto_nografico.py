def inicio():
    bienvenida()
    seleccion_modo()

def bienvenida():
    print("¡Bienvenido a Taxonomía Programada!")

def seleccion_modo():
    print("Seleccione una opción:")
    print("1. Inicio.")
    print("2. Créditos.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_1()
    elif respuesta == "2":
        print("Créditos:")
        print("José Huertas-Desarrollador del proyecto")
        print("José Fung-Mentor")
        print("Katia Chérigo-Coordinadora del proyecto")
        print("Iris Gómez-Coordinadora del Programa de Conservación de Murciélagos del CRU Coclé")
        print("Pablo Gutierrez & Fernando Guardia-Especialistas del Programa de Conservación de Murciélagos del CRU Coclé")
        seleccion_modo()
    else:
        print("La respuesta no es válida.")
        seleccion_modo()

def preg_murc_1():
    print ("Estructura en forma de hoja encima de la nariz (apéndice nasal foliar libre):")
    print("1. Presente.")
    print("2. Ausente.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_2()
    elif respuesta == "2":
        preg_murc_52()
    elif respuesta == "3":
        seleccion_modo()
    else:
        print("La respuesta no es válida.")
        preg_murc_1()

def preg_murc_2():
    print("Rabo:")
    print("1. Presente.")
    print("2. Ausente.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_3()
    elif respuesta == "2":
        preg_murc_33()
    elif respuesta == "3":
        preg_murc_1()
    else:
        print("La respuesta no es válida.")
        preg_murc_2()
    
def preg_murc_3():
    print("¿La cola se extiende hasta el margen de la membrana interfemoral(MI)?")
    print("1. Sí.")
    print("2. No.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_4()
    elif respuesta == "2":
        preg_murc_5()
    elif respuesta ==3 :
        preg_murc_2()
    else:
        print("La respuesta no es válida.")
        preg_murc_3()

def preg_murc_4():
    print("Seleccione la opción más acertada:")
    print("1. Posee líneas de dentículos dermales en el margen ventral posterior de la MI, orejas alrededor del tamaño de la cabeza, peso el cuerpo +/- 8g, antebrazo 34-37mm.")
    print("2. Posee el margen posterior de la membrana interfemoral desnudo, orejas y hoja de la nariz mucho más alargado que la cabeza, peso corporal +/- 18g, antebrazo 49-54mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Macrophyllum macrophyllum.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Lonchorhina aurita.")
        reinicio()
    elif respuesta == "3":
        preg_murc_3()
    else:
        print("La respuesta no es válida.")
        preg_murc_4()

def preg_murc_5():
    print("Calcar(o calcáneo):")
    print("1. Obviamente más alargado que el pie.")
    print("2. Igual o más corto que el pie.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_6()
    elif respuesta == "2":
        preg_murc_15()
    elif respuesta == "3":
        preg_murc_3()
    else:
        print("La respuesta no es válida.")
        preg_murc_5()

def preg_murc_6():
    print("Seleccione la opción más acertada:")
    print("1. Con una línea medio-dorsal blanca, hoja en la nariz con pelos y mellada, peso corporal +/-15g, antebrazo de 46-55mm.")
    print("2. Sin línea, hoja en la nariz desnuda.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Mimon crenulatum.")
        reinicio()
    elif respuesta == "2":
        preg_murc_7()
    elif respuesta == "3":
        preg_murc_5()
    else:
        print("La respuesta no es válida.")
        preg_murc_6()

def preg_murc_7():
    print("Antebrazo de:")
    print("1. menos de 48mm.")
    print("2. más de 48mm.")
    print("3. Volver")
    respuesta = int(input)
    if respuesta == "1":
        preg_murc_8()
    elif respuesta == "2":
        preg_murc_11()
    elif respuesta == "3":
        preg_murc_6
    else:
        print("La respuesta no es válida.")
        preg_murc_7()

def preg_murc_8():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo +40mm, dedos del pie y antebrazo notablemente peludo, una cresta de pelos largos en la corona de los machos adultos, con 4 incisivos inferiores, Micronycteris tiene un ornamento simple en la barbilla (cojincillos suaves alargados), faja entre las orejas (una membrana delgada que conecta en parte o enteramente las bases de las orejas a través de la frente), peso corporal de 16g y antebrazo de 42-46mm.")
    print("2. Antebrazo -40mm, dedos del pie y antebrazo sin pelos notables.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Micronycteris hirsuta.")
        reinicio()
    elif respuesta == "2":
        preg_murc_9()
    elif respuesta == "3":
        preg_murc_7()
    else:
        print("La respuesta no es válida.")
        preg_murc_8()

def preg_murc_9():
    print("Seleccione la opción más acertada:")
    print("1. Parte inferior del cuerpo blanquizco, 4 incisivos inferiores, peso corporal +/-7g y antebrazo de 34-38mm.")
    print("2. Partes inferiores del cuerpo chocolate.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Micronycteris schmidtorum.")
        reinicio()
    elif respuesta == "2":
        preg_murc_10()
    elif respuesta == "3":
        preg_murc_8()
    else:
        print("La respuesta no es válida.")
        preg_murc_9()

def preg_murc_10():
    print("Seleccione la opción más acertada:")
    print("1. Lóbulo anterior de la oreja densamente peludo hasta casi la punta, pelo dorsal largo (8mm) e hirsuto (velludo), 4 incisivos inferiores, longitud de las orejas de 21-22mm, pelo corto en el lóbulo basal anterior (+/-3mm), pelo más largo en la espalda superior (10-11mm), dorso rojizo-chocolate, peso corporal +/-7g y antebrazo de 32-37mm.")
    print("2. Longitud de las orejas de 18-19mm, pelo más largo en el lóbulo basal anterior(7mm), pelo más corto en la espalda superior (8mm), dorso gris-chocolate oscuro, peso +/-7g y antebrazo de 32-37mm.")
    print("3. Lóbulo anterior de las orejas escasamente peludo en la base, pelo dorsal corto (4mm), 2 incisivos inferiores, vientre chocolate, apenas diferente al torso, faja entre las orejas ausente, cara escasamente peluda, el ornamento de la barbilla es una 'V' en forma de dos frijoles, peso corporal +/-9g y antebrazo de 33-40mm.")
    print("4. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Micronycteris megalotis.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Micronycteris microtis.")
        reinicio()
    elif respuesta == "3":
        print("Su murciélago es Tonatia brasilienis.")
        reinicio()
    elif respuesta == "4":
        preg_murc_9()
    else:
        print("La respuesta no es válida.")
        preg_murc_10()

def preg_murc_11():
    print("Seleccione la opción más acertada:")
    print("1. Orejas cortas, no extienden más allá de la nariz cuando se las coloca hacia adelante, peso corporal +/-126g y antebrazo de 80-93mm.")
    print("2. Orejas más largas que la cabeza.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Phyllostomus hastatus.")
        reinicio()
    elif respuesta == "2":
        preg_murc_12()
    elif respuesta == "3":
        preg_murc_7()
    else:
        print("La respuesta no es válida.")
        preg_murc_11()
    
def preg_murc_12():
    print("Seleccione la opción más acertada:")
    print("1. Orejas puntiagudas, peso corporal +/-20g y antebrazos de 53-61mm.")
    print("2. Orejas redondeadas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Mimon bennetti.")
        reinicio()
    elif respuesta == "2":
        preg_murc_13()
    elif respuesta == "3":
        preg_murc_11()
    else:
        print("La respuesta no es válida.")
        preg_murc_12()

def preg_murc_13():
    print("Seleccione la respuesta más acertada:")
    print("1. Antebrazo +70mm, pelo largo y lanoso, herradura de la hoja de la nariz fuertemente bordeada ventralmente, peso corporal +/-84g y antebrazo de 77-83mm.")
    print("2. Antebrazo -70mm, pelo más corto y no lanoso, herradura atada para bajo ventralmente.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Chrotopterus auritus.")
        reinicio()
    elif respuesta == "2":
        preg_murc_14()
    elif respuesta == "3":
        preg_murc_12()
    else:
        print("La respuesta no es válida.")
        preg_murc_13()

def preg_murc_14():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo peludo, línea blanca en corona, gargante gris, peso corporal +/-36g y antebrazo de 56-61mm.")
    print("2. Antebrazo casi desnudo, sin línea en la corona, garganta blanca o blanquizca, cara desnuda, coloca las orejas para atrás cuando se toca la cabeza, peso corporal +/-34g y antebrazo 50-56mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Tonatia saurophila.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Tonatia silvicola.")
        reinicio()
    elif respuesta == "3":
        preg_murc_13()
    else:
        print("La respuesta no es válida.")
        preg_murc_14()

def preg_murc_15():
    print("Antebrazo de:")
    print("1. +50mm.")
    print("2. -50mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_16()
    elif respuesta == "2":
        preg_murc_19()
    elif respuesta == "3":
        preg_murc_5()
    else:
        print("La respuesta no es válida.")
        preg_murc_15()

def preg_murc_16():
    print("Seleccione la opción más acertada:")
    print("1. Orejas puntiagudas, peso corporal +/-24g y antebrazo de 54-58mm.")
    print("2. Orejas redondeadas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Glyphonycteris daviesi.")
        reinicio()
    elif respuesta == "2":
        preg_murc_17()
    elif respuesta == "3":
        preg_murc_15()
    else:
        print("La respuesta no es válida.")
        preg_murc_16()

def preg_murc_17():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo peludo, labios granujientos, peso corporal +/-35g y antebrazo de 57-65mm.")
    print("2. Antebrazo casi desnudo, labios lisos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Trachops cirrhosus.")
        reinicio()
    elif respuesta == "2":
        preg_murc_18()
    elif respuesta == "3":
        preg_murc_16()
    else:
        print("La respuesta no es válida.")
        preg_murc_17()

def preg_murc_18():
    print("Seleccione la opción más acertada:")
    print("1. Puntas de las alas blancas, tragus atenuado, pelo corto, sedoso, hoja de la nariz tiene una forma de un triángulo de 90° en la base, peso corporal +/-61g, antebrazo de 60-68mm.")
    print("2. Alas sin puntas blancas, tragus contundente, peso corporal +/-42g, antebrazo de 60-68mm.")
    print("3. Volver")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Phylloderma stenops.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Phyllostomus discolor.")
        reinicio()
    elif respuesta == "3":
        preg_murc_17()
    else:
        print("La respuesta no es válida.")
        preg_murc_18()

def preg_murc_19():
    print("Pelos dorsales:")
    print("1. Tricoloridos.")
    print("2. Bicoloridos o monocoloridos.")
    print("3.Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_20()
    elif respuesta == "2":
        preg_murc_26()
    elif respuesta == "3":
        preg_murc_15()
    else:
        print("La respuesta no es válida.")
        preg_murc_19()

def preg_murc_20():
    print("Ornamento de barbilla:")
    print("1. Simple.")
    print("2. Mosaico de verrugas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_21()
    elif respuesta == "2":
        preg_murc_24()
    elif respuesta == "3":
        preg_murc_19()
    else:
        print("La respuesta no es válida.")
        preg_murc_20()

def preg_murc_21():
    print("Seleccione la opción más acertada:")
    print("1. Hoja de la nariz muy pequeña y triangular, lengua extensible, vibrisas conspicuas, orejas cortas y redondeadas, incisivos inferiores ausentes, peso corporal +/-8g y antebrazo de 31-35mm.")
    print("2. Hoja de la nariz más larga que ancha, lengua no extensible, vibrisas no conspicuas, orejas de tamaño intermedio.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_22()
    elif respuesta == "2":
        preg_murc_23()
    elif respuesta == "3":
        preg_murc_20()
    else:
        print("La respuesta no es válida.")
        preg_murc_21()

def preg_murc_22():
    print("Seleccione la opción más acertada:")
    print("1. Hocico menos elongado, alas conectadas a los pies cerca de la base de los dedos.")
    print("2. Hocico muy elongado, alas conectadas a los tobillos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lichonycteris obscura.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Hylonycteris underwoodi.")
        reinicio()
    elif respuesta == "3":
        preg_murc_21()
    else:
        print("La respuesta no es válida.")
        preg_murc_22()

def preg_murc_23():
    print("Seleccione la opción más acertada:")
    print("1. Oreja angosta (mucho más larga que ancha), línea blanca indistinta en la espalda (normalmente), negro alrededor de los ojos, peso corporal +/-11g, antebrazo de 37-40mm, dos verrugas paralelas en la barbilla.")
    print("2. Oreja ancha (más o menos misma largura y longitud) sin línea en la espalda, peso corporal +/-10g y antebrazo de 37-43mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Trinycteris nicefori.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Glyphonycteris sylvestris.")
        reinicio()
    elif respuesta == "3":
        preg_murc_21()
    else:
        print("La respuesta no es válida.")
        preg_murc_23()

def preg_murc_24():
    print("Seleccione la opción más acertada:")
    print("1. Tercer diente post-canino (M1) más bajo que los dientes adyacentes, antebrazo -38mm, pelos dorsales normalmente chocolates, indistintamente tricoloridos, la menos especies de los 3 del género Carollia, peso corporal +/-13g (11-15) y antebrazo de 34-38mm.")
    print("2. Tercer diente post-canino (M1) tiene misma altura como los dientes adyacentes, antebrazo +38mm, pelos dorsales normalmente gris, notablemente tricoloridos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Carollia castanea.")
        reinicio()
    elif respuesta == "2":
        preg_murc_25()
    elif respuesta == "3":
        preg_murc_20()
    else:
        print("La respuesta no es válida.")
        preg_murc_24()

def preg_murc_25():
    print("Seleccione la opción más acertada:")
    print("1. Tibia y antebrazo peludo, extremidad posterior(rodilla a tobillo) +/-17mm, rodilla a puntas de garras 26-29mm, pelo más suave, largo y notablemente tricolorido en el dorso, línea de dientes superiores inclinada hacia afuera hasta PM4, peso corporal +/-15g y antebrazo de 27-42mm.")
    print("2. Antebrazo casi desnudo, rodilla a tobillo +/-21mm, rodilla a la punta de las garras 29-32mm, pelo más áspero, la especie más grande del género, peso corporal +/-19g y antebrazo de 41-45mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Carollia brevicauda.")
        reinicio()
    elif respuesta == "2":
        print(" Su murciélago es Carollia perspicillata.")
        reinicio()
    elif respuesta == "3":
        preg_murc_24()
    else:
        print("La respuesta no es válida.")
        preg_murc_25()

def preg_murc_26():
    print("Seleccione la opción más acertada:")
    print("1. Hocico largo, lengua extensible, orejas cortas y redondeadas.")
    print("2. Hocico corto, lengua no extensible, orejas largas y no redondeadas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_27()
    elif respuesta == "2":
        preg_murc_32()
    elif respuesta == "3":
        preg_murc_19()
    else:
        print("La respuesta no es válida.")
        preg_murc_26()

def preg_murc_27():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo +40mm, peso corporal +/-15g y antebrazo de 40-45mm.")
    print("2. Antebrazo -40mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lonchophylla robusta.")
        reinicio()
    elif respuesta == "2":
        preg_murc_28()
    elif respuesta == "3":
        preg_murc_26()
    else:
        print("La respuesta no es válida.")
        preg_murc_27()

def preg_murc_28():
    print("Seleccione la opción más acertada:")
    print("1. Pelos dorsales monocoloridos, dorso rojizo-chocolate, pelos cortos, rostro corto, peso corporal +/-8g y antebrazo de 32-38m.")
    print("2. Pelos dorsales bicoloridos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lionycteris spurrelli.")
        reinicio()
    elif respuesta == "2":
        preg_murc_29()
    elif respuesta == "3":
        preg_murc_27()
    else:
        print("La respuesta no es válida.")
        preg_murc_28()

def preg_murc_29():
    print("Incisivos interiores superiores:")
    print("1. mucho más largos que los exteriores y sobresalientes.")
    print("2. solamente un poco más largos que los exteriores y no notablemente sobresalientes.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_30()
    elif respuesta == "2":
        preg_murc_31()
    elif respuesta == "3":
        preg_murc_28()
    else:
        print("La respuesta no es válida.")
        preg_murc_29()

def preg_murc_30():
    print("Seleccione la opción más acertada:")
    print("1. Calcar (o calcáneo) llega hasta el final de la segunda falange cuando se le coloca a lado del pie, pulgar peludo, dorso anaranjado-chocolate, parte inferior del cuerpo amarilla o blanquizca, peso corporal +/-8g y antebrazo de 32-35mm.")
    print("2. Calcar (o calcáneo) llega solamente un poco más allá del final de la primera falange cuando se lo coloca a lado del pie; pulgar no peludo; dorso chocolate; negruzco-chocolate en nuca; corona, cara y partes inferiores del cuerpo chocolate; peso corporal +/-6g y antebrazo de 29-34mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lonchophylla mordax.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Lonchophylla thomasi.")
        reinicio()
    elif respuesta == "3":
        preg_murc_29()
    else:
        print("La respuesta no es válida.")
        preg_murc_30()

def preg_murc_31():
    print("Seleccione la opción más acertada:")
    print("1. Incisivos superiores (vista oclusa) forman una creciente regular, incisivos interiores solamente poco más largos que los exteriores, incisivos inferiores separados por un espacio, peso corporal +/-7g y antebrazo 32-35mm.")
    print("2. Incisivos superiores (vista oclusa) forman una serie angular, incisivos interiores mucho más largos que los exteriores, incisivos inferiores interiores se tocan, peso corporal +/-11g y antebrazo de 33-38mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Glossophaga comissarisi.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Glossophaga soricina.")
        reinicio()
    elif respuesta == "3":
        preg_murc_29()
    else:
        print("La respuesta no es válida.")
        preg_murc_31()

def preg_murc_32():
    print("Seleccione la opción más acertada:")
    print("1. Partes inferiores del cuerpo amarillas o naranjas, orejas puntiagudas, peso corporal +/-14g y antebrazo de 40-42mm.")
    print("2. Partes inferiores del cuerpo blanquizacas, orejas grandes y redondeadas, calcar (o calcáneo) igual o más corto que el pie, brecha en la faja entre las orejas profunda, peso corporal +/-6g y antebrazo de 33-38mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lampronycteris brachyotis.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Micronycteris minuta.")
        reinicio()
    elif respuesta == "3":
        preg_murc_26()
    else:
        print("La respuesta no es válida.")
        preg_murc_32()

def preg_murc_33():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo casi de 100mm, especie más grande, peso corporal +/-151g y antebrazo de 98-110mm.")
    print("2. Antebrazo -75mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Vampyrum spectrum.")
        reinicio()
    elif respuesta == "2":
        preg_murc_34()
    elif respuesta == "3":
        preg_murc_2()
    else:
        print("La respuesta no es válida.")
        preg_murc_33()

def preg_murc_34():
    print("Dorso:")
    print("1. con por lo menos un rastro de una línea mediana blanca.")
    print("2. sin línea blanca.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_35()
    elif respuesta == "2":
        preg_murc_41()
    elif respuesta == "3":
        preg_murc_33()
    else:
        print("La respuesta no es válida.")
        preg_murc_34()

def preg_murc_35():
    print("Extensión de la línea dorsal:")
    print("1. hasta la corona.")
    print("2. no más alla de la nuca.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_36()
    elif respuesta == "2":
        preg_murc_37()
    elif respuesta == "3":
        preg_murc_34()
    else:
        print("La respuesta no es válida.")
        preg_murc_35()

def preg_murc_36():
    print("Seleccione la opción más acertada:")
    print("1. Puntas de las alas blancas (no siempre), antebrazo amarillo, el murciélago más grande con líneas blancas, peso corporal +/-36g y antebrazo de 47-56mm.")
    print("2. Puntas de las alas no blancas, línea dorsal blanca brillante, membrana interfemoral (MI) angosta, en forma de 'V' y fuertemente orlada, pelos dorsales tricoloridos (la banda basal a veces indistinto) márgenes de las orejas y tragus amarillos o naranjas, de pequeño tamaño, peso corporal +/-17g y antebrazo de 37-41mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Vampyrodes caraccioli.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Platyrrhinus helleri.")
        reinicio()
    elif respuesta == "3":
        preg_murc_35()
    else:
        print("La respuesta no es válida.")
        preg_murc_36()

def preg_murc_37():
    print("Seleccione la opción más acertada:")
    print("1. Hoja de la nariz lateralmente aplanada, cortada, y truncada en la punta, antebrazo y membrana interfemoral (MI) densamente peludos, ojos grandes, líneas faciales raras veces presentes, línea dorsal indistinta, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U', no orlada, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-22g y antebrazo de 42-47mm.")
    print("2. Hoja de la nariz aguda en la punta, antebrazo y membrana interfemoral (MI) poco peludos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Chiroderma villosum.")
        reinicio()
    elif respuesta == "2":
        preg_murc_38()
    elif respuesta == "3":
        preg_murc_35()
    else:
        print("La respuesta no es válida.")
        preg_murc_37()

def preg_murc_38():
    print("Seleccione la opción más acertada:")
    print("1. Pelos dorsales notablemente tri- o tetracoloridos, línea mediana solamente en parte inferior de la espalda, incisivos interiores superiores agudos o desafilados, no truncados.")
    print("2. Pelos dorsales bicoloridos u obscuramente tricoloridos, línea dorsal mediana se extiende hasta la nuca, incisivos interiores superiores truncados y notablemente bilobados.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_39()
    elif respuesta == "2":
        preg_murc_40()
    elif respuesta == "3":
        preg_murc_37()
    else:
        print("La respuesta no es válida.")
        preg_murc_38()

def preg_murc_39():
    print("Seleccione la opción más acertada:")
    print("1. Puntas de los pelos dorsales escarchadas blancas, base gris, pero no muy distinta del amarillo oscuro en el medio, tercer y cuarto diente post-canino inferior (M1 y M2) tienen forma de una vasija, posteriormente sin cúspide, caninos largos y delgados, línea dorsal llega hasta los hombros, normalmente indistinta, márgenes de las orejas y tragus amarillos o naranjas, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, pelos dorsales tricoloridos (banda basal a veces indistinta), peso corporal +/-14g y antebrazo de 35-39mm.")
    print("2. Pelos dorsales sin puntas blancas, base de los pelos dorsales gris oscuros y bien distinguida de la banda mediana amarilla oscura, caninos cortos y gruesos, ojos grandes, líneas faciales anchas, siempre presentes, de un blanco brillante, línea dorsal presente y normalmente brillante, llega hasta los hombros, membrana interfemoral (MI) ancha y en forma de 'U' sin orlas, pelos dorsales tricoloridos, márgenes de las orejas y tragus amarillos o naranjas, peso corporal +/-17g y antebrazo de 38-41mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Vampyressa nymphaea.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Chiroderma trinitatum.")
        reinicio()
    elif respuesta == "3":
        preg_murc_38()
    else:
        print("La respuesta no es válida.")
        preg_murc_39()

def preg_murc_40():
    print("Seleccione la opción más acertada:")
    print("1. Membrana interfemoral (MI), tibia y dedos del pie peludos, líneas faciales y línea mediana dorsal a veces obscuras, brillantes, línea dorsal llega hasta los hombros o a la nuca, ojos pequeños, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 41-45mm.")
    print("2. Extremidades posteriores (membrana del rabo y piernas) prácticamente desnudas, líneas faciales y línea dorsal siempre prominentes, línea dorsal llega hasta los hombros o la nuca, normalmente brillante, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, incisivos interiores superiores truncados, bilobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 40-44mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Uroderma magnirostrum.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Uroderma bilobatum.")
        reinicio()
    elif respuesta == "3":
        preg_murc_38()
    else:
        print("La respuesta no es válida.")
        preg_murc_40()

def preg_murc_41():
    print("Antebrazo:")
    print("1. +50mm.")
    print("2. -50mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_42()
    elif respuesta == "2":
        preg_murc_44()
    elif respuesta == "3":
        preg_murc_34()
    else:
        print("La respuesta no es válida.")
        preg_murc_41()

def preg_murc_42():
    print("Seleccione la opción más acertada:")
    print("1. Extremidades posteriores prácticamente desnudas, líneas faciales indistintas, peso corporal +/-48g y antebrazo de 55-67mm.")
    print("2. Extremidades posteriores peludas, líneas faciales prominentes, membranas de las alas peludas cerca del cuerpo.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Artibeus jamaicensis.")
        reinicio()
    elif respuesta == "2":
        preg_murc_43()
    elif respuesta == "3":
        preg_murc_41()
    else:
        print("La respuesta no es válida.")
        preg_murc_42()

def preg_murc_43():
    print("Seleccione la opción más acertada:")
    print("1. Dos pares de líneas faciales brillantes, peso corporal +/-67g y antebrazo de 69-78mm.")
    print("2. Normalmente solo un par de líneas faciales (sobre los ojos), líneas abajo de los ojos pueden ser presentes, pero indistintas, peso corporal +/-61g y antebrazo de 61-68mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Artibeus lituratus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Artibeus intermedius.")
        reinicio()
    elif respuesta == "3":
        preg_murc_42()
    else:
        print("La respuesta no es válida.")
        preg_murc_43()

def preg_murc_44():
    print("Seleccione la opción más acertada:")
    print("1. Membrana interfemoral (MI) ausente, hombros de color naranja o amarillo, piernas peludas, incisivos inferiores trilobados.")
    print("2. Membrana interfemoral (MI) presente, hombros del mismo color que el resto del dorso.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_45()
    elif respuesta == "2":
        preg_murc_46()
    elif respuesta == "3":
        preg_murc_41()
    else:
        print("La respuesta no es válida.")
        preg_murc_44()

def preg_murc_45():
    print("Seleccione la opción más acertada:")
    print("1. Pelo dorsal de color pálido, líneas de los dientes maxilares arqueadas para afuera (no paralelas), peso corporal +/-15g y antebrazo de 37-42mm.")
    print("2. Pelo dorsal oscuro, líneas de los dientes maxilares casi paralelas, peso corporal +/-20g y antebrazo de 41-45mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Sturnira lilium.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Sturnira luisi.")
        reinicio()
    elif respuesta == "3":
        preg_murc_44()
    else:
        print("La respuesta no es válida.")
        preg_murc_45()

def preg_murc_46():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo normalmente de +35mm, paladar casi circular.")
    print("2. Antebrazo normalmente de -35mm, paladar anteriormente estrechado.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_47()
    elif respuesta == "2":
        preg_murc_50()
    elif respuesta == "3":
        preg_murc_44()
    else:
        print("La respuesta no es válida.")
        preg_murc_46()

def preg_murc_47():
    print("Seleccione la opción más acertada:")
    print("1. Color del pelo chocolate oscuro, membrana interfemoral (MI) notablemente orlada, angosta y en forma de 'V', herradura de la hoja de la nariz ventralmente doblada para abajo, incisivos interiores superiores no bilobados, líneas faciales presentes, amarillas, angostas, líneas medianas dorsales ausentes, incisivos interiores superiores truncados, no lobados, márgenes de las orejas y tragus blancos o de color crema, peso corporal +/-17g y antebrazo de 37-43mm.")
    print("2. Color del pelo gris-chocolate, membrana interfemoral (MI) desnuda o escasamente orlada, ancha y en forma de 'U',  herradura ventralmente libre, incisivos interiores superiores bilobados.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Enchistenes hartii.")
        reinicio()
    elif respuesta == "2":
        preg_murc_48()
    elif respuesta == "3":
        preg_murc_46()
    else:
        print("La respuesta no es válida.")
        preg_murc_47()

def preg_murc_48():
    print("Seleccione la opción más acertada:")
    print("1. Márgenes de las orejas amarillas y amarillas en la base, hoja de la nariz más larga y ancha, M3 ausente, líneas faciales siempre presentes, líneas blancas brillantes y anchas, línea mediana dorsal ausente, incisivos interiores superiores truncados  y bilobados, peso corporal +/-11g, antebrazo de 35-40mm y pelo de 4-6mm.")
    print("2. Márgenes de las orejas no amarillas y de color crema en la base, hoja de la nariz más corta y angosta, M3 presente, líneas faciales siempre presentes, blanchas, angostas y pequeñas, incisivos interiores superiores truncados y bilobados.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Artibeus phaeotis.")
        reinicio()
    elif respuesta == "2":
        preg_murc_49()
    elif respuesta == "3":
        preg_murc_47()
    else:
        print("La respuesta no es válida.")
        preg_murc_48()

def preg_murc_49():
    print("Seleccione la opción más acertada:")
    print("1. Más pequeño, partes inferiores del cuerpo de color más claro y amarillo, frecuentemente tiene líneas faciales blancas bien definidas y prominentes, extremidades posteriores (tibia, pie y membrana interfemoral (MI)) casi desnudas, peso corporal +/-11g, antebrazo de 35-42mm y pelo velludo de 6-7mm.")
    print("2. Más grande, partes inferiores del cuerpo de color más oscuro, gris-chocolate, no siempre tiene líneas faciales bien definidas, extremidades posteriores (tibia, pie y membrana interfemoral (MI)) normalmente peludas, peso corporal +/-13g y antebrazo de 40-45mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Artibeus watsoni.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Artibeus incomitatus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_48()
    else:
        print("La respuesta no es válida.")
        preg_murc_49()

def preg_murc_50():
    print("Seleccione la opción más acertada:")
    print("1. Líneas faciales presentes, blancas y angostas, muy pequeño, calcar (o calcáneo) recto, base de la oreja y hoja de la nariz solamente moderadamente amarillas, línea dorsal ausente, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, márgenes de las orejas y tragus de color amarillo o naranja, pelo dorsal tricolorido (banda basal a veces obscura), peso corporal +/-8g y antebrazo de 29-34mm.")
    print("2. Líneas faciales ausentes, calcar (o calcáneo) recto o falciforme, base de las orejas y hoja de la nariz de color amarillo brillante.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Vampyressa pusilla.")
        reinicio()
    elif respuesta == "2":
        preg_murc_51()
    elif respuesta == "3":
        preg_murc_46()
    else:
        print("La respuesta no es válida.")
        preg_murc_50()

def preg_murc_51():
    print("Seleccione la opción más acertada:")
    print("1. Dorso anterior blanquizco, dorso posterior de color tostado, calcar (o calcáneo) recto, peso corporal +/-5g y antebrazo de 23-31mm.")
    print("2. Dorso anterior amarillo, dorso posterior de color tostado, calcar (o calcáneo) falciforme, líneas faciales y línea dorsal siempre ausentes, membrana interfemoral (MI) ancha y en forma de 'U', sin orlas, márgenes de las orejas y tragus de color amarillo o naranja, peso corporal +/-7g y antebrazo de 29-33mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Ectophylla alba.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Mesophylla macconnelli.")
        reinicio()
    elif respuesta == "3":
        preg_murc_50()
    else:
        print("La respuesta no es válida.")
        preg_murc_51()

def preg_murc_52():
    print("Seleccione la opción más acertada:")
    print("1. Rabo ausente.")
    print("2. Rabo presente.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_53()
    elif respuesta == "2":
        preg_murc_56()
    elif respuesta == "3":
        preg_murc_1()
    else:
        print("La respuesta no es válida.")
        preg_murc_52()

def preg_murc_53():
    print("Seleccione la opción más acertada:")
    print("1. Cara desnuda y grotescamente arrugada, mancha blanca en el hombro, membrana interfemoral (MI) ancha, peluda, en forma de 'U' y fuertemente orlada, líneas siempre ausentes, pelo dorsal tricolorido, cara muy corta básicamente sin rostro, orejas no afiladas, peso corporal +/-20g y antebrazo de 41-45mm.")
    print("2. Cara peluda con ornamentos rudimentarios en la nariz, sin manchas blancas en el hombro, membrana interfemoral (MI) angosta o ausente.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Centurio senex.")
        reinicio()
    elif respuesta == "2":
        preg_murc_54()
    elif respuesta == "3":
        preg_murc_52()
    else:
        print("La respuesta no es válida.")
        preg_murc_53()

def preg_murc_54():
    print("Seleccione la opción más acertada:")
    print("1. Puntas de las alas blancas, peso corporal +/-36g y antebrazo de 48-54mm.")
    print("2. Puntas de las alas no blancas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Desmodus youngii.")
        reinicio()
    elif respuesta == "2":
        preg_murc_55()
    elif respuesta == "3":
        preg_murc_53()
    else:
        print("La respuesta no es válida.")
        preg_murc_54()

def preg_murc_55():
    print("Seleccione la opción más acertada:")
    print("1. Miembro metacarpal del pulgar muy elongado, orejas de tamaño mediano y redondeadas, calcar (o calcáneo) aparentemente ausente, extremidades posteriores con pelos muy cortos, partes inferiores del cuerpo blanquizcas, peso corporal +/-34g y antebrazo de 53-65mm.")
    print("2. Miembro metacarpal del pugar corto, orejas cortas y cuadradas, calcar (o calcáneo) notable, extremidades posteriores densamente peludas, partes inferiores del cuerpo gris chocolate, peso corporal +/-25g y antebrazo de 49-56mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Desmodus rotundus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Diphylla ecaudata.")
        reinicio()
    elif respuesta == "3":
        preg_murc_54()
    else:
        print("La respuesta no es válida.")
        preg_murc_55()

def preg_murc_56():
    print("Seleccione la opción más acertada:")
    print("1. Rabo se extiende hasta o más allá del margen de la membrana interfemoral (MI).")
    print("2. Rabo no llega gasta el margen de la membrana interfemoral (MI).")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_57()
    elif respuesta == "2":
        preg_murc_82()
    elif respuesta == "3":
        preg_murc_52()
    else:
        print("La respuesta no es válida.")
        preg_murc_56()

def preg_murc_57():
    print("Seleccione la opción más acertada:")
    print("1. Rabo llega gasta el margen de la membrana interfemoral (MI) o se extiende solamente una o dos vértebras más allá.")
    print("2. Rabo se extiende mucho más allá del margen de la membrana interfemoral (MI).")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_58()
    elif respuesta == "2":
        preg_murc_69()
    elif respuesta == "3":
        preg_murc_56()
    else:
        print("La respuesta no es válida.")
        preg_murc_57()

def preg_murc_58():
    print("Membrana interfemoral (MI):")
    print("1. Extensivamente peluda.")
    print("2. Casi desnuda.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_59()
    elif respuesta == "2":
        preg_murc_62()
    elif respuesta == "3":
        preg_murc_57()
    else:
        print("La respuesta no es válida.")
        preg_murc_58()

def preg_murc_59():
    print("Seleccione la opción más acertada:")
    print("1. De color amarillo, alas negras, peso corporal +/-11g y antebrazo de 43-47mm.")
    print("2. De color rojizo.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lasiurus ega.")
        reinicio()
    elif respuesta == "2":
        preg_murc_60()
    elif respuesta == "3":
        preg_murc_58()
    else:
        print("La respuesta no es válida.")
        preg_murc_59()

def preg_murc_60():
    print("Seleccione la opción más acertada:")
    print("1. Dorso y partes inferiores del cuerpo rojos, peso corporal +/-20g y antebrazo +/-50mm.")
    print("2. Partes inferiores del cuerpo de color amarillo o negruzco.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lasiurus egregius.")
        reinicio()
    elif respuesta == "2":
        preg_murc_61()
    elif respuesta == "3":
        preg_murc_59()
    else:
        print("La respuesta no es válida.")
        preg_murc_60()

def preg_murc_61():
    print("Seleccione la opción más acertada:")
    print("1. Partes inferiores del cuerpo amarillas, dorso rojizo-naranja, banda mediana de los pelos dorsales es pálida y ancha, peso corporal +/-8g y antebrazo de 38-42mm.")
    print("2. Partes inferiores del cuerpo negruzcas, dorso marrón, banda mediana de los pelos dorsales es pálida y angostas, peso corporal +/-13g y antebrazo de 43-46mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Lasiurus blossevillii.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Lasiurus castaneus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_60()
    else:
        print("La respuesta no es válida.")
        preg_murc_61()

def preg_murc_62():
    print("Seleccione la opción más acertada:")
    print("1. Piernas muy largas, membrana del ala muy grande y conectada muy arriba en la tibia, peso corporal +/-6g y antebrazo de 36-39mm.")
    print("2. Piernas cortas, membrana del ala conectada al lado del pie.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Natalus stramineus.")
        reinicio()
    elif respuesta == "2":
        preg_murc_63()
    elif respuesta == "3":
        preg_murc_58()
    else:
        print("La respuesta no es válida.")
        preg_murc_62()

def preg_murc_63():
    print("El primer diente post-canino alto en la parte superior está:")
    print("1. Adyacente al canino.")
    print("2. Separado del canino por dientes pqueños y bajos.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_64()
    elif respuesta == "2":
        preg_murc_67()
    elif respuesta == "3":
        preg_murc_62()
    else:
        print("La respuesta no es válida.")
        preg_murc_63()

def preg_murc_64():
    print("Seleccione la opción más acertada:")
    print("1. Bases del pelo dorsal pálido, amarillo, amarillo oscuro, peso corporal +/-5g y antebrazo de 27-31mm.")
    print("2. Bases del pelo dorsal fusco oscuro.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Rhogeessa tumida.")
        reinicio()
    elif respuesta == "2":
        preg_murc_65()
    elif respuesta == "3":
        preg_murc_63()
    else:
        print("La respuesta no es válida.")
        preg_murc_64()    

def preg_murc_65():
    print("Seleccione la opción más acertada:")
    print("1. Pequeño, pelo corto, peso corporal +/-7g y antebrazo de 37-43mm.")
    print("2. Tamaño mediano a grande, pelo largo, antebrazo +40mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Eptesicus furinalis.")
        reinicio()
    elif respuesta == "2":
        preg_murc_66()
    elif respuesta == "3":
        preg_murc_64()
    else:
        print("La respuesta no es válida.")
        preg_murc_65()

def preg_murc_66():
    print("Seleccione la opción más acertada:")
    print("1. Tamaño mediano, negruzco, peso corporal +/-10g y antebrazo de 42-47mm.")
    print("2. Grande, de color chocolate oscuro, peso corporal +/-13g y antebrazo de 46-54mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Eptesicus brasiliensis.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Eptesicus fuscus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_65()
    else:
        print("La respuesta no es válida.")
        preg_murc_66()

def preg_murc_67():
    print("Seleccione la opción más acertada:")
    print("1. Partes inferiores del cuerpo blanquizcas, dorso negruzco con puntas pálidas, pies más grandes, peso corporal +/-7g y antebrazo de 33-38mm.")
    print("2. Partes inferiores del cuerpo amarillas o chocolates, dorso sin puntas pálidas, pies pequeños.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Myotis albescens.")
        reinicio()
    elif respuesta == "2":
        preg_murc_68()
    elif respuesta == "3":
        preg_murc_63()
    else:
        print("La respuesta no es válida.")
        preg_murc_67()

def preg_murc_68():
    print("Seleccione la opción más acertada:")
    print("1. Pelo dorsal lanoso, peso corporal +/-5g y antebrazo de 32-38mm.")
    print("2. Pelo dorsal liso, peso corporal +/-4g y antebrazo de 33-38mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Myotis riparius.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Myotis nigricans.")
        reinicio()
    elif respuesta == "3":
        preg_murc_67()
    else:
        print("La respuesta no es válida.")
        preg_murc_68()

def preg_murc_69():
    print("Discos de succión en el pulgar y los pies:")
    print("1. Presentes.")
    print("2. Ausentes.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_70()
    elif respuesta == "2":
        preg_murc_71()
    elif respuesta == "3":
        preg_murc_57()
    else:
        print("La respuesta no es válida.")
        preg_murc_69()

def preg_murc_70():
    print("Seleccione la opción más acertada:")
    print("1. Partes inferiores del cuerpo blancas o amarillas pálidas, rabo se extiende 5-8mm más allá de la membrana interfemoral (MI), membrana interfemoral (MI) casi desnuda, calcar (o calcáneo) normalmente con dos proyecciones membranosas extendiendo hasta el margen posterolateral de la membrana interfemoral (MI), peso corporal +/-4g y antebrazo de 34-38mm.")
    print("2. Partes inferiores del cuerpo chocolates o naranja-chocolates, rabo se extiende 2-4mm más allá de la membrana interfemoral (MI), membrana interfemoral (MI) con pelos largos (4mm) escasamente distribuidos, pelos finos, calcar (o calcáneo) con una proyección membranosa extendiendo hasta el margen posterolateral de la membrana interfemoral (MI), peso corporal +/-3g y antebrazo de 30-35mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Thyroptera tricolor.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Thyroptera discifera.")
        reinicio()
    elif respuesta == "3":
        preg_murc_69()
    else:
        print("La respuesta no es válida.")
        preg_murc_70()

def preg_murc_71():
    print("Antitragus:")
    print("1. Petiolado (casi circular, pellizcado en la base).")
    print("2. Más ancho en la base.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_72()
    elif respuesta == "2":
        preg_murc_76()
    elif respuesta == "3":
        preg_murc_69()
    else:
        print("La respuesta no es válida.")
        preg_murc_71()   

def preg_murc_72():
    print("Seleccione la opción más acertada:")
    print("1. Pelos en cadera de 3-6mm y antebrazo +/-50mm.")
    print("2. Pelos en cadera de 1-2mm y antebrazo -45mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_73()
    elif respuesta == "2":
        preg_murc_75()
    elif respuesta == "3":
        preg_murc_71()
    else:
        print("La respuesta no es válida.")
        preg_murc_72()

def preg_murc_73():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo desnudo, incisivos interiores superiores sobresalientes, peso corporal +/-21g y antebrazo de 48-56mm.")
    print("2. Antebrazo peludo, incisivos interiores superiores no sobresalen.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Promops centralis.")
        reinicio()
    elif respuesta == "2":
        preg_murc_74()
    elif respuesta == "3":
        preg_murc_72()
    else:
        print("La respuesta no es válida.")
        preg_murc_73()

def preg_murc_74():
    print("Seleccione la opción más acertada:")
    print("1. Pelos dorsales con bases de color blanco o gris contrastante, peso corporal +/-27g y antebrazo de 45-52mm.")
    print("2. Pelos dorsales con poco contraste entre las puntas y las bases, peso corporal +/-32g y antebrazo de 46-51mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Molossus sinaloae.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Molossus ater.")
        reinicio()
    elif respuesta == "3":
        preg_murc_73()
    else:
        print("La respuesta no es válida.")
        preg_murc_74()

def preg_murc_75():
    print("Seleccione la opción más acertada:")
    print("1. Pelo +/-3mm en el centro de la espalda, banda basal de los pelos dorsales es pálida, peso corporal +/-12g y antebrazo de 36-40mm.")
    print("2. Pelo +/-2mm en el centro de la espalda, poco o ningún contraste entre las puntas y las bases de los pelos dorsales, peso corporal +/-22g y antebrazo de 38-43mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Molossus molossus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Molossus bondae.")
        reinicio()
    elif respuesta == "3":
        preg_murc_72()
    else:
        print("La respuesta no es válida.")
        preg_murc_75()

def preg_murc_76():
    print("Seleccione la opción más acertada:")
    print("1. Orejas grandes, conectadas en la frente, hocico no hinchado e inflado.")
    print("2. Orejas de tamaño moderado, no conectadas en la frente, hocico hinchado e inflado.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_77()
    elif respuesta == "2":
        preg_murc_81()
    elif respuesta == "3":
        preg_murc_71()
    else:
        print("La respuesta no es válida.")
        preg_murc_76()

def preg_murc_77():
    print("Seleccione la opción más acertada:")
    print("1. Labios superiores grandes, sueltos y muy arrugados, peso corporal +/-10g y antebrazo de 36-46mm.")
    print("2. Labios superiores normales.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Tadarida brasiliensis.")
        reinicio()
    elif respuesta == "2":
        preg_murc_78()
    elif respuesta == "3":
        preg_murc_76()
    else:
        print("La respuesta no es válida.")
        preg_murc_77()

def preg_murc_78():
    print("Antebrazo:")
    print("1. +50mm.")
    print("2. -40mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_79()
    elif respuesta == "2":
        preg_murc_80()
    elif respuesta == "3":
        preg_murc_77()
    else:
        print("La respuesta no es válida.")
        preg_murc_78()

def preg_murc_79():
    print("Seleccione la opción más acertada:")
    print("1. Tragus relativamente pequeño, agudo, pliegue anterior basal de la oreja -15mm, color en el dorso negruzco, peso corporal +/-33g y antebrazo de 66-74mm.")
    print("2. Tragus relativamente grande, truncado, pliegue anterior basal de la oreja +15mm, color en el dorso gris chocolate, peso corporal +/-38g y antebrazo de 55-63mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Eumops auripendulus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Eumops glaucinus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_78()
    else:
        print("La respuesta no es válida.")
        preg_murc_79()

def preg_murc_80():
    print("Seleccione la opción más acertada:")
    print("1. Pelo dorsal corto (2mm) y terciopelado, peso corporal +/-18g y antebrazo de 36-42mm.")
    print("2. Pelo dorsal largo (6mm) y suelto, peso corporal +/-10g y antebrazo de 38-49mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Eumops hansae.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Eumops bonariensis.")
        reinicio()
    elif respuesta == "3":
        preg_murc_78()
    else:
        print("La respuesta no es válida.")
        preg_murc_80()

def preg_murc_81():
    print("Seleccione la opción más acertada:")
    print("1. Pequeño, pecho blanquizco, peso corporal +/-13g y antebrazo de 31-36mm.")
    print("2. Grande, color del pecho no diferenciado, negruzco o chocolate, peso corporal +/-20g y antebrazo de 34-38mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Molossops paranus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Molossops greenhalli.")
        reinicio()
    elif respuesta == "3":
        preg_murc_76()
    else:
        print("La respuesta no es válida.")
        preg_murc_81()            

def preg_murc_82():
    print("Seleccione la opción más acertada:")
    print("1. De color blanco o blanquizco, membranas pálidas, peso corporal +/-16g y antebrazo de 64-66mm.")
    print("2. De color negruzco, chocolate o naranja, membranas negruzcas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Diclidurus albus.")
        reinicio()
    elif respuesta == "2":
        preg_murc_83()
    elif respuesta == "3":
        preg_murc_56()
    else:
        print("La respuesta no es válida.")
        preg_murc_82()

def preg_murc_83():
    print("Seleccione la opción más acertada:")
    print("1. Dos líneas blanquizcas longitudinales en dorso.")
    print("2. Una o ninguna línea longitudinal en dorso.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_84()
    elif respuesta == "2":
        preg_murc_86()
    elif respuesta == "3":
        preg_murc_82()
    else:
        print("La respuesta no es válida.")
        preg_murc_83()

def preg_murc_84():
    print("Seleccione la opción más acertada:")
    print("1. Grande, de color negruzco, con saco glandular, peso corporal +/-6g y antebrazo de 40-49mm.")
    print("2. Pequeño, de color gris o chocolate y antebrazo -45mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Saccopteryx bilineata.")
        reinicio()
    elif respuesta == "2":
        preg_murc_85()
    elif respuesta == "3":
        preg_murc_83()
    else:
        print("La respuesta no es válida.")
        preg_murc_84()

def preg_murc_85():
    print("Seleccione la opción más acertada:")
    print("1. Antebrazo desnudo, saco glandular en membrana antebrachial, peso corporal +/-4g y antebrazo de 36-43mm.")
    print("2. Antebrazo con mechones de pelo aislados, sin saco glandular en el ala, peso corporal +/-3g y antebrazo de 34-41mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Saccopteryx leptura.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Rhynchonycteris naso.")
        reinicio()
    elif respuesta == "3":
        preg_murc_84()
    else:
        print("La respuesta no es válida.")
        preg_murc_85()

def preg_murc_86():
    print("Seleccione la opción más acertada:")
    print("1. Con una línea mediana dorsal de color blanquizco o amarillo, labio leporino (hendido).")
    print("2. Dorso sin líneas, labio superior normal.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_87()
    elif respuesta == "2":
        preg_murc_88()
    elif respuesta == "3":
        preg_murc_83()
    else:
        print("La respuesta no es válida.")
        preg_murc_86()

def preg_murc_87():
    print("Seleccione la opción más acertada:")
    print("1. Pequeño, pies posteriores de -21mm, garras no excesivamente grandes, peso corporal +/-30g y antebrazo de 55-59mm.")
    print("2. Grande, pies posteriores excepcionalmente grandes (+25mm), garras excesivamente grandes, peso corporal +/-55g y antebrazo de 81-89mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Noctilio albiventris.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Noctilio leporinus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_86()
    else:
        print("La respuesta no es válida.")
        preg_murc_87()

def preg_murc_88():
    print("Seleccione la opción más acertada:")
    print("1. Saco en forma de bolsillo en membrana antebrachial en los machos.")
    print("2. Sin saco glandular en las alas.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_89()
    elif respuesta == "2":
        preg_murc_91()
    elif respuesta == "3":
        preg_murc_86()
    else:
        print("La respuesta no es válida.")
        preg_murc_88()

def preg_murc_89():
    print("Seleccione la opción más acertada:")
    print("1. Ala conectada cerca de la base de los dedos del pie, saco cerca de antebrazo, peso corporal +/-9g y antebrazo de 45-48mm.")
    print("2. Ala conectada al tobillo, saco en el margen mediano o anterior de la membrana.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Cormura brevirostris.")
        reinicio()
    elif respuesta == "2":
        preg_murc_90()
    elif respuesta == "3":
        preg_murc_88()
    else:
        print("La respuesta no es válida.")
        preg_murc_89()

def preg_murc_90():
    print("Seleccione la opción más acertada:")
    print("1. Grande, peso corporal +/-7g y antebrazo de 44-54mm.")
    print("2. Pequeño, peso corporal +/-5g y antebrazo de 37-44mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Peropteryx kappleri.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Peropteryx microtis.")
        reinicio()
    elif respuesta == "3":
        preg_murc_89()
    else:
        print("La respuesta no es válida.")
        preg_murc_90()

def preg_murc_91():
    print("Seleccione la opción más acertada:")
    print("1. Orejas cortas, redondeadas, formando un túnel, pelo gris, pulgares rojos, peso corporal +/-3g y antebrazo de 34-36mm.")
    print("2. Orejas de tamaño moderado, no forman un túnel, pelo chocolate, naranja o gris-chocolate, antebrazo +44mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Furipterus horrens.")
        reinicio()
    elif respuesta == "2":
        preg_murc_92()
    elif respuesta == "3":
        preg_murc_88()
    else:
        print("La respuesta no es válida.")
        preg_murc_91()

def preg_murc_92():
    print("Seleccione la opción más acertada:")
    print("1. Membranas de las alas conectadas cerca de los dedos del pie, pelo largo (9mm en la cadera) y tosco, peso corporal +/-5g y antebrazo de 42-45mm.")
    print("2. Membranas de las alas conectadas a los tobillos o en la tibia, pelo corto (5mm en la cadera) y no tosco.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Centronycteris maximiliani.")
        reinicio()
    elif respuesta == "2":
        preg_murc_93()
    elif respuesta == "3":
        preg_murc_91()
    else:
        print("La respuesta no es válida.")
        preg_murc_92()

def preg_murc_93():
    print("Alas se conectan en:")
    print("1. La espalda (en la línea mediana dorsal), dando la apariencia de una espalda desnuda.")
    print("2. Los lados del cuerpo, solamente un poco más arriba de lo normal.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        preg_murc_94()
    elif respuesta == "2":
        preg_murc_95()
    elif respuesta == "3":
        preg_murc_92()
    else:
        print("La respuesta no es válida.")
        preg_murc_93()

def preg_murc_94():
    print("Alas se conectan en:")
    print("1. Grande, platopatagio cubierto con muchos pelos cortos, peso corporal +/-15g y antebrazo de 49-56mm.")
    print("2. Pequeño, platopatagio escasa e irregularmente cubierto con pelos largos, peso corporal +/-7g y antebrazo de 40-50mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Pteronotus gymnonotus.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Pteronotus davyi.")
        reinicio()
    elif respuesta == "3":
        preg_murc_93()
    else:
        print("La respuesta no es válida.")
        preg_murc_94()

def preg_murc_95():
    print("Alas se conectan en:")
    print("1. Grande, peso corporal +/-23g y antebrazo de 49-65mm.")
    print("2. Pequeño, peso corporal +/-8g y antebrazo de 40-47mm.")
    print("3. Volver.")
    respuesta = input()
    if respuesta == "1":
        print("Su murciélago es Pteronotus parnellii.")
        reinicio()
    elif respuesta == "2":
        print("Su murciélago es Pteronotus personatus.")
        reinicio()
    elif respuesta == "3":
        preg_murc_93()
    else:
        print("La respuesta no es válida.")
        preg_murc_95()

def reinicio():
    print("¿Volver a empezar?")
    print("1. Sí.")
    print("2. No.")
    respuesta = input()
    if respuesta == "1":
        inicio()
    elif respuesta == "2":
        print("Hasta luego.")
    else:
        print("La respuesta no es válida.")
        reinicio()

inicio()