import re

texto = "En el año 2025, 12 estudiantes viajan juntos. ¡Hola! ¿Te gusta aprender? El cielo despejado, las estrellas (★) brillan. 8 niños juegan, 7.80 horas de estudio. Lista: libro, lápiz, mochila. El costo es $35.40. ¿Sabías que el código #7788 es importante? La vida es conocimiento, @todos colaboran. El tiempo avanza, 9 días de clase. ¡Éxito! El número especial es 202. ¿Qué harías con 22.15 pesos? La respuesta está en la lista: leer, escribir, pensar. ¡Sigue aprendiendo! 100 palabras, 9 enteros, 3 decimales, 2 listas."


patron1 = r"(?<![\d.])\d+(?![\d.])" 
patron2 = r"-?\d+\.\d+"         
patron3 = r"\b(True|False)\b"        
patron4 = r'"(.*?)"'                 

# listas
patron5_brackets = r"\[\s*([^\]]+?)\s*\]"
patron5_labels = r"(?i)(?:\bLista:|\bLa respuesta está en la lista:)\s*([A-Za-zÁÉÍÓÚáéíóúÜüÑñ0-9@\#★\s,]+?)(?=(?:[.\n]|$))"

patron_palabras = r"(?:@|#)?[A-Za-zÁÉÍÓÚáéíóúÜüÑñ0-9★]+(?:\.[0-9]+)?"

def analizar(texto_a):
    enteros = re.findall(patron1, texto_a)
    flotantes = re.findall(patron2, texto_a)
    booleans = re.findall(patron3, texto_a, re.IGNORECASE)
    strings = re.findall(patron4, texto_a)
    listas_br = re.findall(patron5_brackets, texto_a)
    listas_lab = re.findall(patron5_labels, texto_a)

    listas = []
    for s in listas_br:
        listas.append(s.strip())
    for s in listas_lab:
        listas.append(s.strip().rstrip("."))

    palabras = re.findall(patron_palabras, texto_a)

    return {
        "palabras_count": len(palabras),
        "enteros": enteros,
        "n_enteros": len(enteros),
        "flotantes": flotantes,
        "n_flotantes": len(flotantes),
        "booleans": booleans,
        "n_booleans": len(booleans),
        "strings": strings,
        "n_strings": len(strings),
        "listas": listas,
        "n_listas": len(listas),
    }
    
if texto.strip():
    res = analizar(texto)
    print("\n--- RESULTADOS ---")
    print("Palabras encontradas:", res["palabras_count"])
    print("Enteros:", res["enteros"], "->", res["n_enteros"])
    print("Decimales:", res["flotantes"], "->", res["n_flotantes"])
    print("Listas:", res["listas"], "->", res["n_listas"])

try:
    texto1 = input("\nIngrese su texto: ")
except EOFError:
    texto1 = ""

if texto1.strip():
    res1 = analizar(texto1)
    print("\n--- RESULTADOS ---")
    print("Palabras encontradas:", res1["palabras_count"])
    print("Enteros:", res1["enteros"], "->", res1["n_enteros"])
    print("Decimales:", res1["flotantes"], "->", res1["n_flotantes"])
    print("Listas:", res1["listas"], "->", res1["n_listas"])
