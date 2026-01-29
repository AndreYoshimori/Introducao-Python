# Programa 9.14: Mostra a data atual em diversos fusos horários

from zoneinfo import ZoneInfo
from datetime import datetime


bruxelas = ZoneInfo("Europe/Brussels")
nova_iorque = ZoneInfo("America/New_York")
tokio = ZoneInfo("Japan")
manaus = ZoneInfo("America/Manaus")
brasilia = ZoneInfo("Brazil/East")
rio_branco = ZoneInfo("America/Rio_Branco")

agora = datetime.now()

print("Agora em:")
print(f"Bruxelas    {agora.astimezone(bruxelas)}")
print(f"Nova Iorque    {agora.astimezone(nova_iorque)}")
print(f"Tokio    {agora.astimezone(tokio)}")

print("Agora no Brasil:")
print(f"Rio Branco    {agora.astimezone(rio_branco)}")
print(f"Manaus    {agora.astimezone(manaus)}")
print(f"Brasília    {agora.astimezone(brasilia)}")
