from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

chatbot = ChatBot('FreeBirdsBot')

trainer = ListTrainer(chatbot)

# trainer.train("chatterbot.corpus.english")
# trainer.train("chatterbot.corpus.english.greetings")
# trainer.train("chatterbot.corpus.english.conversations")

while True:
    input_data = input("You- ")
    response = chatbot.get_response(input_data)
    print("Bot- ", response)
