# Python-Port Scanner

 A Python-based multithreaded port scanner for cybersecurity 🔐 that detects open &amp; closed TCP ports on a target IP within a specified range. It uses ⚙️ socket programming for connection testing and 🚀 threading for faster scanning. Helps in network security analysis, vulnerability checking &amp; reconnaissance 🕵️

🛠️ Technologies Used
•  🐍 Python 3

📦 Modules Used
• 🔌 socket → TCP connection & port scanning
• 📥 sys → command-line arguments handling
• ⏱️ time → execution time calculation
• 🧵 threading → multithreaded scanning

🧠 Concepts Used
• 🌐 Network Programming
• 📡 TCP/IP Protocol
• 🚀 Multithreading
• 🔐 Cybersecurity Basics
• 🕵️ Port Scanning & Reconnaissance

✨ Features
• 🔎 Scans open and closed TCP ports
• 🌐 Supports IP address / hostname input
• 🎯 Custom port range selection (start to end port)
• 🚀 Fast scanning using multithreading
• 🧾 Shows service name for open ports
• ⏱️ Displays total scan time
• 📊 Shows total open and closed ports count

🚀 How to Run

▶️ Run the script
python Port_Scanner.py <TARGET> <START_PORT> <END_PORT>
💡 Example
python Port_Scanner.py 127.0.0.1 20 100

📊 Output Includes
• 🟢 Open ports with service names
• 🔴 Closed ports count
• ⏱️ Total scan time

