from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    name = request.args['name']
    cool = request.args['cool']
    animal = request.args['animal']
    birth =  str(request.args['birth'])
    reply1 = str(name+"The"+animal+"Lover"+cool+birth)
    return render_template('response.html', response1 = reply1)
    
if __name__=="__main__":
    app.run(debug=True)
