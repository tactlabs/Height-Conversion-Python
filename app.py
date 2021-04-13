# importing Flask and other modules
from flask import Flask, request, render_template 
  
# Flask constructor
app = Flask(__name__)   
  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        
       value_got = request.form["value"]
       x= float(value_got)
       stable = 30.48
       y= float(stable)
       result= float(x)*float(y)
       return "Your Height is "+ str(result)+ " in cm"
    return render_template("index.html")
  
if __name__=='__main__':
   app.run(port=3001, debug = True)
