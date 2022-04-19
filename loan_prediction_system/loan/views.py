from django.shortcuts import render


# Create your views here.
from rest_framework.generics import GenericAPIView
from .utils import classify


class GetResult(GenericAPIView):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        data = request.data
        credit_Score = data.get("Credit_Score", '')
        First_Time_Homebuyer_Flag = data.get("First_Time_Homebuyer_Flag", "")
        mortgage_insurance_percentage = data.get("Mortgage_Insurance_Percentage", "")
        number_of_units = data.get("Number_Of_Units", "")
        occupancy_status = data.get("Occupancy_Status", "")
        original_combined_loan_to_value = data.get("Original_Combined_Loan_To_Value", '')
        original_debt_to_income_ratio = data.get("Original_Debt_To_Income_Ratio", "")
        original_UPB = data.get("Original_UPB","")
        original_loan_to_value = data.get("Original_Loan_To_Value", "")
        original_interest_rate = data.get("Original_Interest_Rate", "")
        prepayment_penalty_mortgage_flag = data.get("Prepayment_Penalty_Mortgage_Flag", "")
        product_type = data.get("Product_Type", "")
        property_type = data.get("Property_Type", "")
        loan_purpose = data.get("Loan_Purpose", "")
        original_loan_term = data.get("Original_Loan_Term", "")
        number_of_borrowers = data.get("Number_Of_Borrowers", "")


        answer = classify(credit_Score, First_Time_Homebuyer_Flag,mortgage_insurance_percentage, number_of_units,
                          occupancy_status,original_combined_loan_to_value,original_debt_to_income_ratio, original_UPB,
                          original_loan_to_value,original_interest_rate,prepayment_penalty_mortgage_flag,product_type,
                          property_type, loan_purpose,original_loan_term, number_of_borrowers)

        return render(request, 'index.html',{"result":answer})