# Mortgage-Backed Securities Prepayment Risk Prediction

## Overview

The Mortgage-Backed Securities (MBS) Prepayment Risk Prediction project is a web application designed to predict the risk of consumers paying off their mortgages early. Given the significant impact that early mortgage payoffs have on MBS investments, this application provides valuable insights for investors and financial institutions. By utilizing machine learning pipelines, the application analyzes data from Freddie Mac to uncover trends and indicators that can assist in anticipating consumer behavior regarding mortgage prepayments.

## Purpose

The primary goal of this project is to enhance decision-making for MBS investments and risk management by predicting the likelihood of early mortgage payoffs. Early payoffs can affect the cash flow of MBS, as investors stop receiving interest payments on mortgages that are paid off ahead of schedule. 

## Explanation of Columns

CreditScore: Numeric score representing the creditworthiness of the borrower. No missing values, with 370 unique scores.

FirstPaymentDate: Date of the first payment, stored as an integer (likely a timestamp). There are 66 unique dates.

FirstTimeHomebuyer: Categorical variable indicating whether the borrower is a first-time homebuyer. Contains 3 unique values.

MaturityDate: The date when the loan matures, stored as an integer. There are 96 unique maturity dates.

MSA : Metropolitan Statistical Area, a categorical variable with 392 unique entries.

MIP: Mortgage Insurance Premium, an integer with 37 unique values.

Units: Number of units in the property (e.g., single-family home, multi-family). Contains 5 unique values.

Occupancy: Indicates whether the property is owner-occupied or rented, with 3 unique categories.

OCLTV: Original Combined Loan-to-Value ratio, an integer with 102 unique values.

DTI: Debt-to-Income ratio, an integer with 66 unique values.

OrigUPB: Original Unpaid Principal Balance, an integer with 375 unique balances.

LTV: Loan-to-Value ratio, an integer with 97 unique values.

OrigInterestRate: The original interest rate of the loan, stored as a float with 254 unique rates.

Channel: The channel through which the loan was originated (e.g., retail, wholesale), with 4 unique values.

PPM: Prepayment Penalty Mortgage, a categorical variable with 3 unique values.

ProductType: Type of mortgage product, with only 1 unique value (indicating all entries are of the same type).

PropertyState: The state where the property is located, with 53 unique states.

PropertyType: Type of property (e.g., single-family, condo), with 7 unique types.

PostalCode: The postal code of the property, with 1,767 unique codes.

LoanSeqNum: A unique identifier for each loan, with 291,451 unique entries (indicating it is likely a primary key).

LoanPurpose: Purpose of the loan (e.g., purchase, refinance), with 3 unique values.

OrigLoanTerm: The original term of the loan in months, with 61 unique terms.

NumBorrowers: Number of borrowers on the loan, with 3 unique values.

SellerName: The name of the loan seller, with 24,994 missing values and 21 unique names.

ServicerName: The name of the loan servicer, with 20 unique names.

EverDelinquent: Indicates whether the borrower has ever been delinquent on payments, with 2 unique values (likely binary).

MonthsDelinquent: The number of months the loan has been delinquent, with a maximum of 174 months.

MonthsInRepayment: The number of months the loan has been in repayment, with a maximum of 212 months.

## Features

1. **Prepayment Risk Prediction**:
   - Utilizes machine learning models to predict the risk of early mortgage payoffs.

2. **Loan Eligibility Classification**:
   - Implements a classification model to determine loan eligibility based on consumer data.

3. **Delinquency Regression**:
   - Employs a regression model to predict the likelihood of mortgage delinquency.

4. **Data Analysis**:
   - Analyzes Freddie Mac data to identify trends and factors influencing mortgage prepayments.

5. **User-Friendly Interface**:
   - Provides a web-based interface for users to input data and view predictions.

6. **Model Evaluation**:
   - Includes functionality to evaluate model performance and accuracy.

7. **Visualization**:
   - Displays visualizations of prediction results and trends to aid user understanding.

## Technologies Used

- **Python**: The primary programming language for developing the machine learning models and web application.
- **Streamlit**: Framework for building the web application interface.
- **Scikit-learn**: Library for implementing machine learning algorithms.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib/Seaborn**: Libraries for data visualization.
- **Freddie Mac Data**: Trusted source for mortgage data used in model training and prediction.
