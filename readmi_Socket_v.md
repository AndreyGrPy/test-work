Socket Startup Guide to view top news

install library::

    import socket
    
create a local server::

    def run_json_file():
        try:
            server = some_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 2000))
            server.listen(4)
            while True:
                client_soket, adress = server.accept()
                data = client_soket.recv(1024).decode('utf-8')
                content = load_page(data)
                client_soket.send(content)
                client_soket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            server.close()
    
    
    def load_page(request_data):
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/json; charset=utf-8\r\n\r\n'
        path = request_data.split(' ')[1]
        response = ''

we get data from the repository and read::

        with open('hot_news_uk112.json', 'rb') as file:
            response = file.read()
        return HDRS.encode('UTF-8') + response
    
Important!!!
enter on the browser line   "http://127.0.0.1:2000/request"    to view::

    if __name__ == '__main__':
        run_json_file()