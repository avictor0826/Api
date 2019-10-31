from flask import Flask, jsonify, request
from flask_socketio import SocketIO , send


app = Flask(__name__)
f=open("text.txt","w+")
f.close()

@app.route("/multi", methods=['GET', 'POST'])
def mul():
	my=""
	num = request.args.get("num")
	numone = request.args.get("numone")
	val=int(numone) * int(num)
	my=my+str(num)+"*"+str(numone)+"="+str(val)
	f=open("text.txt","a+")
	f.write(my)
	#f.write("\n")
	f.close()

	f=open("text.txt","r")
	content=f.read()
	
	return jsonify(content)



if __name__=='__main__':
    app.run( debug=True)