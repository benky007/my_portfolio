import json
import tkinter

name = input("Enter gymbros name: ")
date = input("Enter date in dd/mm/yyyy format: ")
muscles = input("Enter muscles trained: ").split(" ")
duration = input("Enter duration in minutes: ")
training = True
count = 1
entry = {"Date": date, "Muscles": muscles, "Duration": duration}
print(entry)
while training:
    exercise = input(f"Enter exercise {count}: ")
    print(exercise)
    if exercise == "exit":
        training = False
    else:
        entry[f"Exercise {count}"] = {"Name": exercise}
        sets = input("Enter number of sets: ")
        for i in range(int(sets)):
            reps = input(f"Enter number of reps for set {i + 1}: ")
            weight = input(f"Enter weight for set {i + 1}: ")
            entry[f"Exercise {count}"][f"Set{i + 1}"] = [reps, weight]
        count += 1

print(entry)

with open("gym_log.json") as readfile:
    data = json.load(readfile)

for gym_rats in data["Logs"]:
    if gym_rats["Name"] == name:
        gym_rats["Sessions"] = entry
    else:
        pass

print(data)

with open("gym_log.json", "w") as outfile:
    json.dump(json_obj, outfile, separators=(",", ": "))
# TODO: need to reformat the gym.json thingy and add a catalogue of each exercise and each persons 1RM and best
#  weight and average weight and average reps