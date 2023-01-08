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
                     "Hello!",
                     "Hi there",
                     "what's your name",
                     "im a bot i dont have a name",
                     "how old are you ?",
                     "i'm ageless"

                ]

list_to_train2 = [   
                     "Hello!",
                     "Hi ?",  
                     "Can you tell me a joke?",   
                     "joke.",  
                     "Ha ha, that's funny. Can you tell me more about Python?", 
                     "Python is a high-level, general-purpose programming language. It is widely used for web development, data analysis, artificial intelligence, and scientific computing. Python is known for its simplicity, readability, and flexibility.",   
                     "That's really interesting. Thank you for the information.", 
                     "You're welcome! Is there anything else you would like to know?",
                ]

List_trainer = ListTrainer(bot)

 
List_trainer.train(list_to_train)
List_trainer.train(list_to_train2)
 
while True :
      user_response = input("user: ")
      print("Chatbot: " + str(bot.get_response(user_response)))





