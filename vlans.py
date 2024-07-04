def verificar_tipo_vlan(vlan):
    if 0 <= vlan <= 99:
        return "VLAN simple"
    elif 100 <= vlan <= 199:
        return "VLAN extendida"
    else:
        return "Fuera de rango"

# Solicitar al usuario que ingrese una VLAN
vlan = int(input("Ingresa el número de VLAN: "))

# Verificar y mostrar el tipo de VLAN
tipo_vlan = verificar_tipo_vlan(vlan)
print(f"La VLAN {vlan} es {tipo_vlan}")
