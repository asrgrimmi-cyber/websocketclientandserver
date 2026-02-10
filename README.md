🚀 WebSocket-HTTP Bridge System
This system provides a bridge between a standard HTTP JSON API and a WebSocket Server. It allows legacy or web-based clients to interact with WebSocket services seamlessly.

📋 System Architecture
Client: Sends an HTTP POST request with a JSON payload to the Bridge.

Bridge (Server): Receives the HTTP request, establishes a temporary connection to the WebSocket server, forwards the data, and returns the response.

Target WS: The final destination processing the commands.

🛠️ Prerequisites
Before installation, ensure your Fedora (or other Linux) system is updated:

Python 3.9+

Pip (Python Package Manager)

Network access between the Client, Bridge, and Target WS.

📥 Installation Guide
1. Install Required Dependencies
Run the following command to install the necessary Python libraries:

Bash
pip install fastapi uvicorn websockets websocket-client requests
2. Configure the Bridge
In the Server Code, update the following variables to match your environment:

WEBSOCKET_URL: The address of your target WebSocket.

TARGET_IP & TARGET_PORT: Used for the startup diagnostic tool.

3. Firewall Configuration (Fedora)
If the Bridge and Client are on different machines, open port 5000:


sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload

🚀 Execution Instructions
Running the Bridge (Server)
Save the server code as bridge_server.py.

Start the server:

python3 bridge_server.py

Watch the Startup Diagnostic. If you see ✅, the bridge is ready.

Running the Client
Save the client code as bridge_client.py.

Update the BRIDGE_URL in the script to the IP of the Bridge server.

Run the client:
python3 bridge_client.py
