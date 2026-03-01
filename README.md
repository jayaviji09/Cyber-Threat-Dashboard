Cyber Threat Monitoring & Prediction Dashboard
A web-based cybersecurity tool designed to monitor system parameters and predict potential threat risks using real-time data inputs. This project features a dark-themed, responsive UI with integrated system monitoring fields.

🚀 Features
System Monitoring: Displays real-time System IP, Total Packets, CPU Time, and Memory usage.

Manual Analysis: Allows users to input Packet Rate, Active CPU Time, and Used Memory for risk prediction.

Interactive UI: A modern dark-mode dashboard with a sleek "Glassmorphism" effect.

Smart Navigation: Includes "Previous" and "Predict" actions for seamless user experience.

Form Validation: Built-in JavaScript checks to prevent negative values or empty submissions.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Flexbox/Gradients), JavaScript (ES6)

Backend: Python (Flask Framework)

Styling: Custom CSS with a focus on Cyber-style aesthetics.

📂 Project Structure
Plaintext
├── app.py              # Main Python Flask application
├── static/
│   ├── style.css       # Custom styling and button layouts
│   └── script.js       # Navigation and validation logic
└── templates/
    └── dashboard.html  # Main UI Dashboard
⚙️ Installation & Setup
Clone the project:

Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Flask:
Make sure you have Python installed, then run:

Bash
pip install flask
Run the application:

Bash
python app.py
Access the Dashboard:
Open your browser and go to http://127.0.0.1:8000/

🛡️ Usage
Review the automatically detected system parameters.

Enter the current network Packet Rate.

Input the Active CPU % and Memory Usage (GB).

Click Predict Threat Risk to analyze the data.

Use the Previous button to navigate back safely without losing the session.
