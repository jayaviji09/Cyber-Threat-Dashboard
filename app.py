from flask import Flask, render_template, request, redirect, url_for, session, flash
from threading import Timer
import sqlite3
import webbrowser
import socket
from datetime import datetime
from monitor import monitor_system

app = Flask(__name__)
app.secret_key = "cyber_security_deep_key_123"

# ------------------ DATABASE SETTINGS ------------------
def init_db():
    """Initializes the threat log database."""
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS threat_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT,
                packet_rate INTEGER,
                cpu_usage REAL,
                used_memory REAL,
                alert_count INTEGER,
                risk_level TEXT,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database Error: {e}")

# ------------------ CORE LOGIC FUNCTIONS ------------------
def get_system_ip():
    """Fetches the local IP of the host machine."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return "127.0.0.1"

def analyze_threats(packets, cpu, memory):
    """Deep analysis of micro-anomalies based on threshold logic."""
    alerts = 0
    reasons = []
    
    # Rule 1: Packet Rate Anomaly
    if packets > 7500:
        alerts += 1
        reasons.append("High Network Traffic")
    
    # Rule 2: CPU Spike Detection
    if cpu > 85:
        alerts += 1
        reasons.append("Processor Overload")
        
    # Rule 3: Memory Saturation
    if memory > 12.0:
        alerts += 1
        reasons.append("Memory Leakage Detected")
        
    # Final Risk Calculation
    if alerts >= 2:
        risk = "HIGH"
    else:
        risk = "LOW"
        
    return risk, alerts, reasons

# ------------------ ROUTES ------------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Hardcoded credentials for cyber threat monitoring
        if username == "cyber_threat" and password == "silent123":
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Credentials! Access Denied.")
            
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    
    # Live monitoring data
    live_cpu, live_mem = monitor_system()
    ip_addr = get_system_ip()

    if request.method == "POST":
        try:
        
            p_rate = int(request.form.get("packet_rate", 0))
            manual_cpu = float(request.form.get("active_cpu", 0)) 
            manual_mem = float(request.form.get("used_memory", 0)) 
            
        
            status, alert_total, issues = analyze_threats(p_rate, manual_cpu, manual_mem)
            
            
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO threat_logs 
                (ip_address, packet_rate, cpu_usage, used_memory, alert_count, risk_level, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (ip_addr, p_rate, manual_cpu, manual_mem, alert_total, status, datetime.now()))
            conn.commit()
            conn.close()
            
            return redirect(url_for("result", status=status, alerts=alert_total))
        except Exception as e:
            print(f"Error: {e}")
            return redirect(url_for("dashboard"))

    return render_template("dashboard.html", ip=ip_addr, cpu=live_cpu, mem=live_mem,
                           t_p="50,000", t_t="3600", t_c="100", t_m="16 GB")

@app.route("/result")
def result():
    if "user" not in session:
        return redirect(url_for("login"))
    
    status = request.args.get("status", "UNKNOWN")
    alerts = request.args.get("alerts", 0)
    return render_template("result.html", status=status, alerts=alerts)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ------------------ MAIN ------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import socket
from datetime import datetime
from monitor import monitor_system

app = Flask(__name__)
app.secret_key = "cyber_security_deep_key_123"

# ------------------ DATABASE SETTINGS ------------------
def init_db():
    """Initializes the threat log database."""
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS threat_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT,
                packet_rate INTEGER,
                cpu_usage REAL,
                used_memory REAL,
                alert_count INTEGER,
                risk_level TEXT,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database Error: {e}")

# ------------------ CORE LOGIC FUNCTIONS ------------------
def get_system_ip():
    """Fetches the local IP of the host machine."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return "127.0.0.1"

def analyze_threats(packets, cpu, memory):
    """Deep analysis of micro-anomalies based on threshold logic."""
    alerts = 0
    reasons = []
    
    # Rule 1: Packet Rate Anomaly
    if packets > 7500:
        alerts += 1
        reasons.append("High Network Traffic")
    
    # Rule 2: CPU Spike Detection
    if cpu > 85:
        alerts += 1
        reasons.append("Processor Overload")
        
    # Rule 3: Memory Saturation
    if memory > 12.0:
        alerts += 1
        reasons.append("Memory Leakage Detected")
        
    # Final Risk Calculation
    if alerts >= 2:
        risk = "HIGH"
    else:
        risk = "LOW"
        
    return risk, alerts, reasons

# ------------------ ROUTES ------------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Hardcoded credentials for cyber threat monitoring
        if username == "cyber_threat" and password == "silent123":
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Credentials! Access Denied.")
            
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    
    # Live monitoring data
    live_cpu, live_mem = monitor_system()
    ip_addr = get_system_ip()

    if request.method == "POST":
        try:
        
            p_rate = int(request.form.get("packet_rate", 0))
            manual_cpu = float(request.form.get("active_cpu", 0)) 
            manual_mem = float(request.form.get("used_memory", 0)) 
            
        
            status, alert_total, issues = analyze_threats(p_rate, manual_cpu, manual_mem)
            
            
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO threat_logs 
                (ip_address, packet_rate, cpu_usage, used_memory, alert_count, risk_level, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (ip_addr, p_rate, manual_cpu, manual_mem, alert_total, status, datetime.now()))
            conn.commit()
            conn.close()
            
            return redirect(url_for("result", status=status, alerts=alert_total))
        except Exception as e:
            print(f"Error: {e}")
            return redirect(url_for("dashboard"))

    return render_template("dashboard.html", ip=ip_addr, cpu=live_cpu, mem=live_mem,
                           t_p="50,000", t_t="3600", t_c="100", t_m="16 GB")

@app.route("/result")
def result():
    if "user" not in session:
        return redirect(url_for("login"))
    
    status = request.args.get("status", "UNKNOWN")
    alerts = request.args.get("alerts", 0)
    return render_template("result.html", status=status, alerts=alerts)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ------------------ MAIN ------------------
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/")

if __name__ == "__main__":
    init_db()  
    Timer(2, open_browser).start()
    print("Security Server Starting on Port 8000...")
    app.run(debug=False, port=8000)