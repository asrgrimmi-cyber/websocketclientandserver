import time
import json
import socket
from fastapi import FastAPI, HTTPException
from websocket import create_connection  # From websocket-client

app = FastAPI()

# Configuration
WEBSOCKET_URL = "ws://127.0.0.1:9001"
TARGET_IP = "127.0.0.1"
TARGET_PORT = 9001

def check_connection_on_startup():
    """Checks the network and WS server before the API starts."""
    print("\n" + "="*40)
    print("STARTUP DIAGNOSTIC: Checking WebSocket Server...")

    # 1. TCP Port Check
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((TARGET_IP, TARGET_PORT))

    if result == 0:
        print(f"✅ Network: Port {TARGET_PORT} is reachable.")
    else:
        print(f"❌ Network: Port {TARGET_PORT} is CLOSED or UNREACHABLE.")
        print(f"   (Check if the service is running on {TARGET_IP})")
        return False

    # 2. WebSocket Handshake Check
    try:
        ws = create_connection(WEBSOCKET_URL, timeout=3)
        print(f"✅ WebSocket: Handshake successful at {WEBSOCKET_URL}.")
        ws.close()
        print("="*40 + "\n")
        return True
    except Exception as e:
        print(f"❌ WebSocket: Connection failed - {str(e)}")
        print("="*40 + "\n")
        return False

@app.post("/bridge")
async def bridge_to_websocket(payload: dict):
    print(f"\n--- New Request Received ---")
    print(f"Payload from Client: {payload}")

    ws = None
    try:
        ws = create_connection(WEBSOCKET_URL, timeout=10)
        time.sleep(5)
        print(ws.recv())
        # Send exactly what we received
        message_to_send = json.dumps(payload)
        ws.send(message_to_send)

        response = ws.recv()
        print(f"Received response: {response}")

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"websocket_response": response}

    except Exception as e:
        print(f"CRITICAL ERROR: {type(e).__name__} - {str(e)}")
        raise HTTPException(status_code=500, detail=f"Bridge failed: {str(e)}")

    finally:
        if ws:
            ws.close()

if __name__ == "__main__":
    import uvicorn
    # Perform the startup test
    connection_ok = check_connection_on_startup()

    if not connection_ok:
        print("⚠️ Warning: Bridge is starting but cannot reach the target server.")
        print("Requests to /bridge will likely fail until the network is fixed.\n")

    uvicorn.run(app, host="0.0.0.0", port=5000)
