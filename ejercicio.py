import math
datos = [15, 14, 10, 23, 18, 14, 11, 10, 15, 9, 18, 18, 13, 10, 8, 19, 17, 16, 13, 20, 17, 14, 12, 11, 11, 9, 12, 19, 14, 9]
valorMayor = datos[0];
valorMenor = datos[0];
for d in datos:
    if (d > valorMayor):
        valorMayor = d
    if (d < valorMenor):
        valorMenor = d
rango = valorMayor - valorMenor
# K = numero de clases
k = round(1 + (3.322 * math.log10(len(datos))))
amplitudClase = math.ceil(rango / k)
fronteras = {}
for i in range(k):
    fronteras[f"frontera{i + 1}"] = []

frontera = valorMenor
for i in fronteras.values():
    i.append(frontera)
    frontera += amplitudClase
    i.append(frontera)

frecuencia = 0
for f in fronteras.values():
    for d in datos:
        if (f[0] <= d and d < f[1]):
            frecuencia += 1
    f.append(frecuencia)
    frecuencia = 0

for f in fronteras.values():
    marcaClase = (f[0] + f[1]) / 2
    f.append(marcaClase)

contador = 1
for f in fronteras.values():
    print(f'Frontera {contador}: {f[0]} - {f[1]}, frecuencia: {f[2]}, marca de clase: {f[3]}')
    contador += 1
