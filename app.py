#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
bot = ChatBot("Python-BOT")
trainer = ListTrainer(bot)
trainer.train(['App is not working properly', 'Please provide feedback at the feedback section','Thanks',''])
greet_conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]


issue_resolve = [
"My app is crashing",
"Our best minds our working on it",
"OK",
"Thank you for contacting Healthwayy"

]
 
open_timings_conversation = [
    "Who created Healthwayy",
    "Healthwayy is created by three geeks Kushagra Sharma, Kashish Bhagat and Manish",
    "How can I contact them",
    "You can send a feedback to them",
    "How?",
    "There is feedback option inside the app",
    "Thanks",
    "Bye... Have a good day"
]
 
close_timings_conversation = [
    "What time does the Bank close?",
    "The Bank closes at 5PM",
]




#Training healthwayyBot
trainer.train(greet_conversation)
trainer.train(issue_resolve)
trainer.train(open_timings_conversation)
trainer.train(close_timings_conversation)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")














def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(bot.get_response(userText))
    if botReply is "default_value":
        botReply = str(bot.get_response('default_response'))
@app.route("/")
def index():    
    return render_template("index.html") 
@app.route("/get")

def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
