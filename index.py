from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot" , read_only=False , logic_adapters=["chatterbot.logic.BestMatch"])

list_to_train = [
    "",
    "",
    "",
]

List_trainer = ListTrainer(bot)

list_train.train()

