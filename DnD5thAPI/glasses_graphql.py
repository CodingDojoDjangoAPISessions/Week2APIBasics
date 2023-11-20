from DnD5thAPI import BASE_URL
import requests
from pprint import pprint

class ClassGraphQLAdapter():

    def __init__(self):
        self.url = BASE_URL+"/graphql"

    def get_all_classes(self):
        query = """
        {
            classes {
                name
                hit_die
                saving_throws {
                    name
                }
            }
        }
        """
        request = {"query": query}

        response = requests.post(url=self.url, json=request)

        pprint(response.json())