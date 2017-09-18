from flask import Flask, render_template, jsonify, request
import json
import Example.eduhouse_chatbot_KoreanQ_V2 as griffithChatbot
app = Flask(__name__)

griffithChatbot.train()
@app.route('/')
def hello():
   all_args =""
   return render_template("index.html")
@app.route('/input')
def output():
    
    all_args = request.args.lists() # gets the get arguments passed to the server from the webpage, here is where you would do stuff with it.
    inputList = list(all_args)
    #outputText = json.loads(outputJson)
    inputText = str(inputList[0][1])
    #inputText = str(inputList[0][1])
    inputText = inputText.lower()
    print(inputText)
    chatbotOutput = griffithChatbot.search(inputText)
    #jsonify(all_args) #if you want the args in json format.
    print (chatbotOutput)
    return render_template("index.html", output=chatbotOutput) # pass what you want the chatbot to say here. see: https://stackoverflow.com/questions/24292766/how-to-process-get-query-string-with-flask


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"), debug=True) #must be run on port 8080 or 8082 otherwise c9 won't run it.