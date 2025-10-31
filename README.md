# 🏥 Cardiovascular Risk Prediction API

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive **FastAPI-based machine learning API** for cardiovascular risk assessment. This project provides real-time risk predictions based on patient health metrics using a trained machine learning model.

## 🚀 Features

- **Real-time Risk Prediction**: Instant cardiovascular risk assessment
- **RESTful API**: Complete CRUD operations for patient management
- **Machine Learning Integration**: Pre-trained model for accurate predictions
- **Data Validation**: Pydantic schemas for robust input/output validation
- **Auto-generated Documentation**: Interactive API documentation with Swagger UI
- **Persistent Storage**: SQLite database for patient data storage
- **Comprehensive Testing**: Unit tests for API reliability

## 📊 Health Metrics Processed

The API analyzes 8 key clinical indicators:

| Parameter | Description | Range | Type |
|-----------|-------------|-------|------|
| **Age** | Patient age | 0-120 years | Integer |
| **Gender** | Patient gender (0=Male, 1=Female) | 0+ | Integer |
| **Blood Pressure (High)** | Systolic blood pressure | 0+ | Float |
| **Blood Pressure (Low)** | Diastolic blood pressure | 0+ | Float |
| **Glucose** | Blood glucose levels | 0+ | Float |
| **KCM** | KCM medical parameter | 0+ | Float |
| **Troponin** | Cardiac biomarker levels | 0+ | Float |
| **Heart Rate** | Pulse/impulse rate | 0+ | Integer |

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cardiovascular-risk-api.git
   cd cardiovascular-risk-api
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

### Interactive Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### API Endpoints

#### 🏥 Patient Management

##### Create Patient with Risk Prediction
```http
POST /patients/
```

**Request Body**:
```json
{
  "age": 45,
  "gender": 0,
  "pressurhigh": 140.0,
  "pressurlow": 90.0,
  "glucose": 100.0,
  "kcm": 50.0,
  "troponin": 0.01,
  "impluse": 75
}
```

**Response**:
```json
{
  "id": 1,
  "age": 45,
  "gender": 0,
  "pressurhigh": 140.0,
  "pressurlow": 90.0,
  "glucose": 100.0,
  "kcm": 50.0,
  "troponin": 0.01,
  "impluse": 75,
  "status": "positive"
}
```

##### Get All Patients
```http
GET /patients/
```

##### Get Specific Patient
```http
GET /patients/{id}
```

##### Update Patient
```http
PUT /patients/{id}
```

#### 🧪 Risk Prediction

##### Standalone Risk Prediction
```http
POST /predict_risk/
```

**Request Body**:
```json
{
  "age": 45,
  "gender": 0,
  "pressurhigh": 140.0,
  "pressurlow": 90.0,
  "glucose": 100.0,
  "kcm": 50.0,
  "troponin": 0.01,
  "impluse": 75
}
```

**Response**:
```json
{
  "prediction_code": 1,
  "risk_status": "positive",
  "message": "Le modèle estime que le patient présente un positive"
}
```

## 🏗️ Project Structure

```
apiai/
├── main.py                 # FastAPI application main file
├── models.py              # SQLAlchemy database models
├── schemas.py             # Pydantic data validation schemas
├── crud.py                # Database CRUD operations
├── database.py            # Database configuration
├── test_main.py           # Unit tests
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── data2.csv              # Training dataset
├── health_model.pkl       # Trained ML model
├── label_encoder.pkl      # Data label encoder
└── patients.db            # SQLite database file
```

## 🧪 Testing

### Run Tests

```bash
pytest
```

### Run Specific Test

```bash
pytest test_main.py -v
```

### Test Coverage

The project includes unit tests for:
- API endpoint functionality
- Status code validation
- Response format validation
- Risk prediction accuracy

