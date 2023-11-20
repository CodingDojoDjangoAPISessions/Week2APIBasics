from DnD5thAPI import BASE_URL
import requests

print(BASE_URL)


class ClassAdapter:

    def __init__(self):
        self.url = BASE_URL + "/api/classes"

    def get_all_classes(self):
        response = requests.get(url=self.url)
        return response.json()

class MonsterAdapter:

    def __init__(self):
        self.url = BASE_URL+"/api/monsters"

    def get_all_monsters(self):
        response = requests.get(url=self.url)
        return response.json()

    def get_a_monster(self, index):
        monster_url = f"{self.url}/{index}"
        response = requests.get(url=monster_url)
        return response.json()