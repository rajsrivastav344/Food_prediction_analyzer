# 🍎 खाद्य पोषण विश्लेषक
## Food Nutrition Analyzer - Complete ML Project

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Django](https://img.shields.io/badge/django-4.2.8-darkgreen)

**एक आधुनिक AI-संचालित खाद्य विश्लेषण वेब प्लेटफॉर्म**

[विशेषताएं](#विशेषताएं) • [इंस्टॉलेशन](#installation) • [उपयोग](#usage) • [API](#api) • [योगदान](#contributing)

</div>

---

## 📋 विषय सूची

- [परिचय](#परिचय)
- [विशेषताएं](#विशेषताएं)
- [तकनीकी स्टैक](#तकनीकी-स्टैक)
- [इंस्टॉलेशन](#installation)
- [उपयोग](#usage)
- [API एंडपॉइंट्स](#api-endpoints)
- [स्क्रीनशॉट](#स्क्रीनशॉट)
- [योगदान](#contributing)
- [लाइसेंस](#license)

---

## परिचय

**खाद्य पोषण विश्लेषक** एक अत्याधुनिक वेब एप्लीकेशन है जो कृत्रिम बुद्धिमत्ता का उपयोग करके:

✨ **तस्वीर से खाद्य पदार्थों की पहचान** करता है
🔬 **पूरी पोषण जानकारी** प्रदान करता है  
⚕️ **स्वास्थ्य-आधारित सुझाव** देता है
📊 **विस्तृत विश्लेषण रिपोर्ट** बनाता है

यह प्लेटफॉर्म **100% हिंदी में** है और **शहरी भारतीयों** के लिए विशेष रूप से डिजाइन किया गया है।

### 🎯 उद्देश्य

- भारतीय शहरी जनता को स्वास्थ्यकर आहार संबंधी जानकारी प्रदान करना
- AI/ML का सामान्य मानुष को सुलभ बनाना
- डिजिटल स्वास्थ्य सेवा को लोकतांत्रिक बनाना

---

## विशेषताएं

### 🍽️ खाद्य विश्लेषण
- 📸 तस्वीर अपलोड करें (JPG, PNG, PDF)
- 🤖 AI-संचालित खाद्य पहचान
- ⚡ तुरंत विश्लेषण परिणाम

### 📊 पोषण जानकारी
- 🔢 कैलोरी, प्रोटीन, कार्ब्स, वसा
- 🌾 फाइबर और शर्करा विश्लेषण
- 📈 विजुअल न्यूट्रिशन बार

### ⚕️ स्वास्थ्य सुझाव
- 🏥 15+ स्वास्थ्य स्थितियों के लिए सुझाव
- ✅ उपयुक्त/अनुपयुक्त खाद्य पदार्थ
- ⚠️ विस्तृत चेतावनियां

### 📄 रिपोर्ट जेनरेशन
- 📥 डाउनलोड योग्य विस्तृत रिपोर्ट
- 🖨️ प्रिंट-तैयार प्रारूप
- 📊 डेटा विज़ुअलाइजेशन

### 👤 उपयोगकर्ता प्रबंधन
- 📝 साइन अप और पंजीकरण
- 🔐 सुरक्षित लॉगिन
- 📈 विश्लेषण इतिहास
- 💾 पसंदीदा सूची

### 📱 अन्य विशेषताएं
- 🌐 पूर्ण responsive design
- 🎨 सुंदर और आकर्षक UI
- ⚡ तेजी़ लोडिंग
- 🔒 डेटा एन्क्रिप्शन
- 📞 24/7 ग्राहक सहायता

---

## तकनीकी स्टैक

### 🔙 Backend
- **Framework**: Django 4.2.8
- **API**: Django REST Framework
- **Database**: SQLite (Dev) / PostgreSQL (Prod)
- **Language**: Python 3.8+

### 🤖 Machine Learning
- **विजन**: OpenCV, TensorFlow, PyTorch
- **मशीन लर्निंग**: scikit-learn, pandas
- **डेटा**: NumPy, scipy

### 🎨 Frontend
- **HTML5**: Semantic markup
- **CSS3**: Grid, Flexbox, Animations
- **JavaScript**: Vanilla JS (no frameworks)
- **Responsive**: Mobile-first design

### 📦 अन्य
- **Image Processing**: Pillow
- **Security**: Django security middleware
- **Deployment**: Gunicorn, Docker (optional)
- **Version Control**: Git

---

## Installation

### आवश्यकताएं
```
✓ Python 3.8 या उच्चतर
✓ pip (Python package manager)
✓ 2GB RAM न्यूनतम
✓ 500MB डिस्क स्पेस
```

### चरण 1️⃣: Repository क्लोन करें

```bash
git clone https://github.com/yourusername/food-nutrition-analyzer.git
cd food-nutrition-analyzer
```

### चरण 2️⃣: Virtual Environment बनाएं

```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### चरण 3️⃣: Dependencies इंस्टॉल करें

```bash
pip install -r requirements.txt
```

### चरण 4️⃣: Django सेटअप करें

```bash
# Migrations
python manage.py makemigrations
python manage.py migrate

# Admin User बनाएं
python manage.py createsuperuser

# Static files
python manage.py collectstatic --noinput
```

### चरण 5️⃣: Server चलाएं

```bash
python manage.py runserver
```

**✅ अब खोलें**: http://localhost:8000

---

## Usage

### 🏠 होम पेज
```
http://localhost:8000/
```
- परिचय और विशेषताएं देखें
- "शुरू करें" पर क्लिक करें

### 🔍 खाद्य विश्लेषण करें
```
http://localhost:8000/generator/
```

1. **तस्वीर अपलोड करें**
   - JPG, PNG, या PDF चुनें
   - या drag-drop करें

2. **विश्लेषण करें**
   - "विश्लेषण करें" बटन दबाएं
   - कुछ सेकंड प्रतीक्षा करें

3. **परिणाम देखें**
   - पहचाने गए खाद्य पदार्थ
   - पोषण विवरण
   - विजुअल बार चार्ट

4. **स्वास्थ्य सुझाव**
   - अपनी स्वास्थ्य स्थिति चुनें
   - रिपोर्ट जेनरेट करें
   - डाउनलोड करें

### 📖 अन्य पेज

| URL | विवरण |
|-----|--------|
| `/about/` | परिचय और टीम |
| `/services/` | सभी सेवाएं |
| `/contact/` | संपर्क फॉर्म |
| `/policy/` | गोपनीयता नीति |
| `/admin/` | Admin पैनल |

---

## API Endpoints

### 🔐 प्रमाणीकरण

```http
POST /api/signup/
Content-Type: application/json

{
  "username": "user123",
  "email": "user@example.com",
  "password": "password123",
  "first_name": "राज"
}
```

```http
POST /api/login/
Content-Type: application/json

{
  "username": "user123",
  "password": "password123"
}
```

### 🍽️ खाद्य विश्लेषण

```http
POST /api/analyze/
Content-Type: multipart/form-data

image: <file>
portions: 1.0
```

**Response:**
```json
{
  "status": "success",
  "foods_detected": ["चावल", "दाल"],
  "nutrition_data": {
    "foods_detected": [...],
    "total_nutrition": {
      "calories": 250,
      "protein": 8.5,
      "carbs": 45,
      "fat": 2.5,
      "fiber": 4.2,
      "sugar": 1.5
    },
    "food_details": [...]
  }
}
```

### 📊 रिपोर्ट जेनरेशन

```http
POST /api/report/
Content-Type: application/json

{
  "foods": ["चावल", "दाल"],
  "health_conditions": ["मधुमेह"],
  "portions": 1.0
}
```

### 📋 स्वास्थ्य स्थितियां

```http
GET /api/health-conditions/
```

**Response:**
```json
{
  "status": "success",
  "health_conditions": [
    {"hindi": "मधुमेह", "english": "Diabetes"},
    {"hindi": "उच्च_रक्तचाप", "english": "High Blood Pressure"},
    ...
  ]
}
```

### 🥘 खाद्य डेटाबेस

```http
GET /api/foods/
```

**Response:**
```json
{
  "status": "success",
  "foods": [
    {
      "hindi": "चावल",
      "english": "Rice",
      "nutrition": {
        "calories": 130,
        "protein": 2.7,
        ...
      }
    },
    ...
  ]
}
```

---

## Project Structure

```
food-nutrition-analyzer/
│
├── 📄 manage.py
├── 📄 settings.py              # Django configuration
├── 📄 urls.py                  # URL routing
├── 📄 views.py                 # Views and APIs
├── 📄 nutrition_model.py       # ML Model
├── 📄 requirements.txt         # Dependencies
├── 📄 SETUP_GUIDE.md           # Setup instructions
│
├── 📁 templates/
│   ├── base.html              # Base template
│   ├── home.html              # Home page
│   ├── generator.html         # Food analyzer
│   ├── about.html             # About page
│   ├── services.html          # Services
│   ├── contact.html           # Contact
│   ├── policy.html            # Privacy policy
│   ├── login.html             # Login
│   └── signup.html            # Signup
│
├── 📁 static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── 📁 media/
│   └── uploads/               # User uploads
│
└── 📁 ml_models/
    └── trained models
```

---

## 📚 समर्थित खाद्य पदार्थ (500+)

### 🌾 अनाज
चावल, गेहूँ, दाल, ज्वार, बाजरा, मकई

### 🥔 सब्जियां
आलू, प्याज, टमाटर, गाजर, बीन्स, मटर, लहसुन

### 🥛 डेयरी
दूध, दही, पनीर, मक्खन, घी

### 🥚 प्रोटीन
अंडा, मांस, मछली, मुर्गी

### 🍎 फल
सेब, केला, आम, संतरा, अनार, पपीता

### और भी बहुत कुछ...

---

## ⚕️ समर्थित स्वास्थ्य स्थितियां

1. 🟢 **सामान्य** - Normal
2. 🔴 **मधुमेह** - Diabetes
3. 🔴 **उच्च रक्तचाप** - High Blood Pressure
4. ❤️ **हृदय रोग** - Heart Disease
5. ⚖️ **मोटापा** - Obesity
6. 🫘 **गुर्दा रोग** - Kidney Disease
7. 🍽️ **यकृत रोग** - Liver Disease
8. **पेट संबंधी समस्याएं**
9. **हड्डी रोग**
10. **थायरॉयड**
11. और 5+ अन्य...

---

## 🎨 डिज़ाइन और UI/UX

### रंग पैलेट
```
🔴 Primary: #FF6B6B (लाल)
🔵 Secondary: #4ECDC4 (सियान)  
🟡 Accent: #FFE66D (पीला)
⚫ Dark: #2C3E50
⚪ Light: #ECF0F1
```

### Animations
- ✨ Smooth transitions
- 📤 Slide-in effects
- 🎯 Hover animations
- 📍 Scroll-triggered effects
- ⏱️ Loading spinners
- 🔄 Rotation effects

### Responsive
- 📱 Mobile-first approach
- 💻 Desktop optimized
- 🖥️ Tablet friendly
- ♿ Accessibility compliant

---

## 🔒 सुरक्षा विशेषताएं

- ✅ CSRF Protection
- ✅ SQL Injection Prevention
- ✅ XSS Protection
- ✅ Password Hashing (bcrypt)
- ✅ Rate Limiting
- ✅ HTTPS Ready
- ✅ Data Encryption
- ✅ Secure Headers

---

## 📊 डेटाबेस Schema

### Users Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255),
    first_name VARCHAR(100),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

### Analysis Table
```sql
CREATE TABLE analysis (
    id INT PRIMARY KEY,
    user_id INT FOREIGN KEY,
    image_path VARCHAR(500),
    detected_foods JSON,
    nutrition_data JSON,
    health_conditions JSON,
    report_data JSON,
    created_at TIMESTAMP
);
```

---

## 🚀 डिप्लॉयमेंट

### Heroku पर डिप्लॉय करें

```bash
# Procfile बनाएं
echo "web: gunicorn nutrition_project.wsgi" > Procfile

# Deploy
git push heroku main
heroku run python manage.py migrate
```

### Docker के साथ

```bash
# Dockerfile बनाएं
docker build -t food-analyzer .
docker run -p 8000:8000 food-analyzer
```

### AWS/DigitalOcean

```bash
# Install dependencies
pip install -r requirements.txt

# Run with Gunicorn
gunicorn -w 4 nutrition_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 🧪 परीक्षण

```bash
# Unit tests चलाएं
python manage.py test

# Coverage report
coverage run --source='.' manage.py test
coverage report
```

---

## 🐛 Known Issues और Limitations

- 🔹 पहली बार लोडिंग थोड़ी धीमी हो सकती है (ML मॉडल)
- 🔹 बहुत बड़ी तस्वीरें upload में समय ले सकती हैं
- 🔹 Offline mode अभी उपलब्ध नहीं है
- 🔹 Multiple भाषाओं का समर्थन आने वाला है

---

## 📈 Future Enhancements

- [ ] Voice input support
- [ ] AR camera integration
- [ ] Personalized meal plans
- [ ] Calorie tracking over time
- [ ] Social sharing features
- [ ] Multi-language support
- [ ] Mobile apps (iOS/Android)
- [ ] AI chatbot assistant
- [ ] Integration with fitness trackers
- [ ] Advanced analytics dashboard

---

## 💡 Tips और Tricks

### बेहतर परिणामों के लिए
1. 📸 अच्छी रोशनी में तस्वीर लें
2. 📐 खाने को सीधे ऊपर से फोटो करें
3. 🎯 खाने को पूरी तरह दिखाएं
4. 📷 स्पष्ट और फोकस्ड तस्वीर लें

### Performance Tips
1. ⚡ Cache को साफ करें (Ctrl+Shift+Del)
2. 📵 Offline mode में काम करें
3. 🗑️ पुरानी uploads हटाएं
4. 🔄 नियमित रूप से refresh करें

---

## 🤝 Contributing

हम आपके योगदान का स्वागत करते हैं! कृपया देखें [CONTRIBUTING.md](CONTRIBUTING.md)

### Git Workflow

```bash
# Fork करें
git clone https://github.com/yourusername/repo.git

# Feature branch बनाएं
git checkout -b feature/amazing-feature

# Changes commit करें
git commit -m 'Add amazing feature'

# Push करें
git push origin feature/amazing-feature

# Pull Request खोलें
```

---

## 📞 Support

### समर्थन के लिए संपर्क करें:
- 📧 **Email**: support@foodnutritionanalyzer.in
- 📱 **Phone**: +91 98765 43210
- 🌐 **Website**: www.foodnutritionanalyzer.in
- 💬 **Discord**: [Join Server](https://discord.gg/foodanalyzer)

### सामान्य समस्याएं

**Q: ModuleNotFoundError: No module named 'django'**
```bash
A: pip install -r requirements.txt
```

**Q: Database error**
```bash
A: python manage.py migrate
```

**Q: Static files नहीं मिल रहीं**
```bash
A: python manage.py collectstatic --clear
```

---

## 📄 License

यह प्रोजेक्ट **MIT License** के तहत है। विवरण के लिए [LICENSE](LICENSE) देखें।

---

## 🙏 Acknowledgments

- Django community
- OpenCV contributors
- scikit-learn team
- Indian nutrition database sources
- All our users and contributors

---

## 📊 Project Stats

- **Lines of Code**: 5000+
- **Pages**: 8
- **API Endpoints**: 10+
- **Foods in Database**: 500+
- **Health Conditions**: 15+
- **Animations**: 20+
- **Development Time**: 100+ hours

---

<div align="center">

### 🌟 अगर यह प्रोजेक्ट पसंद आया, तो ⭐ दें!

**Made with ❤️ for Indian Health**

[⬆ Top](#खाद्य-पोषण-विश्लेषक)

</div>
