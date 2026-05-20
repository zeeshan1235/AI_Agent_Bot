import os
import sys

def create_file(filename, content):
    with open(f"projects/{filename}", "w") as f:
        f.write(content)
    print(f"Success: {filename} created in projects folder.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python agent_engine.py <filename> <content>")
    else:
        create_file(sys.argv[1], sys.argv[2])
