import os
import sys

def build_app(app_name):
    print(f"Creating application: {app_name}...")
    
    # Calculator ka simple code
    if "calculator" in app_name.lower():
        code = """
def calculator():
    print("Welcome to Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {a + b}")

if __name__ == "__main__":
    calculator()
"""
        filename = "calculator.py"
    else:
        code = "print('Project initialized')"
        filename = "project.txt"

    # File save karna
    with open(f"projects/{filename}", "w") as f:
        f.write(code)
    
    print(f"Successfully created {filename}")
    
    # Upload karna
    os.system("git add projects/*")
    os.system("git commit -m 'Auto-generated app'")
    os.system("git push origin main")
    print("Application uploaded to GitHub!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        build_app(sys.argv[1])
    else:
        print("Please provide an app name.")
