ingreso_mensual = float(input("Ingrese el ingreso mensual: "))
ingreso_anual = ingreso_mensual * 14

impuesto_tramo_1 = 0.0
impuesto_tramo_2 = 0.0
impuesto_tramo_3 = 0.0
impuesto_tramo_4 = 0.0

if ingreso_anual > 20000:
    monto_tramo_2 = ingreso_anual - 20000
    if monto_tramo_2 > 30000:
        monto_tramo_2 = 30000
    impuesto_tramo_2 = monto_tramo_2 * 0.10

if ingreso_anual > 50000:
    monto_tramo_3 = ingreso_anual - 50000
    if monto_tramo_3 > 50000:
        monto_tramo_3 = 50000
    impuesto_tramo_3 = monto_tramo_3 * 0.20

if ingreso_anual > 100000:
    monto_tramo_4 = ingreso_anual - 100000
    impuesto_tramo_4 = monto_tramo_4 * 0.30

impuesto_total = impuesto_tramo_1 + impuesto_tramo_2 + impuesto_tramo_3 + impuesto_tramo_4

if ingreso_anual > 0:
    tasa_efectiva = (impuesto_total / ingreso_anual) * 100
else:
    tasa_efectiva = 0

print(f"Ingreso Anual: {ingreso_anual}")
print(f"Impuesto tramo 1 [0-20000]: {impuesto_tramo_1}")
print(f"Impuesto tramo 2 [20000-50000]: {impuesto_tramo_2}")
print(f"Impuesto tramo 3 [50000-100000]: {impuesto_tramo_3}")
print(f"Impuesto tramo 4 [>100000]: {impuesto_tramo_4}")
print(f"Total de impuestos: {impuesto_total}")
print(f"Tasa efectiva real: {tasa_efectiva}%")