import io
import os.path
import sys
import subprocess

# Regenerate our cryptography.egg-info directory
subprocess.check_call([sys.executable, "setup.py", "egg_info"])

# Get test requires from requires.txt
test_requires = []
with io.open(
        os.path.join(
            os.path.dirname(__file__),
            "cryptography.egg-info",
            "requires.txt"
        ), encoding="utf8") as fp:
    in_test = False
    for line in fp:
        if line.strip() == "[test]":
            in_test = True
        elif in_test:
            if line.startswith("["):
                in_test = False
            else:
                test_requires.append(line.strip())

subprocess.check_call([sys.executable, "-m", "pip", "install"] + test_requires)
