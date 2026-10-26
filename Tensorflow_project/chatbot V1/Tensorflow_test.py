import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
from tensorflow.python.framework import ops
import random
import json
import pickle

stemmer = LancasterStemmer()
answer = 0

with open("intents1.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        pattern_words, response_words, labels, pattern_training, response_training, tag_check = pickle.load(f)
except:
    pattern_words = []
    response_words = []
    pattern_docs_x = []
    response_docs_x = []
    docs_y = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_wrds = nltk.word_tokenize(pattern)
            pattern_words.extend(pattern_wrds)
            pattern_docs_x.append(pattern_wrds)
            docs_y.append(intent["tag"])

        for response in intent["responses"]:
            response_wrds = nltk.word_tokenize(response)
            response_words.extend(response_wrds)
            response_docs_x.append(response_wrds)

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    pattern_words = [stemmer.stem(w.lower()) for w in pattern_words if w not in "?"]
    pattern_words = sorted(list(set(pattern_words)))
    response_words = [stemmer.stem(wo.lower()) for wo in response_words if wo not in "?"]
    response_words = sorted(list(set(response_words)))

    labels = sorted(labels)

    pattern_training = []
    response_training = []
    tag_check = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(pattern_docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in pattern_words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        pattern_training.append(bag)
        tag_check.append(output_row)
    pattern_training = numpy.array(pattern_training)
    tag_check = numpy.array(tag_check)

    for x1, doc1 in enumerate(response_docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc1]

        for w in pattern_words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        response_training.append(bag)
    response_training = numpy.array(response_training)

    with open("data.pickle", "wb") as f:
        pickle.dump((pattern_words, response_words, labels, pattern_training, response_training, tag_check), f)

ops.reset_default_graph()

layers = 0
for tags in data["intents"]:
    layers += len(tags["patterns"])

net = tflearn.input_data(shape=[None, len(pattern_training[0])])
net = tflearn.fully_connected(net, layers)
net = tflearn.fully_connected(net, layers)
net = tflearn.fully_connected(net, len(tag_check[0]), activation="softmax")
net = tflearn.regression(net)
# net1 = tflearn.input_data(shape=[None, len(response_training[0])])
# net1 = tflearn.fully_connected(net1, layers)
# net1 = tflearn.fully_connected(net1, layers)
# net1 = tflearn.fully_connected(net1, len(tag_check[0]), activation="softmax")
# net1 = tflearn.regression(net1)

model = tflearn.DNN(net)
# model1 = tflearn.DNN(net1)

model.fit(pattern_training, tag_check, n_epoch=500, batch_size=14, show_metric=True)
model.save("model.tflearn")
# model1.fit(pattern_training, response_training, n_epoch=500, batch_size=14, show_metric=True)
# model1.save("model1.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            print(i, w)
            if w == se:
                bag[i] = 1
    return numpy.array(bag)


def chat():
    print("Start talking to the bot(type quit to quit)")
    while True:
        inp = input("You:")
        if inp.lower() == "quit":
            with open('memory.json', 'r+') as f:
                data1 = json.load(f)
                data1["memory"][2]["responses"] = ""
                f.seek(0)
                json.dump(data1, f, indent=1)
                f.truncate()
            break
        elif inp.lower() == "train":
            model.fit(pattern_training, tag_check, n_epoch=500, batch_size=14, show_metric=True)
        elif inp.lower() == "cmd":
            passwording1 = True
            count = 0
            while passwording1:
                password = input("you need a password to go to the command prompt(enter password)\n")
                with open("accounts.json", "r") as accounts:
                    users = json.load(accounts)
                    for acc in users["passwords"]:
                        if acc["password"] == password:
                            teaching(acc["user"], users)
                            passwording1 = False
                        if acc["password"] != password:
                            count += 1
                    if count == len(users["passwords"]):
                        next1 = input(
                            "There is no user with this password(type try to try again or\ntype no to go back "
                            "to chatting)")
                        if next1 == "try":
                            pass
                        if next1 == "no":
                            passwording1 = False

        results = model.predict([bag_of_words(inp, pattern_words)])[0]
        results1 = model1.predict([bag_of_words(inp, response_words)])[0]
        results_index = numpy.argmax(results)
        results_index1 = numpy.argmax(results1)
        tag = labels[results_index]
        response_now = response_docs_x[results_index1]
        print(response_now)

        if inp != "train" and inp != "quit" and inp != "cmd" and results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            with open('memory.json', 'r+') as f:
                data1 = json.load(f)
                if tag == "how" or tag == "colour" or tag == "like":
                    if tag == "like":
                        qus = data1["memory"][0]["responses"]["question"]
                        answer = 0
                        if len(qus) == 0:
                            answer = 0
                        else:
                            for index in range(len(qus)):
                                if qus[str(index)][0] == inp:
                                    ans = qus[str(index)][1]
                                    print(ans)
                                else:
                                    answer = answer + 1
                        if answer == len(qus):
                            ran = random.choice(responses)
                            data1["memory"][0]["responses"]["question"][len(qus)] = [inp, ran]
                            ans = ran
                            print(ans)
                        f.seek(0)
                        json.dump(data1, f, indent=1)
                    elif tag == "how":
                        tag_index = 2
                        if data1["memory"][tag_index]["responses"] == "":
                            data1["memory"][tag_index]["responses"] = random.choice(responses)
                            ans = data1["memory"][tag_index]["responses"]
                            print(ans)
                            f.seek(0)
                            json.dump(data1, f, indent=1)
                            f.truncate()
                        else:
                            ans = data1["memory"][tag_index]["responses"]
                            print(ans)
                    elif tag == "colour":
                        tag_index = 1
                        if data1["memory"][tag_index]["responses"] == "":
                            data1["memory"][tag_index]["responses"] = random.choice(responses)
                            ans = data1["memory"][tag_index]["responses"]
                            print(ans)
                            f.seek(0)
                            json.dump(data1, f, indent=1)
                            f.truncate()
                        else:
                            ans = data1["memory"][tag_index]["responses"]
                            print(ans)
                if tag != "how" and tag != "like" and tag != "colour":
                    print(random.choice(responses))
        elif inp != "train" and inp != "quit" and inp != "cmd" and results[results_index] < 0.7:
            inp1 = input("Can you please teach me what you mean(yes or no)\n")
            if inp1.lower() == "yes":
                passwording = True
                count = 0
                while passwording:
                    password = input("you need a password to edit the json files(enter password)\n")
                    with open("accounts.json", "r") as accounts:
                        users = json.load(accounts)
                        for acc in users["passwords"]:
                            if acc["password"] == password:
                                teaching(acc["user"], users)
                                passwording = False
                            if acc["password"] != password:
                                count += 1
                        if count == len(users["passwords"]):
                            next1 = input(
                                "There is no user with this password(type try to try again or\ntype no to go back "
                                "to chatting)")
                            if next1 == "try":
                                pass
                            if next1 == "no":
                                passwording = False

            if inp1.lower() == "no":
                print("okay then :(")
                pass
            else:
                print("okay then:(")
                pass


def teaching(prompt, users):
    prompting = 0
    to_prompt = 0
    run = True
    adjust = True
    try:
        prompted = input(f"type help for help on how to use this command prompt or type quit to quit the prompt\nand "
                         f"you can type new for adding a new user\n{prompt}@comp.AI: ")
    except KeyboardInterrupt:
        print("^C")
    while run:
        if prompted == "help":
            print("ADD                      This is to add a new dictionary into the intents list in the json file\n"
                  "ADJUST                   This is to adjust an already existing dictionary in the intents "
                  "dictionary by "
                  "using the\n "
                  "                         number of the tag\n"
                  "ADJUST PATTERNS_ADD      This can only be run after the ADJUST command is and this adds a pattern "
                  "to \n "
                  "                         the patterns list of the chosen tag\n"
                  "ADJUST RESPONSES_ADD     This can only be run after ADJUST command is run and this adds a response "
                  "to \n "
                  "                         the responses list of the chosen tag\n"
                  "ADJUST PATTERNS_WRITE    This can only be run after the ADJUST command is and this re-writes all "
                  "of \n                         the patterns list of the chosen tag with the syntax of using forward "
                  "\n                         slashes to separate parts in the list\n"
                  "ADJUST RESPONSES_WRITE   This can only be run after the ADJUST command is and this re-writes all "
                  "of \n                         the responses list of the chosen tag with the syntax of using forward "
                  "\n                         slashes to separate parts in the list\n"
                  "NEW                      This is used to add a new user to the system by asking for a root "
                  "password \n                        and then a username and password for the new user\n"
                  "QUIT                     This is used to exit out of anything you are currently in\n")
            prompting = 1
        if prompted == "add":
            try:
                tag1 = input("enter tag of new dictionary\n")
                patterns1 = input("enter patterns list of new dictionary(___/___/___)\n")
                responses1 = input("enter responses list of new dictionary(___/___/___)\n")
                dict1 = {"tag": tag1,
                         "patterns": patterns1.split("/"),
                         "responses": responses1.split("/"),
                         "context_set": ""}
                with open("intents1.json", "r+") as file:
                    data1 = json.load(file)
                    file.seek(0)
                    data1["intents"].append(dict1)
                    json.dump(data1, file, indent=1)
                prompting = 1
            except KeyboardInterrupt:
                print("^C\n")
                prompting = 1
        if prompted == "adjust":
            print("type quit to quit this prompt")
            taged = input(f"What is to be adjusted(type the integer of the tag of the dictionary to be "
                          f"adjusted)\n{prompt}@comp.AI/adjust: ")
            adjusted = input("type adjust patterns_add to add to the patterns\ntype adjust patterns_write to "
                             f"overwrite the patterns list\ntype adjust responses_add to add to the responses\ntype "
                             f"adjust responses_write to overwrite the responses "
                             f"list\n{prompt}@comp.AI/adjust/{int(taged)}: ")
            while adjust:
                if adjusted == "adjust patterns_add":
                    with open("intents1.json", "r+") as file1:
                        intents = json.load(file1)
                        new_patterns = input("Enter new pattern")
                        intents["intents"][int(taged)]["patterns"].append(new_patterns)
                        file1.seek(0)
                        json.dump(intents, file1, indent=1)
                    to_prompt = 1
                if adjusted == "adjust patterns_write":
                    with open("intents1.json", "r+") as file1:
                        intents = json.load(file1)
                        new_patterns1 = input("Enter new pattern list(___/___/___)")
                        intents["intents"][int(taged)]["patterns"] = new_patterns1.split("/")
                        file1.seek(0)
                        json.dump(intents, file1, indent=1)
                    to_prompt = 1
                if adjusted == "adjust responses_add":
                    with open("intents1.json", "r+") as file1:
                        intents = json.load(file1)
                        new_responses = input("Enter new response")
                        intents["intents"][int(taged)]["responses"].append(new_responses)
                        file1.seek(0)
                        json.dump(intents, file1, indent=1)
                    to_prompt = 1
                if adjusted == "adjust responses_write":
                    with open("intents1.json", "r+") as file1:
                        intents = json.load(file1)
                        new_responses1 = input("Enter new response list(___/___/___)")
                        intents["intents"][int(taged)]["responses"] = new_responses1.split("/")
                        file1.seek(0)
                        json.dump(intents, file1, indent=1)
                    to_prompt = 1
                if adjusted == "quit":
                    adjust = False
                if adjusted != "quit" and adjusted != "responses_write" and adjusted != "responses_add" and \
                        adjusted != "patterns_write" and adjusted != "patterns_add":
                    print("invalid input")
                    to_prompt = 1
                if to_prompt == 1:
                    adjusted = input(f"{prompt}@comp.AI/adjust/{int(taged)}: ")
                    to_prompt = 0
            prompting = 1
        if prompted == "new":
            while True:
                new_inp = input("enter root password to make new user")
                if users["passwords"][0]["password"] == new_inp:
                    new_user = input("Enter new users prompt")
                    new_pass = input("Enter new users password")
                    dict2 = {"user": new_user, "password": new_pass}
                    with open("accounts.json", "r+") as f1:
                        acc1 = json.load(f1)
                        f1.seek(0)
                        acc1["passwords"].append(dict2)
                        json.dump(acc1, f1, indent=1)
                elif new_inp == "quit":
                    break
                else:
                    print("try again or type quit to leave\n")

                if acc1["password"] != password:
                    print("you have 4 more attempts\n")
        if prompted == "quit":
            run = False
        if prompted != "adjust" and prompted != "help" and prompted != "add" and prompted != "new" and \
                prompted != "quit" and prompted != "adjust patterns_add" and prompted != "quit":
            print("invalid input")
            prompting = 1
        if prompting == 1:
            prompted = input(f"{prompt}@comp.AI: ")
            prompting = 0


chat()
