import re
from ip_logic import analyze_logs

# Read logs from file
with open("server_logs.txt", "r") as file:
    logs = file.read()

results = analyze_logs(logs)

print("\n🔍 Suspicious IP Analysis Report\n")

for r in results:
    print(f"IP: {r['ip']} | Attempts: {r['attempts']} | Risk: {r['risk']}")

