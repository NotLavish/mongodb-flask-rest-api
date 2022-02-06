from pymongo import MongoClient

class Database():
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://lav:owo@cluster0.gcdkv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true")
        self.db = self.cluster["contacts"]
        self.collection = self.db["people"]
        

    def createInfo(self):
        empty = {}
        name = input("Input the name: ")
        empty["name"] = name
        email = input("Input the email: ")
        empty["email"] = email
        while True:
            info = input("Anything else? ")
            if info != "done":
                empty[info] = input(f"Inset {info}:")
            else:
                break
        return empty

    def addPerson(self, info):
        self.collection.insert_one(info)
        
    def getPerson(self, name):
        return self.collection.find_one({"name":name})

    def updatePerson(self, info, newinfo):
        self.collection.update_one(info, newinfo)
        
    def displayInfo(person):
        print(f"Information\n")
        for i in person:
            print(f"{i}: {person[i]}")
    
    def makeDictionaries(self, person):
        dictionary = {}
        for i in person:
            dictionary[i] = person[i]
        return dictionary
    
    def getAll(self):
        for i in self.collection.find():
            print(i)

db = Database()
asd = db.getPerson('lavish')
asd = db.makeDictionaries(asd)
print(asd)