cd_mrs_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
}
mrs_cd_dict = {v: k for k, v in cd_mrs_dict.items()}

print("¿Qué desea hacer?")
print("1. Traducir de código Morse a texto")
print("2. Traducir de texto a código Morse")
opcion = input("Ingrese el número de la opción deseada: ")

if opcion == '1':
    morse = input("Ingrese el mensaje en código Morse: ")
    signos = morse.split(' ')
    texto_traducido = ''
    for word in signos:
        if word in mrs_cd_dict:  
            letra = mrs_cd_dict[word]
            texto_traducido += letra
        else:
            texto_traducido += ''  
    print("Texto traducido desde código Morse:", texto_traducido)
elif opcion == '2':
    texto = input("Ingrese el mensaje de texto: ")
    codigo_morse = ''
    for char in texto:
        if char.lower() in cd_mrs_dict:
            codigo_morse += cd_mrs_dict[char.lower()] + ' '
        elif char == ' ':
            codigo_morse += ' '
        else:
            codigo_morse += '?'
    print("Código Morse traducido desde texto:", codigo_morse.strip())

else:
    print("Opción no válida. Por favor, ingrese 1 o 2.")
