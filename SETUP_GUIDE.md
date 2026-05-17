# 🍎 खाद्य पोषण विश्लेषक (Food Nutrition Analyzer) - पूरी गाइड

## 📋 परिचय

यह एक पूर्ण ML-आधारित वेब एप्लीकेशन है जो खाद्य पदार्थों का विश्लेषण करता है और स्वास्थ्य सुझाव देता है। 
यह पूरी तरह से हिंदी में है और शहरी भारतीय लोगों के लिए डिज़ाइन किया गया है।

## 🚀 विशेषताएं

✅ **खाद्य पहचान** - AI आधारित खाद्य पदार्थों की पहचान
✅ **पोषण विश्लेषण** - कैलोरी, प्रोटीन, कार्ब्स और अन्य विस्तृत जानकारी
✅ **स्वास्थ्य सुझाव** - 15+ स्वास्थ्य स्थितियों के लिए व्यक्तिगत सुझाव
✅ **रिपोर्ट जेनरेशन** - डाउनलोड योग्य विस्तृत रिपोर्ट
✅ **उपयोगकर्ता प्रबंधन** - साइन अप, लॉगिन, डैशबोर्ड
✅ **मोबाइल फ्रेंडली** - सभी डिवाइस पर काम करता है
✅ **सुरक्षित** - एन्क्रिप्शन और डेटा सुरक्षा

## 📁 प्रोजेक्ट संरचना

```
food-nutrition-analyzer/
├── manage.py
├── requirements.txt
├── settings.py                 # Django settings
├── urls.py                     # URL routing
├── views.py                    # View functions और API
├── nutrition_model.py          # ML Model
│
├── templates/
│   ├── base.html              # Base template
│   ├── home.html              # Home page
│   ├── about.html             # About page
│   ├── services.html          # Services page
│   ├── generator.html         # Food analyzer
│   ├── contact.html           # Contact page
│   ├── policy.html            # Privacy policy
│   ├── login.html             # Login page
│   ├── signup.html            # Signup page
│   └── dashboard.html         # User dashboard
│
├── static/
│   ├── css/
│   │   └── style.css         # Additional styles
│   ├── js/
│   │   └── main.js           # JavaScript
│   └── images/               # Images and icons
│
├── media/
│   └── uploads/              # User uploaded images
│
└── ml_models/                # Trained ML models
    ├── food_classifier.pkl
    └── nutrition_predictor.pkl
```

## 💻 इंस्टॉलेशन गाइड

### चरण 1: आवश्यकताएं
- Python 3.8+
- pip (पायथन पैकेज मैनेजर)
- Virtual Environment

### चरण 2: Python Virtual Environment बनाएं

```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### चरण 3: डिपेंडेंसीज़ इंस्टॉल करें

```bash
pip install -r requirements.txt
```

यह आपके सभी आवश्यक पायथन पैकेज इंस्टॉल करेगा:
- Django 4.2.8
- Django REST Framework
- Pillow (इमेज प्रोसेसिंग)
- OpenCV (कंप्यूटर विजन)
- scikit-learn (ML)
- TensorFlow/PyTorch (डीप लर्निंग)

### चरण 4: Django सेटअप

```bash
# माइग्रेशन बनाएं
python manage.py makemigrations

# डेटाबेस में माइग्रेशन अप्लाई करें
python manage.py migrate

# सुपरयूजर (Admin) बनाएं
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: अपना पासवर्ड

# स्टेटिक फाइलें इकट्ठी करें
python manage.py collectstatic
```

### चरण 5: डेवलपमेंट सर्वर चलाएं

```bash
python manage.py runserver
```

अब अपने ब्राउज़र में जाएं: **http://localhost:8000**

## 🔑 Admin पैनल

Admin पैनल एक्सेस करने के लिए:
- URL: `http://localhost:8000/admin/`
- Username: (जो आपने createsuperuser में दिया था)
- Password: (आपका पासवर्ड)

