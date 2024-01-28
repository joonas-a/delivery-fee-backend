from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

invalid_inputs = [
    {
        "cart_value": "onetwothree",
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": "qwerty",
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": "four",
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": 2024
    },
]

expected_fees = [1100, 852, 710, 410, 1280, 0, 1500]
valid_inputs = [
    {
        "cart_value": 100,
        "delivery_distance": 100,
        "number_of_items": 1,
        "time": "2024-01-16T17:30:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-26T17:30:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 300,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 13,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 20000,
        "delivery_distance": 2235,
        "number_of_items": 15,
        "time": "2024-01-15T13:00:00Z"
    },
    {
        "cart_value": 18000,
        "delivery_distance": 22350,
        "number_of_items": 300,
        "time": "2024-01-15T13:00:00Z"
    },
]


def test_fee_calc_invalid_data():
    for test_input in invalid_inputs:
        response = client.post("/api/calculate_fee", json=test_input)
        assert response.status_code == 400 or response.status_code == 422


def test_fee_calc_correct_data():
    for id, test_input in enumerate(valid_inputs):
        response = client.post("/api/calculate_fee", json=test_input)
        assert response.status_code == 200
        assert response.json() == {"delivery_fee": expected_fees[id]}
