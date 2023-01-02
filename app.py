import pandas as pd
from flask import Flask,request,render_template
import pickle
import base64
import streamlit as st
import streamlit.components.v1 as components
# st.title('HTML test')
HtmlFile = open('templates/employee.html', 'r')
# raw_html = HtmlFile.read().encode("utf-8")
# raw_html = base64.b64encode(raw_html).decode()
st.components.v1.html(HtmlFile, width=None, height=None, scrolling=False)

app = Flask (__name__)
model = pickle.load (open ('model.pkl','rb'))
print("model loaded")

@app.route ('/')
def home():
    return render_template ('employee.html')

@app.route ('/predict',methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    MonthlyIncome = request.form.get("Monthly_Income")
    TotalWorkingYears = request.form.get("Total_Working_Years")
    Age = request.form.get("Age")
    YearsAtCompany = request.form.get("Years_At_Company")
    YearsWithCurrManager = request.form.get("Years_With_Curr_Manager")
    YearsInCurrentRole = request.form.get("Years_In_Current_Role")
    OverTime = request.form.get('Over_Time')
    JobLevel = request.form.get('Job_level')
    JobRole = request.form.get('Job_Role')
    StockOptionLevel = request.form.get("Stock_Option_Level")
    MaritalStatus = request.form.get('Marital_Status' ) 
    EnvSat = request.form.get("Environment_Satisfaction")
    JobInvol = request.form.get("Job_Involvement")
    
    

    OT = {'yes':975, 'no':1491}
    JL = {'Mid Junior': 740 , 'Junior' : 1150, 'Senior' : 351, 'Manager' : 131, 'Executive' : 94}
    JR = {'Sales Executive' : 570, 'Research Scientist' : 481, 'Laboratory Technician' : 507, 'Manufacturing Director' : 186, 
        'Healthcare Representative' : 156, 'Manager' : 125, 'Sales Representative' : 232, 'Research Director' : 88, 'Human Resources' : 121}
    SO = {'Low' : 1280, 'Medium' : 823, 'Very High' : 158, 'High' : 205}
    MS = {'Single' : 970, 'Married' : 1029, 'Divorced' : 467}
    ES = {"Very High":707,"High":694,"Low":598,"Medium":467}
    JI = {"High":1361,"Medium":691,"Very High":207,"Low":207}


    if OverTime in OT.keys():
        OverTime = OT.get(OverTime)
        # print(OverTime, "overtime")

    if JobLevel in JL.keys():
        JobLevel = JL.get(JobLevel)
        # print(JobLevel, "jl")

    if JobRole in JR.keys():
        JobRole = JR.get(JobRole)
        # print(JobRole, "jr")

    if StockOptionLevel in SO.keys():
        StockOptionLevel = SO.get(StockOptionLevel)
        # print(StockOptionLevel, "sol")

    if MaritalStatus in MS.keys():
        MaritalStatus = MS.get(MaritalStatus)
        # print(MaritalStatus, "ms")

    if EnvSat in ES.keys():
        EnvSat = ES.get(EnvSat)
        # print(EnvSat, "env")

    if JobInvol in JI.keys():
        JobInvol = JI.get(JobInvol)
        # print(JobInvol,"env")

    Out = {"MonthlyIncome" : int(MonthlyIncome), "TotalWorkingYears" : int(TotalWorkingYears), "Age" : int(Age), "YearsAtCompany" : int(YearsAtCompany), 
       "YearsWithCurrManager" : int(YearsWithCurrManager), "YearsInCurrentRole" : int(YearsInCurrentRole), "OverTime" : OverTime, 
       "joblev" : JobLevel, "JobRole" : JobRole, "stockopt" : StockOptionLevel, "MaritalStatus" : MaritalStatus, 
       "envsat" : EnvSat, "jobnvol" : JobInvol}
    # print(Out)

    data_df = pd.DataFrame(Out, index=[0])
    # print(data_df)
    # print(data_df.dtypes)
    prediction = model.predict(data_df)
    P = prediction[0]
    # print(P)

    if P == 1:
        Value = "Yes"
        # print(Value)
    else:
        Value = "No"
        # print(Value)

    return render_template('employee.html', prediction_text='Possibility of Employee Leaving is :- {}'.format(Value))

if __name__ == "__main__":
    app.run (debug=False)




