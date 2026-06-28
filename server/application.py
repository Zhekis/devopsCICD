import http.server
import socketserver

PORT = 8000

class TestMe():            #просто класс для демонстрации работы юнит тестов
    def take_five(self):
        return 4
    def port(self):
        return PORT
    
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
#веб-сервер отвечающий на любой запрос строкой из print по-дефолту показывает клиенту список файлов в текущем каталоге