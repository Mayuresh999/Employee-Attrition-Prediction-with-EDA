import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={
        'Monthly_Income': 1000,
        'Total_Working_Years': 10,
        "Age" : 41,
        'Years_At_Company': 5,
        "Years_With_Curr_Manager" : 5,
        'Years_In_Current_Role': 2,
        'Over_Time': 'yes',
        'Job_level': 'Junior',
        'Job_Role': 'Research Scientist',
        'Stock_Option_Level': 'Medium',
        'Marital_Status': 'Married',
        "Environment_Satisfaction": 'Medium',
        "Job_Involvement" : 'High',
}
)

print(r.json())

# MonthlyIncome = 5130 #@param {type:"integer"}
# TotalWorkingYears = 2 #@param {type:"integer"}
# Age = 41 #@param {type:"integer"}
# YearsAtCompany = 10 #@param {type:"integer"}
# YearsWithCurrManager = 5 #@param {type:"integer"}
# YearsInCurrentRole = 7 #@param {type:"integer"}
# OverTime = "no" #@param ["yes", "no"]
# joblev = "Mid Junior" #@param ['Mid Junior', 'Junior', 'Senior', 'Manager', 'Executive']
# JobRole = "Research Scientist" #@param ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources']
# stockopt = "Medium" #@param ['Low', 'Medium', 'Very High', 'High']
# MaritalStatus = "Married" #@param ['Single', 'Married', 'Divorced']
# envsat = "Medium" #@param ['Low', 'Medium', 'Very High', 'High']
# jobnvol = "High" #@param ['Low', 'Medium', 'Very High', 'High']