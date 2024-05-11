from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline as pipe
import finalpredict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():      
    if request.method ==  'POST':  
        creditscore = int(request.form['credit score'])
        loanamount = float(request.form['loan amount'])
        rateofinterest = float(request.form['rate of interest'])
        loantenure = int(request.form['loan tenure'])
        monthsinrepayment = int(request.form['months in repayment'])
        dtiratio = float(request.form['DTI ratio'])
        print(creditscore, loanamount, rateofinterest, loantenure, monthsinrepayment, dtiratio )

        # Calling Finalpredict Function
        def localfunction(cs,la,roi,lt,dti,mip):
            creditrange,creditstatus=finalpredict.creditgrade(cs)
            emiamount,totalloanamount,totalinterest=finalpredict.emi(la,roi,lt)
            dtiratiograde=finalpredict.dtigrade(dti)
            newtenure=finalpredict.tenure(emiamount,roi,la,mip,lt)
            roi=finalpredict.roidata(totalinterest,totalloanamount)            
            return (creditrange,creditstatus,emiamount,totalloanamount,totalinterest,dtiratiograde,newtenure,roi)       

        # Code Starts Here         
        creditrange,creditstatus,emiamount,totalloanamount,totalinterest,dtiratiograde,newtenure,roi =localfunction(creditscore, loanamount, rateofinterest, loantenure, dtiratio, monthsinrepayment)
        finalpredict.result(creditrange,emiamount,totalloanamount,totalinterest,dtiratiograde,newtenure,roi)
        data= [[creditscore, dtiratio, loanamount, rateofinterest,
                loantenure, monthsinrepayment, creditrange,
                emiamount, totalloanamount, totalinterest,
                newtenure, roi]] 
        #classout,regressionone,regressiontwo=finalpredict.pipeline_output(data)              

        return render_template("result.html", creditscore=creditscore,loanamount=loanamount,
                rateofinterest=rateofinterest,loantenure=loantenure,monthsinrepayment=monthsinrepayment,
                dtiratio=dtiratio,creditstatus=creditstatus,emiamount=emiamount,
                totalloanamount=totalloanamount,totalinterest=totalinterest, dtiratiograde=dtiratiograde,
                newtenure=newtenure, roi=roi, #classout=classout, regressionone=regressionone,
                #regressiontwo=regressiontwo)   
        )
        
        
    else:
        print("Welcome page 4") 
        return render_template("predict.html")    
   
@app.route('/result', methods=['GET'])
def result():      
    if request.method ==  'GET':
        return render_template("index.html",creditscore=creditscore,loanamount=loanamount,
                rateofinterest=rateofinterest,loantenure=loantenure,monthsinrepayment=monthsinrepayment,
                dtiratio=dtiratio,creditstatus=creditstatus,emiamount=emiamount,
                totalloanamount=totalloanamount,totalinterest=totalinterest, dtiratiograde=dtiratiograde,
                newtenure=newtenure, roi=roi, classout=classout, regressionone=regressionone,
                regressiontwo=regressiontwo) 
        
    else:
        return render_template("result.html")  


if __name__ == '__main__':
    app.run(debug=True)