Markdown# 🌉 Python HTTP-to-WebSocket Bridge

A lightweight, high-performance bridge built with **FastAPI** that converts incoming **HTTP POST** requests into **WebSocket** messages. This is ideal for allowing standard REST clients or web applications to communicate with WebSocket-based backend services.



## 🌟 Key Features
- **Startup Diagnostics:** Automatically checks network path and WebSocket availability before launching.
- **Synchronous Reliability:** Uses `websocket-client` for stable, blocking I/O operations.
- **Flexible Schema:** Accepts any valid JSON dictionary and forwards it directly.
- **Detailed Logging:** Real-time terminal output for tracking requests and server responses.

---

## 🛠️ Prerequisites

- **OS:** Fedora 39/40, Ubuntu, or any Linux/Windows/macOS environment.
- **Python:** 3.9 or higher.
- **Network:** Access to the target WebSocket server (default port `9001`).

---

## 📥 Installation

1. **Clone or Download** this repository to your Fedora machine.
2. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn websocket-client requests
⚙️ ConfigurationServer Configuration (bridge_server.py)Edit the variables at the top of the script to match your network:PythonWEBSOCKET_URL = "ws://127.0.0.1:9001" # The target WS server
TARGET_IP = "127.0.0.1"               # Used for network ping test
TARGET_PORT = 9001                    # Target port
Client Configuration (bridge_client.py)Update the BRIDGE_URL to point to your Bridge Server's IP address:PythonBRIDGE_URL = "[http://192.168.10.137:5000/bridge](http://192.168.10.137:5000/bridge)"
🚀 Usage1. Start the Bridge ServerRun the server on the machine acting as the bridge:Bashpython3 bridge_server.py
The bridge will perform a diagnostic check. If you see ✅, the path to the WebSocket is clear.2. Run the ClientFrom your client machine, execute:Bashpython3 bridge_client.py
📡 API EndpointsPOST /bridgeForwards data to the WebSocket.Request Body:JSON{
  "message": "ue_get",
  "ue_id": 1
}
Response:Returns the direct JSON response from the WebSocket server.🔧 TroubleshootingErrorMeaningSolution422 Unprocessable EntityData format error.Ensure client is sending a JSON object (dict).500 Internal ErrorConnection failed.Check if the target WS server is actually running.504 Gateway TimeoutConnection timed out.Check firewall settings on ports 5000 and 9001.Curl error (6)DNS Issue.Update /etc/resolv.conf with nameserver 8.8.8.8.📄 LicenseMIT License - Free to use and modify for any project.
---

### I want to ensure your deployment is as automated as possible. What information do you need from me to make this a world-class output? Ask me 5 targeted questions.

1. **Auto-Start:** Would you like the code for a **systemd unit file** so this bridge starts automatically whenever the Fedora server reboots?
2. **Docker:** Would you like a **Dockerfile** to containerize this application for easier deployment?
3. **Security:** Should we add a **Bearer Token** or API Key to the FastAPI headers to keep the bridge private?
4. **Environment Variables:** Would you like the script modified to read the `WEBSOCKET_URL` from an environment variable instead of hard-coding it?
5. **Testing:** Would you like a **bash script** that uses `curl` to test the bridge without needing a Python client?

**Would you like me to generate the `systemd` service file for you now?**
