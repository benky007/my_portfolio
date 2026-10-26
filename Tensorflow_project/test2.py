from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

# Create a new chat bot named Charlie
chatbot = ChatBot('FreeBirdsBot')

trainer = ListTrainer(chatbot)

with open("data.json") as f:
    data = json.load(f)

    trainer.train(data["intents"][0]["traning"])

while True:
    input_data = input("You- ")
    response = chatbot.get_response(input_data)
    print("FreeBirdsBot- ", response)
