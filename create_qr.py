import shutil
import socket
import http.server
import socketserver
import pyqrcode
import threading

def start_server_thread(httpd):
    httpd.serve_forever()

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    port = 3333
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = "http://" + s.getsockname()[0] + ":" + str(port)
    s.close()
    print("serving")

    try:
        httpd =  socketserver.TCPServer(("", port), Handler)
    except OSError:
        return IP
    server_thread = threading.Thread(target=start_server_thread, args=(httpd,))
    server_thread.start()

    print("serve??")
    return IP

def create_qr():
    print("Start archeive")
    shutil.make_archive('static/uploads/files', 'zip', 'static/uploads/user')
    print("ENd archeive")
    ip = start_server()
    print("Start server")

    all_files = f"{ip}/static/uploads/user/"
    zip_file = f"{ip}/static/uploads/files.zip"
    qr1 = pyqrcode.create(all_files)
    qr1.png("static/uploads/qr1.png", scale=5)
    qr2 = pyqrcode.create(zip_file)
    qr2.png("static/uploads/qr2.png", scale=5)

    return (all_files, zip_file)

