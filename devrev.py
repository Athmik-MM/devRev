import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and endpoint from environment variables
api_key = os.getenv("DEVREV_API_KEY")
endpoint = os.getenv("DEVREV_API_URL")

# Define the data for the new work item
work_item_data = {
    "title": "New Task",
    "description": "This is a test task created using the DevRev API.",
    "status": "To Do",
    "priority": "Medium",
    "assignee": "John Doe",
    "due_date": "2024-04-10"
}

# Convert the data to JSON
json_data = json.dumps(work_item_data)

# Define headers including the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send POST request to create the work item
response = requests.post(endpoint, headers=headers, data=json_data)

# Check if the request was successful
if response.status_code == 201:
    print("Work item created successfully.")
    print("Work item details:")
    print(response.json())
else:
    print(f"Failed to create work item. Status code: {response.status_code}")
    print(response.text)
