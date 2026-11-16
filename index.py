from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

# Serve the CS Matching Game in the same folder as this file.
BASE_DIR = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000


class GameRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)


def main():
    os.chdir(BASE_DIR)
    server = ThreadingHTTPServer((HOST, PORT), GameRequestHandler)

    print("CS Matching Game is running.")
    print(f"Open this address in your browser: http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
