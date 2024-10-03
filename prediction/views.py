import joblib
import os
from django.shortcuts import render

# Load the heart disease model (ensure the model file is saved in the app directory)
model_path = os.path.join(os.path.dirname(__file__), 'HeartDiseaseModel.pkl')
model = joblib.load(model_path)

def predict_view(request):
    result = None
    if request.method == 'POST':
        # Collect user input from the form
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        chest_pain = int(request.POST.get('chest_pain'))
        resting_bp = int(request.POST.get('resting_bp'))
        cholesterol = int(request.POST.get('cholesterol'))
        fasting_bs = int(request.POST.get('fasting_bs'))
        resting_ecg = int(request.POST.get('resting_ecg'))
        max_heart_rate = int(request.POST.get('max_heart_rate'))
        exercise_angina = int(request.POST.get('exercise_angina'))
        oldpeak = float(request.POST.get('oldpeak'))
        st_slope = int(request.POST.get('st_slope'))

        # Create input data list (in the correct order for your model)
        input_data = [
            age, sex, chest_pain, resting_bp, cholesterol,
            fasting_bs, resting_ecg, max_heart_rate,
            exercise_angina, oldpeak, st_slope
        ]

        # Predict using the loaded model
        prediction = model.predict([input_data])

        # Map prediction to readable result
        if prediction == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

    return render(request, 'prediction/index.html', {'result': result})
