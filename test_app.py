import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get('/ping/testuser')
    assert resp.status_code == 200


def test_prediction(client):
    test_data = {
                    "Gender" :  "Male",
                    "Married" : "No",
                    "ApplicantIncome": "200",
                    "LoanAmount": 100,
                    "Credit_history" : 0
        }
    resp = client.post('/predict', json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"prediction": "Loan Rejected"}