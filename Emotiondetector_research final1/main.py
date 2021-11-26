from flask import Flask,request,render_template,jsonify
import  record as r


app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html')

@app.route("/index", methods=["POST","GET"])
def trigger():
   # if request.method == "POST":
      return r.processor()
      # print("Hello")
   # return render_template('index.html')
   

if __name__ == "__main__":
   app.run(debug=True)

    