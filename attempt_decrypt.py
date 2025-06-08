#!/usr/bin/env python3
import subprocess, hashlib, sys, base64, os

BLOB_FILE = 'blob.txt'

# runtime assertion: ensure blob file exists and has expected header
if not os.path.exists(BLOB_FILE):
    raise FileNotFoundError('blob.txt missing')

with open(BLOB_FILE, 'rb') as f:
    data = f.read().strip()

assert data.startswith(b'U2FsdGVk'), 'blob does not start with OpenSSL Salted__ header'

# candidate passphrase transformations
candidates = [
    'thispassword',                    # as-is
    'thispassword\n',                  # trailing newline
    'THISPASSWORD',                    # uppercase
    'thispassword'.upper(),            # redundant but explicit
    'thispassword'[::-1],              # reversed
    'drowssap siht',                   # reversed with space
]

def decrypt(passphrase, use_sha):
    key = hashlib.sha256(passphrase.encode()).hexdigest() if use_sha else passphrase
    cmd = [
        'openssl', 'enc', '-aes-256-cbc', '-d', '-a',
        '-md', 'sha256', '-in', BLOB_FILE,
        '-pass', f'pass:{key}'
    ]
    # why: openssl may emit binary; decode ignoring errors
    res = subprocess.run(cmd, capture_output=True, text=True, errors='ignore')
    return res.returncode, res.stdout, res.stderr

for p in candidates:
    for flag in (False, True):
        rc, out, err = decrypt(p, flag)
        tag = 'sha256' if flag else 'raw'
        if rc == 0 and 'bad decrypt' not in err:
            print('SUCCESS', p, tag)
            print(out)
            sys.exit(0)
        else:
            # why: show failing attempt
            msg = err.strip().splitlines()[-1] if err.strip() else 'no err'
            print('FAILED', p, tag, msg)

print('No candidate succeeded')
