import os
import datetime

nome = os.environ.get("OPERADOR", "recruta")
print(f"[{datetime.date.today()}] - Sistema no ar, {nome}!")
print("Empacotado com Dockerfile. Fase 4 dominada até aqui. xD ")
