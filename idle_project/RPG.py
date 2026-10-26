import random
import json
import time

races = {"Zombie":
             {"Health": [50, 70],
              "Dexterity": [15, 25],
              "Agility": [20, 30],
              "Strength": [20, 30]},
         "Goblin":
             {"Health": [30, 50],
              "Dexterity": [15, 25],
              "Agility": [40, 50],
              "Strength": [20, 30]},
         "Human":
             {"Health": [40, 60],
              "Dexterity": [15, 55],
              "Agility": [15, 55],
              "Strength": [20, 40]},
         "Dragon":
             {"Health": [60, 80],
              "Dexterity": [15, 25],
              "Agility": [30, 40],
              "Strength": [40, 50]},
         "Unicorn":
             {"Health": [15, 35],
              "Dexterity": [30, 40],
              "Agility": [20, 30],
              "Strength": [35, 45]},
         "Elf":
             {"Health": [30, 50],
              "Dexterity": [40, 50],
              "Agility": [30, 40],
              "Strength": [15, 25]},
         "Orc":
             {"Health": [15, 35],
              "Dexterity": [11, 21],
              "Agility": [15, 25],
              "Strength": [15, 25]}
         }
classes = {"Tank":
               {"Health": 20,
                "Strength": 20,
                "Dexterity": -10,
                "Agility": -10,
                "Magic Slots": [5, 10],
                "Knockback": [10, 20],
                "Shield": [10, 20]},
           "Melee":
               {"Health": 10,
                "Strength": 20,
                "Dexterity": -10,
                "Agility": 20,
                "Magic Slots": [5, 10],
                "Range Increase": [10, 20],
                "Stealth": [10, 20]},
           "Mage":
               {"Health": -10,
                "Strength": -10,
                "Dexterity": 20,
                "Agility": 20,
                "Magic Slots": [5, 10],
                "Magic Power": [10, 20],
                "Magic Reduction": [10, 20]},
           "Support":
               {"Health": 20,
                "Strength": -10,
                "Dexterity": 20,
                "Agility": -10,
                "Magic Slots": [5, 10],
                "Heal Aura": [10, 20],
                "Magic Aura": [10, 20]}
           }
