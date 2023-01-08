from chatterbot import ChatBot

bot = ChatBot("units" , logic_adabters=['chatterbot.loic.UnitConversion'])

while True:
    user_text = input("ask a question in unit conversion : ")
    chatbot_response = str(bot.get_response(user_text))
    print(chatbot_response)

    