import requests
import os

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")

def run():
    print("Reset...")
    r = requests.post(f"{BASE_URL}/reset")
    print(r.json())

    for i in range(3):
        r = requests.post(f"{BASE_URL}/step", json={"action": "test"})
        print(r.json())

    r = requests.get(f"{BASE_URL}/state")
    print(r.json())

if __name__ == "__main__":
    run()