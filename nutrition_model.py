"""
ML Model for Food Nutrition Analysis (REAL MODEL)
"""

import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image


class NutritionDatabase:
    def __init__(self):
        self.food_database = {
            'चावल': {'name_en': 'Rice', 'calories': 130, 'protein': 2.7, 'carbs': 28, 'fat': 0.3, 'fiber': 0.4, 'sugar': 0.12},
            'आलू': {'name_en': 'Potato', 'calories': 77, 'protein': 1.7, 'carbs': 17, 'fat': 0.1, 'fiber': 2.1, 'sugar': 0.8},
            'टमाटर': {'name_en': 'Tomato', 'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'fat': 0.2, 'fiber': 1.2, 'sugar': 2.6},
            'केला': {'name_en': 'Banana', 'calories': 89, 'protein': 1.1, 'carbs': 23, 'fat': 0.3, 'fiber': 2.6, 'sugar': 12},
            'सेब': {'name_en': 'Apple', 'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2, 'fiber': 2.4, 'sugar': 10},
            'रोटी': {'name_en': 'Bread', 'calories': 265, 'protein': 9, 'carbs': 49, 'fat': 3.3, 'fiber': 6.8, 'sugar': 4.1},
        }

    def get_food_nutrition(self, food):
        return self.food_database.get(food, None)


class NutritionAnalyzerML:
    def __init__(self):
        self.db = NutritionDatabase()
        self.model = MobileNetV2(weights='imagenet')

    def predict_food(self, image_path):
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = self.model.predict(x)
        decoded = decode_predictions(preds, top=3)[0]

        labels = [label for (_, label, conf) in decoded if conf > 0.3]
        return self.map_food(labels)

    def map_food(self, labels):
        mapping = {
            'potato': 'आलू',
            'mashed_potato': 'आलू',
            'banana': 'केला',
            'apple': 'सेब',
            'tomato': 'टमाटर',
            'bread': 'रोटी',
            'rice': 'चावल',
        }

        result = []
        for label in labels:
            for key in mapping:
                if key in label.lower():
                    result.append(mapping[key])

        return list(set(result)) if result else ['अज्ञात']

    def analyze_nutrition(self, foods, portions=1.0):
        total = {'calories':0,'protein':0,'carbs':0,'fat':0,'fiber':0,'sugar':0}
        details = []

        for food in foods:
            data = self.db.get_food_nutrition(food)
            if data:
                details.append({'name_hi': food, 'name_en': data['name_en'], **data})

                for k in total:
                    total[k] += data[k] * portions

        return {
            'foods_detected': foods,
            'total_nutrition': total,
            'food_details': details
        }


nutrition_analyzer = NutritionAnalyzerML()