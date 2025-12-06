salario_base = float(input("Ingrese salario base: "))
horas_extras = float(input("Ingrese horas extras: "))
pago_hora_extra = float(input("Ingrese pago por hora extra: "))
bono = float(input("Ingrese bono: "))
afp = float(input("Ingrese porcentaje AFP: "))
salud = float(input("Ingrese porcentaje Salud: "))

salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono

descuento_afp = salario_base * (afp / 100)
descuento_salud = salario_base * (salud / 100)
descuentos_totales = descuento_afp + descuento_salud

salario_neto = salario_bruto - descuentos_totales

print("Salario Bruto:", salario_bruto)
print("Descuentos Totales:", descuentos_totales)
print("Salario Neto:", salario_neto)