magic = {"Fighting":
             {"Half": ["Flying", "Poison", "Bug", "Psychic", "Fairy"],
              "Effective": ["Fighting", "Ground", "Fire", "Water", "Grass", "Electric", "Dragon"],
              "Super": ["Rock", "Steel", "Ice", "Dark"],
              "No": "Ghost"},
         "Flying":
             {"Half": ["Rock", "Steel", "Electric"],
              "Effective": ["Flying", "Poison", "Ground", "Ghost", "Fire", "Water", "Psychic", "Ice", "Dragon", "Dark",
                            "Fairy"],
              "Super": ["Fighting", "Bug", "Grass"],
              "No": ""},
         "Poison":
             {"Half": ["Poison", "Ground", "Rock", "Ghost"],
              "Effective": ["Fighting", "Flying", "Bug", "Fire", "Water", "Electric", "Psychic", "Ice", "Dragon",
                            "Dark"],
              "Super": ["Grass", "Fairy"],
              "No": "Steel"},
         "Ground":
             {"Half": ["Bug", "Grass"],
              "Effective": ["Fighting", "Ground", "Ghost", "Water", "Psychic", "Ice", "Dragon", "Dark", "Fairy"],
              "Super": ["Poison", "Rock", "Steel", "Fire", "Electric"],
              "No": "Flying"},
         "Rock":
             {"Half": ["Fighting", "Ground", "Steel"],
              "Effective": ["Poison", "Rock", "Ghost", "Water", "Grass", "Electric", "Psychic", "Dragon", "Dark",
                            "Fairy"],
              "Super": ["Flying", "Bug", "Fire", "Ice"],
              "No": ""},
         "Bug":
             {"Half": ["Fighting", "Flying", "Poison", "Ghost", "Steel", "Fire", "Fairy"],
              "Effective": ["Ground", "Rock", "Bug", "Water", "Electric", "Ice", "Dragon"],
              "Super": ["Grass", "Psychic", "Dark"],
              "No": ""},
         "Ghost":
             {"Half": ["Dark"],
              "Effective": ["Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Steel", "Fire", "Water", "Grass",
                            "Electric", "Ice", "Dragon", "Fairy"],
              "Super": ["Ghost", "Psychic"],
              "No": ""},
         "Steel":
             {"Half": ["Steel", "Fire", "Water", "Electric"],
              "Effective": ["Fighting", "Flying", "Poison", "Ground", "Bug", "Ghost", "Grass", "Psychic", "Dragon",
                            "Dark"],
              "Super": ["Rock", "Ice", "Fairy"],
              "No": ""},
         "Fire":
             {"Half": ["Rock", "Fire", "Water", "Dragon"],
              "Effective": ["Fighting", "Flying", "Poison", "Ground", "Ghost", "Electric", "Psychic", "Dark", "Fairy"],
              "Super": ["Bug", "Steel", "Grass", "Ice"],
              "No": ""},
         "Water":
             {"Half": ["Water", "Grass", "Dragon"],
              "Effective": ["Fighting", "Flying", "Poison", "Bug", "Ghost", "Steel", "Electric", "Psychic", "Ice",
                            "Dark", "Fairy"],
              "Super": ["Ground", "Rock", "Fire"],
              "No": ""},
         "Grass":
             {"Half": ["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"],
              "Effective": ["Fighting", "Ghost", "Electric", "Psychic", "Ice", "Dark", "Fairy"],
              "Super": ["Ground", "Rock", "Water"],
              "No": ""},
         "Electric":
             {"Half": ["Grass", "Electric", "Dragon"],
              "Effective": ["Fighting", "Poison", "Rock", "Bug", "Steel", "Fire", "Psychic", "Ice", "Dark", "Fairy"],
              "Super": ["Flying", "Water"],
              "No": "Ground"},
         "Psychic":
             {"Half": ["Steel", "Psychic"],
              "Effective": ["Flying", "Ground", "Rock", "Bug", "Ghost", "Fire", "Water", "Grass", "Electric", "Ice",
                            "Dragon", "Fairy"],
              "Super": ["Fighting", "Poison"],
              "No": "Dark"},
         "Ice":
             {"Half": ["Steel", "Fire", "Water", "Ice"],
              "Effective": ["Fighting", "Poison", "Rock", "Bug", "Ghost", "Electric", "Psychic", "Dark", "Fairy"],
              "Super": ["Flying", "Ground", "Grass", "Dragon"],
              "No": ""},
         "Dragon":
             {"Half": ["Steel"],
              "Effective": ["Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Fire", "Water", "Grass",
                            "Electric", "Psychic", "Ice", "Dark"],
              "Super": ["Dragon"],
              "No": "Fairy"},
         "Dark":
             {"Half": ["Fighting", "Dark", "Fairy"],
              "Effective": ["Flying", "Poison", "Ground", "Rock", "Bug", "Steel", "Fire", "Water", "Grass", "Electric",
                            "Ice", "Dragon"],
              "Super": ["Ghost", "Psychic"],
              "No": ""},
         "Fairy":
             {"Half": ["Poison", "Steel", "Fire"],
              "Effective": ["Flying", "Ground", "Rock", "Bug", "Ghost", "Water", "Grass", "Electric", "Psychic", "Ice",
                            "Fairy"],
              "Super": ["Fighting", "Dragon", "Dark"],
              "No": ""}
         }

def current():


def check(checks):
    with open("characters.json", "r") as file:
        chars = json.load(file)["Bank"]
        keys = []
        count = 0
        for i in range(len(chars)):
            keys.append(list(chars[i].keys())[0])
        for name in keys:
            if checks != name:
                count += 1
        if count == len(keys):
            return True
        else:
            return False


def createCharacter():
    name = input("Enter your characters name\n").lower()
    if check(name):
        aRange = 5
        magic_power = 20
        race = random.choice(list(races.keys()))
        class1 = random.choice(list(classes.keys()))
        spells = random.choice(list(magic.keys()))
        health = random.randint(races[race]["Health"][0] + classes[class1]["Health"],
                                races[race]["Health"][1] + classes[class1]["Health"])
        strength = random.randint(races[race]["Strength"][0] + classes[class1]["Strength"],
                                  races[race]["Strength"][1] + classes[class1]["Strength"])
        dexterity = random.randint(races[race]["Dexterity"][0] + classes[class1]["Dexterity"],
                                   races[race]["Dexterity"][1] + classes[class1]["Dexterity"])
        agility = random.randint(races[race]["Agility"][0] + classes[class1]["Agility"],
                                 races[race]["Agility"][1] + classes[class1]["Agility"])
        location = (0, 0)
        magic_slots = random.randint(classes[class1]["Magic Slots"][0], classes[class1]["Magic Slots"][0])
        stats = [name, race, class1, spells, health, strength, dexterity, agility, magic_slots, location]
        if class1 == "Tank":
            knockback = random.randint(10, 20)
            shield = random.randint(10, 20)
            stats.append(knockback)
            stats.append(shield)
            stats.append(magic_power)
            stats.append(aRange)
            stats.append("Knockback")
            stats.append("Shield")
            stats.append("Magic Power")
            stats.append("Range")
        elif class1 == "Melee":
            aRange = aRange + random.randint(10, 20)
            stealth = random.randint(10, 20)
            stats.append(stealth)
            stats.append(magic_power)
            stats.append(aRange)
            stats.append("Stealth")
            stats.append("Magic Power")
            stats.append("Range")
        elif class1 == "Mage":
            mp = magic_power + random.randint(10, 20)
            mr = random.randint(10, 20)
            stats.append(mp)
            stats.append(mr)
            stats.append(aRange)
            stats.append("Magic Power")
            stats.append("Magic Reduction")
            stats.append("Range")
        elif class1 == "Support":
            ha = random.randint(10, 20)
            ma = random.randint(10, 20)
            stats.append(ha)
            stats.append(ma)
            stats.append(magic_power)
            stats.append(aRange)
            stats.append("Health Aura")
            stats.append("Magic Aura")
            stats.append("Magic Power")
            stats.append("Range")
        character = convert_to_dict(stats)
        saveCharacter(character)
        starter = True
    else:
        with open("characters.json") as f2:
            chars = json.load(f2)["Bank"]
            keys = []
            for i in range(len(chars)):
                keys.append(list(chars[i].keys())[0])
            player = keys.index(name)
            character = chars[player]
            starter = False
    return character, starter


