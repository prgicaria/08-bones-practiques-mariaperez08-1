#!/usr/bin/env python"
'''bones_practiques.py. Programa de Divisió
Instiitut Icària
Programació - 1r de Batxillerat - Curs 24/25
Calcula la divisió entre un divident i divisor, que mostra per pantalla la
divisió, el quocient i el residu. '''

__author__ = "Maria Perez"
__email__ = "mperez2@instituticaria.cat"
__date__ = "2024/10/23"

divident = int(input("introdueix el teu divient(nombre enter)"))
divisor = int(input("introdueix el teu divisor(nombre enter)"))
quocient = divident // divisor
residu = divident - quocient * divisor
print(f"Divisió: {divident}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
