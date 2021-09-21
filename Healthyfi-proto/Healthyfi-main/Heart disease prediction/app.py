import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'Healthyfi-main\Heart disease prediction\heart_attack_prediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('new.html')
@app.route('/disease/',methods=['POST'])
def disease():
    d_name=request.form['search-bar']
    if(d_name=="heart attack"):
       return render_template("survey.html",disease=d_name)
    elif(d_name=="liver disease"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="breast cancer"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="diabetes"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="kidney disease"):
        return render_template("survey.html",disease=d_name)
        
    else:
        msg="No disease found!"
        return render_template("new.html",msg=msg)
@app.route('/survey/',methods=['POST'])
def survey():
    disease_name=request.form['disease-name']
    if(disease_name == "heart attack"):
        return render_template("index.html")
    else:
        return render_template("new.html",msg="under maintanance!")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output ==1:
        return render_template('index.html', prediction_text='You have risk of heart attack'.format(output))
    
    elif output == 0:
        return render_template('index.html', prediction_text='You dont really have risk of heart attack'.format(output))
        



if __name__ == "__main__":
    app.run(debug=True)