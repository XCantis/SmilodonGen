import json
import os

SAVE_FOLDER = "saves"

class SaveManager:

    @staticmethod
    def save_game(clan):
        os.makedirs(SAVE_FOLDER, exist_ok=True)

        data = {
            "name": clan.name,
            "age": clan.age,
            "health": clan.health,
            "members": []
        }

        for member in clan.members:
            data["members"].append({
                "name": member.name,
                "sex": member.sex,
                "age": member.age,
                "role": member.role,
                "alive": member.alive
            })

        with open(f"{SAVE_FOLDER}/{clan.name}.json", "w") as file:
            json.dump(data, file, indent=4)
