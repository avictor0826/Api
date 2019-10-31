import os
from flask import Flask, render_template,jsonify, request, stream_with_context, request, Response
from time import sleep

#fileis='/tmp/datelog'
fileis='text.txt'

app = Flask(__name__)
@app.route('/calc', methods=['GET', 'POST'])
def index():
    return render_template('st.html', fdd= 'asldjf' )

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    #rv.enable_buffering(5)
    rv.disable_buffering()
    return rv

def generate():
    with open(fileis, "r") as f:
        while True:
            content = f.readline()
            yield str(content)


@app.route('/page')
def stream():
    cc = generate()
    return Response(stream_with_context(stream_template('justst.html', fdd = cc)))

f=open(fileis,"w+")
f.close()

@app.route("/multi", methods=['GET', 'POST'])
def mul():
    my=""
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    val=int(number1) * int(number2)
    my=str(number1)+" * "+str(number2)+" = "+str(val)+"\n"
    f=open("text.txt","a+")
    f.write(my)
    return jsonify({ "result": val})

@app.route("/add", methods=['GET', 'POST'])
def add():
    my=""
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    val=int(number1) + int(number2)
    my=str(number1)+" + "+str(number2)+" = "+str(val) + "\n"
    f=open("text.txt","a+")
    f.write(my)
    return jsonify({ "result": val})

@app.route("/divide", methods=['GET', 'POST'])
def divide():
    my=""
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    val=int(number1) / int(number2)
    my=str(number1)+" / "+str(number2)+" = "+str(val) + "\n"
    f=open("text.txt","a+")
    f.write(my)
    return jsonify({ "result": val})
	
@app.route("/sub", methods=['GET', 'POST'])
def sub():
    my=""
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    val=int(number1) - int(number2)
    my=str(number1)+" - "+str(number2)+" = "+str(val) + "\n"
    f=open("text.txt","a+")
    f.write(my)
    return jsonify({ "result": val})
    

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
