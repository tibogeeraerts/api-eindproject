import requests
import json

# Create test admin function
def create_testadmin():
    adminexists = requests.get('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin/testadmin')
    if adminexists:
        print("INFO:     Test admin already exists!")
    else:
        username = "testadmin"
        password = "testadmin"
        data = json.dumps({"username": username, "password": password})
        requests.post('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin', data=data)

# Create test admin
create_testadmin()

# Authentication
headers = {
"Content-Type": "application/x-www-form-urlencoded"
}

request_data = {
    "client_id": "",
    "client_secret": "",
    "scope": "",
    "grant_type": "",
    "refresh_token": "",
    "username": "testadmin",
    "password": "testadmin"
}

# Requesting the token
tokenrequest = requests.post("https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/token", data=request_data, headers=headers)

# Extracting the token that came with the response
token = json.loads(tokenrequest.text)['access_token']

# Using the token in the headers of a secured endpoint
headerswithtoken = {
"accept" : "application/json",
"Authorization": f'Bearer {token}'
}

# Test POST quote
def test_post_quote():
    print("\n")
    content = "This is the post a test quote"
    data = json.dumps({"content": content})
    response = requests.post('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes', data=data)
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict['content'] == content

# Test GET all quotes
def test_get_all_quotes():
    print("INFO:     POST quote test passed!")
    response = requests.get('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes/all')
    assert response.status_code == 200
    response_dict = response.json()
    assert type(response_dict[0]['content']) == str #[0] because response is a list

# Test GET random quote
def test_get_random_quote():
    print("INFO:     GET all quotes test passed!")
    response = requests.get('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes/random')
    assert response.status_code == 200
    response_dict = response.json()
    assert type(response_dict['content']) == str

# Test GET last quote
def test_get_last_quote():
    print("INFO:     GET random quote test passed!")
    response = requests.get('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes/last')
    assert response.status_code == 200
    response_dict = response.json()
    assert type(response_dict['content']) == str

# Test PUT last quote
def test_put_last_quote():
    print("INFO:     GET last quote test passed!")
    content = "This is the update a test quote"
    data = json.dumps({"content": content})
    response = requests.put('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes/last', data=data)
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict['content'] == content

# Test DELETE last quote
def test_delete_last_quote():
    print("INFO:     PUT last quote test passed!")
    response = requests.delete('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/quotes/last')
    assert response.status_code == 200

# Test GET current admin
def test_get_current_admin():
    print("INFO:     DELETE last quote test passed!")
    response = requests.get('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin', headers=headerswithtoken)
    assert response.status_code == 200
    response_dict = response.json()
    assert type(response_dict['username']) == str
    assert response_dict['username'] == 'testadmin'

# Test POST admin
def test_post_admin():
    print("INFO:     GET current admin test passed!")
    username = "testadmin2"
    password = "testadmin2"
    data = json.dumps({"username": username, "password": password})
    response = requests.post('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin', data=data)
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict['username'] == username

# Print final test message
def test_print_passed_last_test():
    print("INFO:     POST admin test passed!")

    # Delete test admins
    requests.delete('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin/testadmin')
    requests.delete('https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/admin/testadmin2')
