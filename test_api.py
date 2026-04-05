
import requests

BASE_URL = "https://nonclinging-gabriel-bewhiskered.ngrok-free.dev"  # đổi thành URL của bạn

def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    print("GET /  OK:", r.json())

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    print("GET /health  OK:", r.json())

def test_predict_positive():
    r = requests.post(f"{BASE_URL}/predict", json={"text": "I love this so much!"})
    assert r.status_code == 200
    print("Positive test  OK:", r.json())

def test_predict_negative():
    r = requests.post(f"{BASE_URL}/predict", json={"text": "This is absolutely terrible."})
    assert r.status_code == 200
    print("Negative test  OK:", r.json())

def test_empty_input():
    r = requests.post(f"{BASE_URL}/predict", json={"text": ""})
    assert r.status_code == 400
    print("Empty input  OK:", r.json())

if __name__ == "__main__":
    test_root()
    test_health()
    test_predict_positive()
    test_predict_negative()
    test_empty_input()
    print("\nTat ca test deu pass!")
