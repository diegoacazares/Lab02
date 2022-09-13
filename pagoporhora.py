# Tendencias e Innovacion en Tecnología Agrícola
#
horas=input("Horas trabajadas? =")
valorPorHora=input("Valor por hora? =")

#se utilizala conversión tipo a int
#sino se hace la conversión existira error porque trata de multiplicar strings
total=int(horas)*int(valorPorHora)

print(total)