import requests
import pytest

# Base URL of your Django REST API
BASE_URL = 'http://10.8.147.49:8000'  # Adjust as needed

def test_get_endpoint():
    response = requests.get(f'{BASE_URL}/getting_data')
    actual_response = response.json()  # Capture the actual response
    print(actual_response)
    # expected_response = {'expected': 'response'}  # Define the expected response
    # assert response.status_code == 200
    # assert actual_response == expected_response, f"Expected {expected_response} but got {actual_response}"

def test_post_endpoint():
    data = {'key': 'value'}
    response = requests.post(f'{BASE_URL}/sending_data', json=data)
    actual_response = response.json()  # Capture the actual response
    expected_response = {'key': 'value'}  # Define the expected response
    assert response.status_code == 201
    assert actual_response == expected_response, f"Expected {expected_response} but got {actual_response}"

# Add more tests as needed
if __name__ == '__main__':
  #  test_post_endpoint()
    test_get_endpoint()