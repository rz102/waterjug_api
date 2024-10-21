from fastapi.testclient import TestClient
from main import app
import json

# Integration testing
client = TestClient(app)
def test_API():
    response = client.post(
        "/water-jug-calculator",
        json = {
            "x_capacity": 2,
            "y_capacity": 10,
            "z_amount_wanted": 4
        }
    )
    assert response.status_code == 200
    assert json.loads(response.text) == {
        "solution":
        [
            {
                "step": 2,
                "bucketX": 2,
                "bucketY": 0,
                "action": "Fill bucket X"
            },
            {
                "step": 2,
                "bucketX": 0,
                "bucketY": 2,
                "action": "Transfer from bucket X to bucket Y"
            },
            {
                "step": 3,
                "bucketX": 2,
                "bucketY": 2,
                "action": "Fill bucket X"
            },
            {
                "step": 4,
                "bucketX": 0,
                "bucketY": 4,
                "action": "Transfer from bucket X to bucket Y"
            }
        ]
    }