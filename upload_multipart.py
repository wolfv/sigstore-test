import os
import glob
from pathlib import Path
import hashlib
 
import requests
 
url = "https://beta.prefix.dev"
channel = f"{url}/api/v1/upload/wolf-channel"

def upload_with_attestation():
    fn = Path(list(glob.glob("output/**/signed-package*.conda"))[0])

    token = os.environ['PREFIX_API_KEY']
    attestation = os.environ['BUNDLE_PATH']
    data = fn.read_bytes()
 
    # skip if larger than 100Mb
    if len(data) > 100 * 1024 * 1024:
        print("Skipping", fn, "because it is too large")
        return
 
    name = fn.name
    sha256 = hashlib.sha256(data).hexdigest()
    sigstore_data = Path(attestation).read_bytes()

    headers = {
        "Authorization": f"Bearer {token}",
    }

    file_headers = {
        "X-file-name": name,
        "X-file-sha256": sha256,
        "Content-Length": str(len(data)),
    }

    files = {
        'file': (fn.name, data, 'application/octet-stream', file_headers),
        'attestation': ('sigstore', sigstore_data, 'application/json')
    }

    # Remove None values from files dict
    files = {k: v for k, v in files.items() if v is not None}

    r = requests.post(channel, files=files, headers=headers)
    print(f"Returned: {r.text}")
    print(f"Uploaded package {name} with status  {r.status_code}")
 

if __name__ == "__main__":
    upload_with_attestation()
