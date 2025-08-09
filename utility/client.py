import requests
import systemChecks as checks

def collect_data():
    return {
        "hostname": checks.get_hostname() or None,
        "os_type": checks.get_os(),
        "disk_encrypted": checks.check_disk_encryption(),
        "os_up_to_date": checks.check_os_update(),
        "antivirus_active": checks.check_antivirus(),
        "inactivity_timeout": checks.get_inactivity_timeout()
    }

def send_data(payload):
    try:
        r = requests.post("http://127.0.0.1:8000/healthcheck", json=payload)
        return r.status_code, r.json()
    except Exception as e:
        return None, str(e)
