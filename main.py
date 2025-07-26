"""Runs the backend and frontend."""
import threading
import time
from src.backend.run import run
from src.frontend.run import run_angular_frontend


def make_backend_thread() -> None:
    # Start the backend in a separate thread
    backend_thread = threading.Thread(target=run)
    backend_thread.daemon = True
    backend_thread.start()

def main():
    """Run both backend and frontend."""
    # Start the backend
    make_backend_thread()
    
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
