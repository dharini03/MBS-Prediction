import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder


# Load the classifier model
classifier_model_path = 'Rfc_pipe.pkl'
with open(classifier_model_path, 'rb') as f:
    classifier_model = pickle.load(f)

# Load the regressor model
regressor_model_path = 'Regression_pipe.pkl'
with open(regressor_model_path, 'rb') as f:
    regressor_model = pickle.load(f)


# Function to preprocess input data
def preprocess_input(data):
    data = pd.DataFrame(data, index=[0])  # Convert input to dataframe

    label_encoder = LabelEncoder()

    for column in ['FirstTImeHomeBuyer', 'Occupancy', 'Channel', 'PPM', 'PropertyState',
                   'PropertyType', 'LoanPurpose', 'NumBorrowers']:
        if column in data:
            data[column] = label_encoder.fit_transform(data[column])[0]
 
    
    def calculateEmi(principal, monthly_interest_rate, loan_term_months):
        numerator = (1 + monthly_interest_rate) ** loan_term_months
        denominator = numerator - 1
        interest = numerator / denominator
        emi = principal * monthly_interest_rate * interest
        return np.int32(emi)
    data['OrigInterestRate_Monthly'] =  np.round((data['OrigInterestRate'] / 12) / 100, 4)
    data['MonthlyInstallment'] = data.apply(
        lambda features: calculateEmi(
            principal=features['OrigUPB'], 
            monthly_interest_rate=features['OrigInterestRate_Monthly'],
            loan_term_months=features['OrigLoanTerm']), axis=1)
    
    def calculate_monthly_income(dti, emi):
        dti = dti if dti <=1 else dti / 100
        if dti == 0:
            monthly_income = emi
        else:
            monthly_income = emi / dti
        return np.int32(monthly_income)
    data['MonthlyIncome'] = data.apply(
        lambda features: calculate_monthly_income(
            dti = features['DTI'],
            emi = features['MonthlyInstallment']), axis =1)
    
    def calculatePrepayment(dti, monthly_income):
        if (dti < 40):
            prepayment = monthly_income / 2
        else:
            prepayment = monthly_income * 3 / 4
        return np.int32(prepayment)
    data['Prepayment'] = data.apply(
        lambda features: calculatePrepayment(
            dti=features['DTI'],
            monthly_income=features['MonthlyIncome']), axis=1)
    data['ActualPayments'] = data['MonthlyInstallment'] * data['MonthsInRepayment']
    data['Prepayments'] = data['Prepayment'] // data['MonthlyInstallment']
    data['ScheduledPayments'] = data['MonthlyInstallment'] * (data['MonthsInRepayment'] - data['Prepayments'] + data['MonthsDelinquent'])
    def get_currentUPB(principal, monthly_interest_rate, monthly_installment,
                   payments_made):
         monthly_interest = monthly_interest_rate * principal
         monthly_paid_principal = monthly_installment - monthly_interest
         unpaid_principal = principal - (monthly_paid_principal * payments_made)
         return np.int32(unpaid_principal)
    data['CurrentUPB'] = data.apply(
        lambda features: get_currentUPB(
            monthly_interest_rate=features['OrigInterestRate_Monthly'],
            principal=features['OrigUPB'], 
            monthly_installment=features['MonthlyInstallment'],
            payments_made=features['MonthsInRepayment']), axis=1)
    data['PPR'] = (data['ScheduledPayments'] - data['ActualPayments']) / data['CurrentUPB']



    return data

# Function to make predictions using the classifier model
def predict_classification(data):
    # Preprocess the input data
    preprocessed_data = preprocess_input(data)
    
    # Make predictions using the classifier model
    predictions = classifier_model.predict(preprocessed_data)
    
    return predictions

#Function to make predictions using the regressor model
def predict_regression(data):
    # Preprocess the input data
    preprocessed_data = preprocess_input(data)
    
    # Make predictions using the regressor model
    predictions = regressor_model.predict(preprocessed_data)
    
    return predictions[0]

# Streamlit app
def main():
   
    # Set app title
    st.title("PREPAYMENT RISK PREDICTION")
    
    # Get user input
    user_input = {}  # Store user input in a dictionary
    

    user_input['CreditScore'] = st.number_input("Credit Score", min_value=653, max_value=770, step=1)
    #user_input['FirstTImeHomeBuyer'] = st.selectbox("First Time Home Buyer?", ['Y', 'N'])
    #user_input['MIP'] = st.number_input("MIP", min_value=0, max_value=100, step=1)
    #user_input['Units'] = st.number_input("Units", min_value=0, max_value=4, step=1)
    #user_input['Occupancy'] = st.selectbox("Occupancy", ['O', 'I', 'S'])
    #user_input['OCLTV'] = st.number_input("OCLTV", min_value=1, max_value=200, step=1)
    user_input['DTI'] = st.number_input("DTI", min_value=1, max_value=100, step=1)
    user_input['OrigUPB'] = st.number_input("Original UPB", min_value=0, max_value=1000000, step=1)
    user_input['LTV'] = st.number_input("LTV", min_value=1, max_value=200, step=1)
    user_input['OrigInterestRate'] = st.number_input("Original Interest Rate", min_value=0.0, step=0.01)
    #user_input['Channel'] = st.selectbox("Channel", ['T', 'R', 'C', 'B'])
    #user_input['LoanPurpose'] = st.selectbox("Loan Purpose", ['P', 'N', 'C'])
    user_input['OrigLoanTerm'] = st.number_input("Original Loan Term", min_value=100, max_value=400, step=1)
    #user_input['NumBorrowers'] = st.selectbox("Number of Borrowers", ['2', '1'])
    user_input['MonthsDelinquent'] = st.number_input("Months Delinquent", min_value=0, step=1)
    user_input['MonthsInRepayment'] = st.number_input("Months In Repayment", min_value=0, step=1)
    
    
    
    # Perform predictions
    # Add a "Predict" button
    if st.button("Predict"):
        # Perform predictions
        classification_result = predict_classification(user_input)

        if classification_result == 0:
            st.markdown("<p style='font-size: 30px; text-align: center; color: green;' class='output'>Loan is Not Delinquent</p>", unsafe_allow_html=True)
            regression_result = abs(int(predict_regression(user_input)))
            st.markdown(f"<p style='font-size: 30px; text-align: center;' class='output'>The prepayment risk is: {regression_result}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='font-size: 30px; text-align: center; color: red;' class='output'>Loan is Delinquent</p>", unsafe_allow_html=True)
        
    
# Run the app
if __name__ == '__main__':
    main()