# This attribute is supported by some versions and others not, so it is handled
import time
time.clock = time.time
# ChatBot class is used for creating a chatbot instance
from chatterbot import ChatBot
# Importing the trainer that trains any incoming data outside the corpus
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
# Creating an instance of ChatBot
currentBot = ChatBot("ShadiBot")
# Creating a trainer to train the model on the data
botTrainer = ListTrainer(currentBot)
# file contains a conversation between two people, it is the training data
file = open('chat.txt', 'r')
# converting the file to a list for easy manipulation
data = file.readlines()
# the counter represents the index of my parts in exchanges
counter = 0
# training the data
botTrainer.train(data)
while True:
    if counter == 32:
        break
    query = (data[counter])
    # this is my speaking
    print("Me : "+query)
    # this is the response of the bot
    print("Bot: " + str(currentBot.get_response(Statement(text=query, search_text=query))))
    print("##############################################################################")
    counter +=2