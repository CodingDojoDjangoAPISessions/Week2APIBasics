from DnD5thAPI.classes_rest import ClassAdapter, MonsterAdapter
from DnD5thAPI.glasses_graphql import ClassGraphQLAdapter
from pprint import pprint

def main():

    connector = ClassGraphQLAdapter()
    response = connector.get_all_classes()





if __name__=="__main__":
    main()
