def time_to_text(minutes):
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        temps = (f"{minutes_restantes} minutes")

    elif minutes_restantes == 0:
    
        temps = (f"{heures} heures")

    else:
        temps = (f"{heures} heures et {minutes_restantes} minutes")

    print(temps)

time_to_text(135)