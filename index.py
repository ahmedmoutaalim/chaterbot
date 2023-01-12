from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer , ChatterBotCorpusTrainer
from flask import Flask , render_template , request



app = Flask(__name__)

bot = ChatBot("chatbot" , read_only=False,
 logic_adapters=[
    {
        "import_path" : "chatterbot.logic.BestMatch",
        "default_response" : "I'm sorry, but I'm unable to find an answer to your question.",
        "maximum_similarity_threshold" : 0.9  
        }])



List_trainer = ListTrainer(bot)


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")

 
@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return  str(bot.get_response(userText))

if __name__ == "__main__" : 
    app.run(debug= True)

