from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot" , read_only=False,
 logic_adapters=[
    {
        "import_path" : "chatterbot.logic.BestMatch",
        "default_response" : "I'm sorry, but I'm unable to find an answer to your question.",
        "maximum_similarity_threshold" : 0.9  
        }])

list_to_train = [
    "hi",
    "hi there",
    "what mean chaimaa to you ?",
    "she's my lobster my heart my soulmate she's anything to me ♡ "
]

List_trainer = ListTrainer(bot)

List_trainer.train(list_to_train)

while True :
      user_response = input("user: ")
      print("Chatbot: " + str(bot.get_response(user_response)))





