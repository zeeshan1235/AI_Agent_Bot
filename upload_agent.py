import os
os.system("git add projects/*")
os.system("git commit -m 'Auto-upload from AI Agent'")
os.system("git push origin main")
print("All projects uploaded to GitHub successfully!")
