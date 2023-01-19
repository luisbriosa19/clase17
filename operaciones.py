from datetime import datetime

ahora = datetime.now()

fin_del_2023 = datetime(2023, 12, 31)

tiempo_falta = fin_del_2023 - ahora

print(tiempo_falta.days)

