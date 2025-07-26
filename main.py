"""Runs the backend and frontend."""
import os
import threading
import time
import subprocess
import webbrowser
from src.backend.run import backend

def run_angular_frontend():
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

def main():
    """Run both backend and frontend."""
    # Start the backend in a separate thread
    backend_thread = threading.Thread(target=backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Start the frontend
    frontend_process = run_angular_frontend()
    
    try:
        # Keep the main thread alive while the frontend is running
        while frontend_process.poll() is None:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        # Try to terminate the frontend process gracefully
        if frontend_process.poll() is None:
            frontend_process.terminate()

if __name__ == "__main__":
    main()
