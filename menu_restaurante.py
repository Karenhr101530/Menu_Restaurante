# Problema 2: Gestión de Precios de Menú de Restaurante
# Autor : Karen Hernández Restrepo 
# Fundamentos de Programacion 
# Mayo del 2026

# --- Módulo: función para calcular el precio final -----------
def calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral):
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral:
        return precio_base * 0.85
    return precio_base

# --- Programa principal --------------------------------------
def main():

    # Matriz del menú: [Nombre, Categoría, Precio Base]
    menu = [
        ["Bandeja Paisa",     "Plato Fuerte", 32000],
        ["Limonada de Coco",  "Bebida",       12000],
        ["Lomo al Trapo",     "Plato Fuerte", 55000],
        ["Ensalada César",    "Entrada",      18000],
        ["Cerveza Artesanal", "Bebida",       15000],
        ["Churrasco",         "Plato Fuerte", 48000],
        ["Tiramisú",          "Postre",       16000],
        ["Agua Mineral",      "Bebida",        6000],
    ]

    categoria_objetivo = "Plato Fuerte"
    umbral = 30000

    # Recorrer la matriz y mostrar resultados
    for producto in menu:
        nombre      = producto[0]
        categoria   = producto[1]
        precio_base = producto[2]

        precio_final = calcular_precio_final(
            precio_base, categoria, categoria_objetivo, umbral
        )

        print(f"{nombre:<22} {categoria:<14} ${precio_base:>10,} ${precio_final:>10,.0f}")

main()