from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
   all_args =""
   return render_template("index.html")
@app.route('/input')
def output():
    
    all_args = request.args.lists() # gets the get arguments passed to the server from the webpage, here is where you would do stuff with it.
    #jsonify(all_args) #if you want the args in json format.
    print all_args
    return render_template("index.html", output=all_args) # pass what you want the chatbot to say here. see: https://stackoverflow.com/questions/24292766/how-to-process-get-query-string-with-flask


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"), debug=True) #must be run on port 8080 or 8082 otherwise c9 won't run it.