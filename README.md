# 🛡️ Cyber Threat Monitoring & Prediction Dashboard

A professional web-based cybersecurity tool designed to monitor system health and predict potential security risks using real-time data inputs. This project features a modern dark-themed dashboard built with **Python Flask**.

---

## 🚀 Key Features
* **Live System Monitoring:** Automatically detects and displays System IP and baseline metrics (Packets, CPU Time, Memory).
* **Predictive Analysis:** Allows users to input manual data (Packet Rate, Active CPU %, Used Memory) to analyze threat risks.
* **Dynamic UI:** Sleek, cybersecurity-inspired dark mode interface with responsive side-by-side navigation buttons.
* **Automated Setup:** Includes a `.bat` script for one-click environment setup and server launch.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask Framework
* **Frontend:** HTML5, CSS3 (Custom Flexbox layout), JavaScript (ES6)
* **System Tools:** `psutil` (for real-time system monitoring)

---

## 📂 Project Structure
```text
├── app.py              # Main Flask Application
├── monitor.py          # Backend script for system resource monitoring
├── run_dashboard.bat   # Automation script to start the project
├── static/
│   ├── style.css       # Custom CSS for dashboard styling
│   └── script.js       # Frontend logic and navigation
└── templates/
    └── dashboard.html  # Main Dashboard User Interface
⚙️ How to Run
Clone/Download: Download the project files as a ZIP and extract them to a folder.

One-Click Start: Double-click the run_dashboard.bat file. This will:

Install necessary dependencies (Flask).

Start the local development server.

Access: Once the terminal says "Running on...", open your browser and go to:
http://127.0.0.1:8000/

🧠 How It Works
Dashboard Load: Upon launching, monitor.py fetches the current system status.

Input Phase: Users enter network traffic data (e.g., if you notice a spike in packet rates).

Risk Logic: When you click Predict Threat Risk, the Flask backend processes the inputs against safety thresholds.

Reporting: The system identifies if the current activity is "Normal" or a "Potential Threat" based on the resource consumption patterns.

