from flask import Flask, request, render_template
import joblib

app = Flask(__name__, template_folder='../templates')

# Load model
model = joblib.load('model/loan_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    income = float(request.form['income'])
    loan = float(request.form['loan'])
    term = float(request.form['term'])
    cibil = float(request.form['cibil'])

    input_data = [[income, loan, term, cibil]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)

    confidence = round(max(probability[0]) * 100, 2)

    # Loan decision
    if prediction == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    # Risk level logic
    if confidence >= 80:
        risk = "LOW"
    elif confidence >= 60:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return render_template(
        'index.html',
        prediction_text=result,
        confidence_text=f"Model Confidence: {confidence}%",
        risk_text=f"Risk Level: {risk}",
        confidence_value=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)