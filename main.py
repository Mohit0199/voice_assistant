from app import app  # Import the Flask app from app.py
import logging

if __name__ == "__main__":
    # Print a message to indicate where the app is running
    host = "127.0.0.1"  # Define the host
    port = 5000        # Define the port

    print(f"Starting Flask app on http://{host}:{port}")
    logging.info(f"Starting Flask app on http://{host}:{port}")

    # Run the Flask app
    app.run(host=host, port=port, debug=True)
