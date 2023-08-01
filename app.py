#flask app routing

from flask import Flask,render_template,request,redirect ,url_for


##creae a simple flask app

app=Flask(__name__)

@app.route('/',methods= ['GET'])
def welcome():
    return "<h1>welcome to home</h1>"

@app.route('/index',methods=['GET'])
def index():
    return"<h2>we are at the index page</h2>"

#variable ruleh
@app.route('/success/<int:score>')
def success(score):
    return"the person has passed and the score is : "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is :" + str(score)

@app.route ('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('calculate.html')
    else :
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average= float((maths+science+history)/3)
        res=""
        if average>=50:
            res="success"
        else:
            res="fail"
        return redirect (url_for(res,score=average))    
            
        #return render_template('calculate.html', score =average)



if __name__=="__main__":
    app.run(debug=True)