**Example Test Case**:
```python
def test_unitaire():
    patient_info = {
        "age": 20,
        "gender": 0,
        "pressurhigh": 100,
        "pressurlow": 60,
        "glucose": 30,
        "kcm": 50,
        "troponin": 40,
        "impluse": 66
    }
    response = client.post("/predict_risk/", json=patient_info)
    assert response.status_code == 200
    result = response.json()
    assert "risk_status" in result
    assert result["risk_status"] in ["positive", "negative"]
```

## 🔧 Architecture

### Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn**: Machine learning library for model training
- **SQLite**: Lightweight disk-based database
- **pytest**: Python testing framework
- **uvicorn**: ASGI server for FastAPI

### Core Components

#### 1. API Layer (`main.py`)
- FastAPI application initialization
- Endpoint definitions and routing
- ML model loading and prediction logic
- Error handling and HTTP responses

#### 2. Data Models (`models.py`)
- SQLAlchemy ORM models
- Database table definitions
- Field types and constraints

#### 3. Validation Schemas (`schemas.py`)
- Pydantic data validation
- API request/response schemas
- Type hints and field validation

#### 4. Business Logic (`crud.py`)
- Database CRUD operations
- Data persistence logic
- Entity relationship management

#### 5. Configuration (`database.py`)
- Database connection setup
- Session management
- SQLAlchemy configuration

## 🔮 Machine Learning Model

### Model Information
- **Algorithm**: Trained scikit-learn model
- **Features**: 8 clinical parameters
- **Output**: Binary classification (positive/negative risk)
- **Model File**: `health_model.pkl`
- **Label Encoder**: `label_encoder.pkl`

### Prediction Process
1. Input validation using Pydantic schemas
2. Feature transformation and normalization
3. Model inference using the trained classifier
4. Result interpretation and response formatting

## 🚀 Deployment

### Local Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Deployment
1. Use a production-grade ASGI server like Gunicorn
2. Set up environment variables for configuration
3. Use a reverse proxy (Nginx)
4. Implement proper logging and monitoring
5. Set up database backups

Example Gunicorn command:
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📝 API Usage Examples

### Python Example
```python
import requests

# Create patient with risk prediction
patient_data = {
    "age": 50,
    "gender": 1,
    "pressurhigh": 160.0,
    "pressurlow": 95.0,
    "glucose": 120.0,
    "kcm": 60.0,
    "troponin": 0.02,
    "impluse": 80
}

response = requests.post("http://localhost:8000/patients/", json=patient_data)
print(response.json())
```

### curl Examples
```bash
# Create patient
curl -X POST "http://localhost:8000/patients/" \
     -H "Content-Type: application/json" \
     -d '{
           "age": 45,
           "gender": 0,
           "pressurhigh": 140.0,
           "pressurlow": 90.0,
           "glucose": 100.0,
           "kcm": 50.0,
           "troponin": 0.01,
           "impluse": 75
         }'

# Get risk prediction
curl -X POST "http://localhost:8000/predict_risk/" \
     -H "Content-Type: application/json" \
     -d '{
           "age": 45,
           "gender": 0,
           "pressurhigh": 140.0,
           "pressurlow": 90.0,
           "glucose": 100.0,
           "kcm": 50.0,
           "troponin": 0.01,
           "impluse": 75
         }'
```

## ⚠️ Important Notes

### Clinical Use
- **This is a research/educational tool only**
- **Not for clinical decision making**
- **Consult with medical professionals for actual patient care**
- **Model accuracy and limitations should be thoroughly evaluated**

### Data Privacy
- Patient data is stored in SQLite by default
- Implement proper security measures for production use
- Comply with healthcare data regulations (HIPAA, GDPR, etc.)

### Model Performance
- Regularly evaluate model performance on new data
- Monitor for concept drift and model degradation
- Update the model periodically with fresh training data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow Python code style conventions
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## 📞 Support

For questions, issues, or contributions:

1. Check the [Issues](https://github.com/your-username/cardiovascular-risk-api/issues) page
2. Create a new issue for bugs or feature requests
3. Join discussions in existing issues
4. Contact the development team

---

**Built with ❤️ for healthcare innovation and machine learning research**
