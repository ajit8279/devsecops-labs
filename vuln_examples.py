# vuln_examples.py
# PURPOSE: intentionally vulnerable examples for CodeQL detection tests.
# DO NOT DEPLOY. Keep in test branch only.

import sqlite3
import subprocess
import pickle
import tempfile
import os

# 1) SQL Injection (string formatting with user input)
def sql_injection_example(user_input):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id INTEGER, name TEXT);")
    # vulnerable: user_input used directly in query string
    query = "SELECT * FROM users WHERE name = '%s'" % user_input
    cur.execute(query)
    return cur.fetchall()

# 2) Command Injection (shell construction)
def command_injection_example(cmd_part):
    # vulnerable: using shell=True style command construction via sh -c
    cmd = "ls " + cmd_part
    subprocess.run(["sh", "-c", cmd], check=False)

# 3) Use of eval on untrusted input
def eval_example(user_expr):
    return eval(user_expr)  # vulnerable

# 4) Insecure deserialization with pickle
def insecure_deserialize(data_bytes):
    return pickle.loads(data_bytes)  # vulnerable

# 5) Insecure temporary file
def insecure_tempfile():
    tmpname = tempfile.mktemp()  # vulnerable
    with open(tmpname, "w") as f:
        f.write("temp")
    return tmpname

# 6) Path Traversal
UPLOAD_DIR = "/tmp/uploads/"
def path_traversal_example(filename):
    path = UPLOAD_DIR + filename  # vulnerable
    return open(path, "rb").read()

# 7) Hardcoded secret
API_KEY = "hardcoded_secret_1234"

