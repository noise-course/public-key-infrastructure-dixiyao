

import requests
import time

def test_web_server(server_url="http://localhost:8080", num_requests=5):
    for i in range(num_requests):
        try:
            print(f"Request #{i+1}:")
            response = requests.get(server_url, timeout=10)
            time.sleep(1)
                
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":

    # Test basic requests
    test_web_server(server_url="http://localhost:8080", num_requests=5)
