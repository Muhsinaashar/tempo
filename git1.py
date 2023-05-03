import requests

# Define the API endpoint you want to retrieve data from
api_endpoint = "https://jsonplaceholder.typicode.com/posts/1"

# Send a GET request to the API endpoint and store the response in a variable
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Access the JSON data in the response and print it in the terminal
    data = response.json()
    print(data[0])
else:
    print("Error retrieving data from API")