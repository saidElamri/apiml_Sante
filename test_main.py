from fastapi.testclient import TestClient
from main import app


client = TestClient(app)
def test_unitaire():
 patient_info = {"age":20,
    "gender":0,
    "pressurhigh":100,
    "pressurlow":60,
    "glucose":30,
    "kcm": 50,
    "troponin":40,
    "impluse":66
    }
 response_st=client.post("/predict_risk/", json=patient_info)
 assert response_st.status_code == 200
 result = response_st.json()
 assert "risk_status" in result
 assert result["risk_status"] in ["negative ", "positive"]