## 📱 पेजेस और फीचर्स

### 1. **होम पेज** (`/`)
- हीरो सेक्शन
- विशेषताएं
- आंकड़े
- CTA बटन

### 2. **खाद्य विश्लेषक** (`/generator/`)
- तस्वीर अपलोड
- AI विश्लेषण
- पोषण परिणाम
- स्वास्थ्य स्थिति चयन
- रिपोर्ट जेनरेशन

### 3. **परिचय** (`/about/`)
- कंपनी की यात्रा
- टीम जानकारी
- मिशन और विजन
- मूल्य और तकनीक

### 4. **सेवाएं** (`/services/`)
- सभी सेवाओं का विवरण
- मूल्य निर्धारण
- FAQ
- प्रक्रिया

### 5. **संपर्क** (`/contact/`)
- संपर्क फॉर्म
- संपर्क जानकारी
- सोशल मीडिया लिंक्स

### 6. **गोपनीयता नीति** (`/policy/`)
- पूरी गोपनीयता नीति
- डेटा सुरक्षा
- उपयोगकर्ता अधिकार

## 🤖 ML मॉडल विवरण

### NutritionAnalyzerML क्लास

```python
from nutrition_model import nutrition_analyzer

# खाद्य पदार्थों का विश्लेषण
foods = nutrition_analyzer.predict_food('image.jpg')

# पोषण जानकारी
nutrition = nutrition_analyzer.analyze_nutrition(foods, portions=1.0)

# स्वास्थ्य सुझाव
report = nutrition_analyzer.generate_health_report(
    nutrition, 
    health_conditions=['मधुमेह', 'उच्च_रक्तचाप']
)
```

### समर्थित खाद्य पदार्थ

500+ भारतीय खाद्य पदार्थ:
- चावल, गेहूँ, दाल
- आलू, प्याज, टमाटर
- दूध, दही, रोटी
- मांस, अंडा
- सेब, केला
- और बहुत कुछ

### समर्थित स्वास्थ्य स्थितियाँ

15+ स्वास्थ्य स्थितियाँ:
- सामान्य (Normal)
- मधुमेह (Diabetes)
- उच्च रक्तचाप (High Blood Pressure)
- हृदय रोग (Heart Disease)
- मोटापा (Obesity)
- गुर्दा रोग (Kidney Disease)
- यकृत रोग (Liver Disease)
- और अधिक...

## 📊 API एंडपॉइंट्स

### सार्वजनिक API

```
GET  /api/home/                      # होम API
POST /api/signup/                    # साइन अप
POST /api/login/                     # लॉगिन
GET  /api/logout/                    # लॉगआउट
POST /api/analyze/                   # खाद्य विश्लेषण
POST /api/report/                    # रिपोर्ट जेनरेशन
GET  /api/health-conditions/         # स्वास्थ्य स्थितियाँ
GET  /api/foods/                     # खाद्य डेटाबेस
POST /api/contact/                   # संपर्क संदेश
```

### Example API Call

```python
# Python requests
import requests

# खाद्य विश्लेषण
response = requests.post(
    'http://localhost:8000/api/analyze/',
    files={'image': open('food.jpg', 'rb')}
)
data = response.json()
```

## 🎨 UI/UX विशेषताएं

### रंग योजना
- **Primary**: #FF6B6B (लाल)
- **Secondary**: #4ECDC4 (सियान)
- **Accent**: #FFE66D (पीला)
- **Dark**: #2C3E50
- **Light**: #ECF0F1

### एनिमेशन
- Slide In animations
- Fade transitions
- Bounce effects
- Hover effects
- Loading spinners
- Scroll-triggered animations

### टाइपोग्राफी
- Display font: Bold और आकर्षक
- Body font: सुलभ और पठनीय
- हिंदी और अंग्रेजी दोनों में

## 🔐 सुरक्षा उपाय

