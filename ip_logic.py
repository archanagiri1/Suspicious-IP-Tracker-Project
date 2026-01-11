import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    raise RuntimeError("ABUSEIPDB_API_KEY not found in environment")

def check_ip_malicious(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": True
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code != 200:
            raise Exception("API Error")

        data = response.json()["data"]

        abuse_score = data.get("abuseConfidenceScore", 0)
        country_code = data.get("countryCode", "N/A")
        usage_type = data.get("usageType", "Unknown")

        is_malicious = "Yes" if abuse_score >= 50 else "No"

        return {
            "ip": ip,
            "abuseScore": abuse_score,
            "isMalicious": is_malicious,
            "country": country_code,
            "usage": usage_type
        }

    except Exception as e:
        return {
            "ip": ip,
            "abuseScore": "Error",
            "isMalicious": "Error",
            "country": "N/A",
            "usage": "N/A"
        }


