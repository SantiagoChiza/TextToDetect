import re

texto = "Ciao! Nel 2025, 11 studenti viaggiano insieme. Lista: libro, penna, zaino. Il prezzo è €29,50. Le stelle (★) brillano sopra la scuola. 5 gatti saltano, 4 cani giocano. Il codice #1133 è speciale. 8 giorni di lezione, 4 di riposo. @tutti collaborano. Il numero magico è 232. Cosa faresti con 19,90€? La risposta è nella lista: studiare, insegnare, sognare. Impara ogni giorno! 100 parole, 8 interi, 3 decimali, 2 listas."

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
