import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'Healthyfi-main\Heart disease prediction\heart_attack_prediction.pkl', 'rb'))
model_heartdisease = pickle.load(open('heart_attack_prediction.pkl', 'rb'))
model_liverdisease = pickle.load(open('liver_disease_prediction.pkl', 'rb'))
model_cancer = pickle.load(open('breast_cancer_prediction.pkl', 'rb'))
model_diabetes = pickle.load(open('diabetes_prediction.pkl', 'rb'))
model_kidney = pickle.load(open('kidney_disease_prediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('new.html')
@app.route('/disease/',methods=['POST'])
def disease():
    d_name=request.form['search-bar']
    if(d_name=="HEART ATTACK"):
       return render_template("survey.html",disease=d_name)
    elif(d_name == "LIVER DISEASE"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="BREAST CANCER"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="DIABETES"):
        return render_template("survey.html",disease=d_name)
    elif(d_name=="KIDNEY DISEASE"):
        return render_template("survey.html",disease=d_name)
        
    else:
        msg="No disease found!"
        return render_template("new.html",msg=msg)
@app.route('/survey/',methods=['POST'])
def survey():
    disease_name=request.form['disease-name']
    if(disease_name == "HEART ATTACK"):
        return render_template("heart.html")
    elif(disease_name == "LIVER DISEASE"):
         return render_template("liver.html")
    elif(disease_name == "KIDNEY DISEASE"):
         return render_template("kidney.html")
    elif(disease_name == "DIABETES"):
         return render_template("diabetes.html")
    elif(disease_name == "BREAST CANCER"):
         return render_template("breast.html")
           
    else:
        return render_template("new.html",msg="Under Maintanance!")

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
        return render_template('heart.html', prediction_text='You Have Risk of Heart Attack'.format(output))
    
    elif output == 0:
        return render_template('heart.html', prediction_text='You Dont Really Have Risk of Heart Attack'.format(output))

@app.route('/liverdisease', methods=['GET','POST'])
def liverdisease():
    if request.method == 'POST':
        Age=int(request.form['Age'])
        Total_Bilirubin= float(request.form['Total_Bilirubin'])
        Direct_Bilirubin= float(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase= int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase= int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase= int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens= float(request.form['Total_Protiens'])
        Albumin= float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio= float(request.form['Albumin_and_Globulin_Ratio'])
        Gender=int(request.form['gender'])

        prediction = model_liverdisease.predict([[Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio, Gender]])

        if prediction==1:
            return render_template('liver.html', prediction_text="Oops! You seem to have Liver Disease.", title='Liver Disease')
        else:
            return render_template('liver.html', prediction_text="Great! You don't have any Liver Disease.", title='Liver Disease')
    else:
        return render_template('liver.html', title='Liver Disease')

@app.route('/breastcancer', methods=['GET','POST'])
def breastcancer():
    if request.method == 'POST':
        texture_mean = float(request.form['texture_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])
        smoothness_mean = float(request.form['smoothness_mean'])
        compactness_mean = float(request.form['compactness_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave points_mean'])
        symmetry_mean = float(request.form['symmetry_mean'])
        radius_se = float(request.form['radius_se'])
        compactness_se = float(request.form['compactness_se'])
        concavity_se = float(request.form['concavity_se'])
        concave_points_se = float(request.form['concave points_se'])
        texture_worst = float(request.form['texture_worst'])
        smoothness_worst = float(request.form['smoothness_worst'])
        compactness_worst = float(request.form['compactness_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concave_points_worst = float(request.form['concave points_worst'])
        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])

        prediction=model_cancer.predict([[texture_mean, perimeter_mean, smoothness_mean, compactness_mean,
        concavity_mean, concave_points_mean, symmetry_mean, radius_se,
        compactness_se, concavity_se, concave_points_se, texture_worst,
        smoothness_worst, compactness_worst, concavity_worst,
        concave_points_worst, symmetry_worst, fractal_dimension_worst]])

        if prediction==1:
            return render_template('breast.html', prediction_text="Oops! The tumor is malignant.", title='Breast Cancer')
        else:
            return render_template('breast.html', prediction_text="Great! The tumor is benign.", title='Breast Cancer')
    else:
        return render_template('breast.html',title='Breast Cancer')



@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    if request.method == 'POST':
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])

        prediction = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if prediction==1:
            return render_template('diabetes.html', prediction_text="Oops! The tumor is malignant.", title='Diabetes')
        else:
            return render_template('diabetes.html', prediction_text="Great! The tumor is benign.", title='Diabetes')
    else:
        return render_template('diabetes.html',title='Diabetes')    

@app.route('/kidneydisease', methods=['GET', 'POST'])
def kidneydisease():

    if request.method == 'POST':
        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['su'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        pcv = float(request.form['pcv'])
        wbcc = float(request.form['wbcc'])
        rbcc = float(request.form['rbcc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        cad = float(request.form['cad'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])

        prediction = model_diabetes.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wbcc, rbcc,
                                              htn, dm, cad, appet, pe, ane ]])

        if prediction==1:
            return render_template('kidney.html', prediction_text="Oops! You have high risk of chronic kidney disease.", title='Kidney Disease')
        else:
            return render_template('kidney.html', prediction_text="Great! You have low risk.", title='Kidney Disease')
    else:
        return render_template('kidney.html',title='Kidney Disease')      



if __name__ == "__main__":
    app.run(debug=True)