1. **CSRF सुरक्षा**: Django के built-in CSRF tokens
2. **पासवर्ड एन्क्रिप्शन**: bcrypt का उपयोग
3. **SSL/TLS**: HTTPS के लिए तैयार
4. **SQL Injection सुरक्षा**: ORM का उपयोग
5. **XSS सुरक्षा**: Template escaping
6. **Rate Limiting**: API throttling

## 🚀 प्रोडक्शन डिप्लॉयमेंट

### Heroku पर डिप्लॉय करने के लिए

```bash
# Procfile बनाएं
echo "web: gunicorn nutrition_project.wsgi" > Procfile

# Git से deploy करें
git init
git add .
git commit -m "Initial commit"
heroku create
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### AWS/DigitalOcean पर

```bash
# Requirements install
pip install -r requirements.txt

# Migrations
python manage.py migrate --settings=settings_production

# Static files
python manage.py collectstatic --settings=settings_production

# Gunicorn से run करें
gunicorn -w 4 nutrition_project.wsgi:application
```

## 📈 प्रदर्शन अनुकूलन

1. **Database Indexing**: अक्सर खोजे जाने वाले फील्ड्स को इंडेक्स करें
2. **Caching**: Redis का उपयोग करें
3. **Image Optimization**: Pillow से image compression
4. **CDN**: Static files के लिए CDN का उपयोग करें
5. **Database Query Optimization**: select_related() और prefetch_related()

## 🧪 टेस्टिंग

```bash
# Unit tests चलाएं
python manage.py test

# Coverage के साथ
coverage run --source='.' manage.py test
coverage report
```

## 📝 डेटाबेस स्कीमा

### User Model
```
- id (Primary Key)
- username (Unique)
- email (Unique)
- password (Hashed)
- first_name
- created_at
- updated_at
```

### Analysis Model
```
- id
- user_id (Foreign Key)
- image_path
- detected_foods
- nutrition_data (JSON)
- health_conditions (JSON)
- report_data (JSON)
- created_at
```

## 🐛 Troubleshooting

### समस्या: ModuleNotFoundError
```bash
# समाधान: सभी dependencies install करें
pip install -r requirements.txt
```

### समस्या: Database Error
```bash
# समाधान: Migrations चलाएं
python manage.py migrate
```

### समस्या: Static Files नहीं मिल रहीं
```bash
# समाधान: Static files collect करें
python manage.py collectstatic --clear
```

### समस्या: Image Upload काम नहीं कर रहा
```bash
# समाधान: uploads folder बनाएं
mkdir media/uploads
chmod 755 media/uploads
```

## 📞 समर्थन और योगदान

### Support के लिए संपर्क करें:
- **ईमेल**: support@foodnutritionanalyzer.in
- **फोन**: +91 98765 43210
- **वेबसाइट**: www.foodnutritionanalyzer.in

### योगदान देने के लिए:
1. Repository को fork करें
2. Feature branch बनाएं (`git checkout -b feature/AmazingFeature`)
3. Changes commit करें (`git commit -m 'Add some AmazingFeature'`)
4. Branch को push करें (`git push origin feature/AmazingFeature`)
5. Pull Request खोलें

## 📄 लाइसेंस

यह प्रोजेक्ट MIT लाइसेंस के तहत है।

## ✨ अतिरिक्त नोट्स

- यह एक शैक्षणिक परियोजना है
- प्रोडक्शन के लिए SECRET_KEY बदलें
- DEBUG=False सेट करें production में
- Proper logging सेटअप करें
- Regular backups लें
- SSL certificate setup करें

## 🎓 सीखने के संसाधन

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- OpenCV Documentation: https://docs.opencv.org/
- scikit-learn: https://scikit-learn.org/
- TensorFlow: https://www.tensorflow.org/

---

**अंतिम अपडेट**: जनवरी 2024
**संस्करण**: 1.0.0
**निर्मित**: Django + Python + Machine Learning

🙏 धन्यवाद खाद्य पोषण विश्लेषक का उपयोग करने के लिए!
