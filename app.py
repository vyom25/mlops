from flask import Flask, jsonify, request
import pickle

# Load the pre-trained model
model_pickle = open("./classifier.pkl", "rb")
model = pickle.load(model_pickle)
print("Loaded_the_model")
    

app = Flask(__name__)

@app.route('/ping/<username>', methods=['GET'])
def ping(username):
    return jsonify({"message": f"Hello, {username}! You are pinging the server."})

@app.route('/predict', methods=['POST'])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == 'Unmarried':
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_history'] == 'Unclear Debts':
        Credit_history = 0
    else:
        Credit_history = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    # Make prediction
    prediction = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_history]])

    if prediction ==0:
        return jsonify({"prediction": "Loan Rejected"})
    else:
        return jsonify({"prediction": "Loan Approved"})

if __name__  == "__main__":
    app.run(debug=True)