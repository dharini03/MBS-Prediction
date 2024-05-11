# MBS-Prediction
The purpose of this project is to predict the risk of consumers paying off their mortgages early.​

Because it has an impact on mortgage-backed securities (MBS) investments they are similar to home loan bundles that are marketed to investors. Investors no longer get interest payments on mortgages that are paid off early.​

To make our predictions even more accurate, we're using data from Freddie Mac(291451, 28), a trusted source in the mortgage industry.​

We can uncover trends and indications that help anticipate whether consumers will pay off their mortgages early by analyzing this data using machine learning.​

This prediction can assist investors and financial institutions in making better decisions about MBS investments and risk management.​

​The dataset has x records and 28 variables.

CreditScore The standardized credit score used to evaluate the borrower during the loan origination process.
FirstPaymentDate The month and year that the first scheduled payment on the load in due
FirstTimeHomebuyer The indicator denoting whether a borrower on the loan qualifies as a first-time homebuyer.
MaturityDate The month and year that the final scheduled payment on the load in due.
MSA Mortgage Security Amount
MIP Mortgage Insurance Percent, the percentage of mortgage insurance coverage obtained at origination in effect at the time the security was issued.
Units The number of dwelling units in the mortgaged property at the time the loan was originated.
Occupancy The classification describing the property occupancy status at the time the loan was originated.
OCLTV For reperforming, modified fixed-rate and modified step-rate loans, the ratio, expressed as a percentage, obtained by dividing the amount of all known outstanding loans at origination by the value of the property.
DTI Debt-To-Income Ratio, The ratio obtained by dividing the total monthly debt expense by the total monthly income of the borrower at the time the loan was originated or modified.
OrigUPB
LTV (Loan-to-Value) The ratio expressed as a percentage, obtained by dividing the amount of loan at origination by the value of the property.
OrigInterestRate For reperforming, modified fixed-rate and modified step-rate loans, the interest rate of the loan as stated on the note at the time the loan was originated. For reperforming, modified fixed-rate and modified step-rate loans, the interest rate of the loan as stated on the note at the time the loan was originated.
Channel The origination channel used by the party that delivered the loan to the issuer.
PPM Prepayment Penalty Mortgage
ProductType The type of real-state product.
PropertyState The abbreviation of denoting the location of the property securing the loan.
PropertyType The classification describing the type of property that secures the loan.
PostalCode
LoanSeqNum Loan Sequence Number
LoanPurpose The classification of the loan as either a purchase money mortgage or a refinance mortgage at the time the loan was originated.
OrigLoanTerm For reperforming, modified fixed-rate and modified step-rate loans, the number of months in which regularly scheduled borrower payments are due as stated on the note at the time the loan was originated.
NumBorrowers The number of borrowers who, at the time the loan was originated, are obligated to repay the loan.
SellerName The name of the entity that sold the load to the issuer.
ServicerName The name of the entity the services the loan during the current reporting period.
EverDelinquent (Assumption) An indication if burrower is delinquent.
MonthsDelinquent Indicates the #months a borrower has been delinquent on their mortgage payments.
MonthsInRepayment Represents the #months a borrower has been making regular mortgage payments.