def saveCharacter(char_sheet):
    with open("characters.json", "r") as f:
        memory = json.load(f)
    with open("characters.json", "w") as f1:
        memory["Bank"].append(char_sheet)
        json.dump(memory, f1, indent=4)


def convert_to_dict(l1):
    if len(l1) == 16:
        dict1 = {l1[0]: {"Race": l1[1],
                         "Class": l1[2],
                         "Spells": l1[3],
                         "Health": l1[4],
                         "Strength": l1[5],
                         "Dexterity": l1[6],
                         "Agility": l1[7],
                         "Magic Slots": l1[8],
                         "Current Location": l1[9],
                         l1[13]: l1[10],
                         l1[14]: l1[11],
                         l1[15]: l1[12]}
                 }
    else:
        dict1 = {l1[0]: {"Race": l1[1],
                         "Class": l1[2],
                         "Spells": l1[3],
                         "Health": l1[4],
                         "Strength": l1[5],
                         "Dexterity": l1[6],
                         "Agility": l1[7],
                         "Magic Slots": l1[8],
                         "Current Location": l1[9],
                         l1[14]: l1[10],
                         l1[15]: l1[11],
                         l1[16]: l1[12],
                         l1[17]: l1[13]}
                 }
    return dict1


def updateCharacter():
    pass


def generateRoom():
    pass


def generateLoot():
    pass


def gameLoop(running, character, start):
    name = list(character.keys())[0].title()
    if start:
        print(f"Hello traveler {name}")
        time.sleep(0.1)
        print(f"Are you ready for the most fun and exhilarating game of your life?")
        time.sleep(0.1)
        print(f"See i didn't even have to ask i already know that your answer would be a yes")
        time.sleep(0.1)
        print(f"But if at any point you want to leave either type bye or ctrl+c")
        time.sleep(0.1)
        print(f"So have fun in my game!:)")
        time.sleep(1)
        print(f"{name} you are here as you were once a {character[name.lower()]['Class']} in the normal land of Earth")
        time.sleep(0.1)
        print(f"You signed yourself up for the trip of a lifetime to the great planet called A4353792")
        time.sleep(0.1)
        print(f"Which is said to have a breathable atmosphere")
        time.sleep(0.1)
        print(f"Your ship full of passengers and supplys sadly crashed leaving you")
        time.sleep(0.1)
        print(f"Lost")
        time.sleep(1)
        print(f"Your materials are scattered and from what you believe there is no life on this planet")
        time.sleep(0.1)
        print(f"Or is there")
        time.sleep(3)
    else:
        print(f"Welcome back traveler {name}")
        time.sleep(0.1)
        print(f"Are you ready for the most fun and exhilarating game of your life?")
        time.sleep(0.1)
        print(f"See i didn't even have to ask i already know that your answer would be a yes")
        time.sleep(0.1)
        print(f"But if at any point you want to leave either type bye or ctrl+c")
        time.sleep(0.1)
        print(f"So have fun in my game!:)")
        time.sleep(1)
        print(f"You have been put back in your last location however it has been days since {name} has traveled here")
        time.sleep(0.1)
        print(f"So don't be surprised if some things may have changed slightly")
    while running:
        try:
            current()
        except KeyboardInterrupt:
            running = False


if __name__ == '__main__':
    char, new = createCharacter()
    # print(char)
    gameLoop(False, char, new)
