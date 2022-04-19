import pickle
import numpy as np
loan_model = pickle.load(open('E:/test/loan_prediction_system/loan/finalized_model.sav', 'rb'))

def classify(credit_score,first_time_homebuyer_flag, mortgage_insurance_percentage, number_of_units,occupancy_status,
             original_combined_loan_to_value, original_debt_to_income_ratio, original_upb, original_loan_to_value,
             original_interest_rate, prepayment_penalty_mortgage_flag, product_type,property_type, loan_purpose,
             original_loan_term, number_of_borrowers,
            ):

    OCCUPANCY_STATUS_O = 0
    OCCUPANCY_STATUS_S = 0

    if occupancy_status == "0":
        OCCUPANCY_STATUS_O = 0
        OCCUPANCY_STATUS_S = 0
    elif occupancy_status == "1":
        OCCUPANCY_STATUS_O = 1
        OCCUPANCY_STATUS_S = 0
    elif occupancy_status == "2":
        OCCUPANCY_STATUS_O = 0
        OCCUPANCY_STATUS_S = 1


    if product_type == "True":
        p_type = 1
    else:
        p_type = 0

    PROPERTY_TYPE_CP = 0
    PROPERTY_TYPE_LH = 0
    PROPERTY_TYPE_MH = 0
    PROPERTY_TYPE_PU = 0
    PROPERTY_TYPE_SF = 0

    LOAN_PURPOSE_N = 0
    LOAN_PURPOSE_P = 0

    if property_type == "0":
        PROPERTY_TYPE_CP = 1
    elif property_type == "1":
        PROPERTY_TYPE_PU = 1
    elif property_type == "2":
        PROPERTY_TYPE_MH = 1
    elif property_type == "3":
        PROPERTY_TYPE_SF = 1
    elif property_type == "4":
        PROPERTY_TYPE_LH = 1

    if loan_purpose == "0":
        LOAN_PURPOSE_N = 0
        LOAN_PURPOSE_P = 1
    elif loan_purpose == "1":
        LOAN_PURPOSE_N = 1
        LOAN_PURPOSE_P = 0


    data = [[credit_score,mortgage_insurance_percentage, number_of_units, original_combined_loan_to_value,
             original_debt_to_income_ratio, original_upb, original_loan_to_value, original_interest_rate,
             prepayment_penalty_mortgage_flag, p_type, original_loan_term, number_of_borrowers,PROPERTY_TYPE_CP, PROPERTY_TYPE_LH,
            PROPERTY_TYPE_MH, PROPERTY_TYPE_PU,PROPERTY_TYPE_SF, OCCUPANCY_STATUS_O, OCCUPANCY_STATUS_S,
             first_time_homebuyer_flag, LOAN_PURPOSE_N, LOAN_PURPOSE_P]]
    
    data = np.asarray(data)

    prediction = loan_model.predict(data)

    if prediction == 1:
        message = "You are more like to pre-pray your loan installments"
    elif prediction == 0:
        message = "You are not like to pre-pray your loan installments"

    return message
