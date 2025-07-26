import os
import time
import subprocess
import webbrowser

def run_angular_frontend() -> None:
    """Run the Angular frontend development server and open it in the browser."""
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              "src", "frontend", "regulations-search")
    
    print("Starting Angular frontend server...")
    
    # Use subprocess to run npm start (which runs ng serve)
    # shell=True is needed for Windows
    process = subprocess.Popen(
        "npx ng serve --open",
        shell=True,
        cwd=frontend_dir
    )
    
    # Wait a bit to make sure the server starts
    time.sleep(5)
    
    # Open the browser if --open flag doesn't work
    webbrowser.open('http://localhost:4200')
    
    return process
