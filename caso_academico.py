print("*************")
print("\t SISTEMAS DE NOTAS")
print("*************")
suma_notas=0
cantidad_materias=0
nota_max=-1
nota_min=21
materia_mayor=""
materia_menor=""
reporte_notas=""
continuar="s"
while continuar.lower()=="s":
    print("Materias",(cantidad_materias+1))
    materia=input("Ingresar nombre de materia: ")
    nota=float(input("Ingresar nota[0-20]:"))
    if nota<0 or nota>20 or materia=="":
        print("ERROR: La nota debe estar entre 0 y 20, y la materiano puede ser vacia....")
    else:
        suma_notas+=nota
        cantidad_materias=cantidad_materias+1
        reporte_notas=reporte_notas+f"*{materia}:{nota}\n"
        if nota>nota_max:
            nota_max=nota
            materia_mayor=materia
        if nota<nota_min:
            nota_min=nota
            materia_menor=materia
        print("Materia registrada exitosamente..!!")
    continuar=input("¿Desea continuar?..(s/n)")
print("*************")
print("\t\tBOLETIN DE NOTAS")
print("*************")
if cantidad_materias>0:
    promedio=suma_notas/cantidad_materias
    print("Reporte de notas",reporte_notas)
    print("Materias Evaluadas: ",cantidad_materias)
    print("Promedio General: ", promedio)
    print("Nota Maxima: ",materia_mayor,"",nota_max)
    print("Nota Minima: ",materia_menor,"",nota_min)
    if promedio>=13:
        print("condicion academica: APROBADO")
    elif promedio>=10.5:
        print("condicion academica: RECUPERACION")
    else:
        print("condicion academica: DESAPROBADO")
else:
    print("no registro materia")