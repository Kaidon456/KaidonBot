from discordrp import Presence
import time
import json

# Importar ID de la aplicacion
with open("./tokens.json") as file:
    data = json.load(file)

#Inicializacion de presence
with Presence(data.get("APP_ID")) as presence:
    print("Connected")
    presence.set(
        {
            "state": "Se parte de la Eterna e imperecedara conquista",
            "details": "Observando el tiempo",
            "timestamps": {
                "start": int(time.time())},
            "assets":{
                "large_image": "bg_space",
                "large_text": "Time"
            },
            "buttons": [
                {
                    "label": "Twitch",
                    "url": "https://www.twitch.tv/kaidon456",
                },
                {
                    "label": "Mis redes",
                    "url": "https://kaidon456.carrd.co/",
                }
            ]
        }
    )
    print("Presence updated")

    while True:
        time.sleep(15)