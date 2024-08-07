def ContarLasVocales (frase):
    vocal = "aeiouAEIOU"
    contar = 0
    for letras in frase:
        if letras in vocal:
            contar += 1
    return contar 

frase = input("ingrese su frase: ")
NumVocal = ContarLasVocales(frase)
print(f"Su frase {frase} contiene {NumVocal} vocales")