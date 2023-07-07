try:
    horas = int(input("Introduzca por favor el número de horas: "))
    tarifa = float(input("Cual es la tarifa por hora: "))

    if horas >= 45:
        horas_extras = horas - 40
        salario_bruto = 40 * tarifa
        tarifa_horas_extras = tarifa * 1.5
        salario_horas_extras = tarifa_horas_extras * horas_extras
        salario_total = salario_bruto + salario_horas_extras
        print("El total es: Lps", salario_total)
    else:
        salario_bruto = horas * tarifa
        print("El total es: Lps", salario_bruto)

except ValueError:
    print("Error, por favor introduzca un número")
