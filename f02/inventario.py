maquina = {
    "hostname": "PC-ciaomah",
    "sistema": "Ubuntu 22.04",
    "cpu_nucleos": 4,
    "atualizada": False
}

print("--- Ficha da Máquina Inicial ---")
print(f"Hostname: {maquina['hostname']}")
print(f"Sistema: {maquina['sistema']}")
print(f"CPU (núcleos): {maquina['cpu_nucleos']}")
print(f"Atualizada: {maquina['atualizada']}")
print("\n=======================================")

maquina["atualizada"] = True

maquina["ultima_verificacao"] = "17/06/2026"

print("\n--- Ficha da Máquina Atualizada ---")
print(f"Hostname: {maquina['hostname']}")
print(f"Sistema: {maquina['sistema']}")
print(f"CPU (núcleos) {maquina['cpu_nucleos']}")
print(f"Atualizada: {maquina['atualizada']}")
print(f"Última verificacao: {maquina['ultima_verificacao']}")
print("\n========================================")
