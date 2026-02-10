import requests
import json

def send_to_bridge(data_payload):
    # The URL of your Python Bridge Server
    BRIDGE_URL = "http://192.168.10.137:5000/bridge"
    
    # The structure expected by the FastAPI 'Payload' model
    payload = {
         "message": "ue_get",
         "ue_id" : 1, 
    }
    
    try:
        print(f"Sending data to bridge: {data_payload}")
        response = requests.post(BRIDGE_URL, json=payload, timeout=15)
        
        # Check if the HTTP request was successful (200 OK)
        response.raise_for_status()
        
        # The bridge returns the WebSocket's response
        result = response.json()
        print("Success! WebSocket responded with:")
        print(json.dumps(result, indent=2))
        return result

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.status_code == 502:
            print("Detail: The bridge couldn't connect to the WebSocket server.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Bridge Server. Is it running?")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    # Example message you want to send to the final WebSocket
    my_message = {
        "command": "get_system_status",
        "user_id": "admin_01"
    }
    
    send_to_bridge(my_message)