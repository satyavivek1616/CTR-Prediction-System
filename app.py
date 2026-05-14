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
        # NUMERICAL FEATURES (I1 - I13)
        # =============================================

        for i in range(1, 14):

            val = request.form.get(f'I{i}')

            # Replace empty values with 0

            if val == '':
                val = 0

            input_data[f'I{i}'] = float(val)

        # =============================================
        # CATEGORICAL FEATURES (C1 - C26)
        # TEMPORARY DEFAULT VALUES
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

        # =============================================
        # REORDER COLUMNS EXACTLY LIKE TRAINING
        # =============================================

        input_df = input_df[model.feature_names_in_]

        # =============================================
        # PREDICT CLICK PROBABILITY
        # =============================================

        prediction = model.predict_proba(input_df)[0][1]

        prediction_percent = round(prediction * 100, 2)

        # =============================================
        # RETURN RESULT TO FRONTEND
        # =============================================

        return render_template(
            'index.html',
            prediction_text=f'Click Probability: {prediction_percent}%'
        )

    except Exception as e:

        return render_template(
            'index.html',
            prediction_text=f'Error: {str(e)}'
        )

# =====================================================
# RUN FLASK APPLICATION
# =====================================================

if __name__ == '__main__':

    app.run(debug=True)