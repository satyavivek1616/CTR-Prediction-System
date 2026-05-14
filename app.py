from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

# =====================================================
# CREATE FLASK APP
# =====================================================

app = Flask(__name__)

# =====================================================
# LOAD TRAINED MODEL
# =====================================================

model = joblib.load('model.pkl')

# =====================================================
# HOME PAGE
# =====================================================

@app.route('/')
def home():

    return render_template('index.html')

# =====================================================
# PREDICTION ROUTE
# =====================================================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        # =============================================
        # CREATE INPUT DICTIONARY
        # =============================================

        input_data = {}

        # =============================================
        # NUMERICAL FEATURES
        # =============================================

        for i in range(1, 14):

            val = request.form.get(f'I{i}')

            if val == '':
                val = 0

            input_data[f'I{i}'] = float(val)

        # =============================================
        # DEFAULT CATEGORICAL FEATURES
        # =============================================

        for i in range(1, 27):

            input_data[f'C{i}'] = 0

        # =============================================
        # MISSING FLAGS
        # =============================================

        input_data['I5_missing_flag'] = 0
        input_data['I6_missing_flag'] = 0

        # =============================================
        # CREATE DATAFRAME
        # =============================================

        input_df = pd.DataFrame([input_data])

        input_df = input_df[model.feature_names_in_]

        # =============================================
        # PREDICT CTR PROBABILITY
        # =============================================

        ctr_probability = model.predict_proba(input_df)[0][1]

        ctr_percent = round(ctr_probability * 100, 2)

        # =============================================
        # GET BID VALUE
        # =============================================

        bid_value = request.form.get('bid_value')

        if bid_value == '':
            bid_value = 0

        bid_value = float(bid_value)

        # =============================================
        # CALCULATE EXPECTED VALUE
        # =============================================

        expected_value = round(ctr_probability * bid_value, 2)

        # =============================================
        # RETURN RESULT
        # =============================================

        return render_template(
            'index.html',
            prediction_text=f'Predicted CTR: {ctr_percent}%',
            bid_text=f'Bid Value: ${bid_value}',
            expected_text=f'Expected Revenue Value: ${expected_value}'
        )

    except Exception as e:

        return render_template(
            'index.html',
            prediction_text=f'Error: {str(e)}'
        )

# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == '__main__':

    app.run(debug=True)