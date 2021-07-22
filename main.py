def yingyong(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>How Are!</h1>']

from wsgiref.simple_server import make_server

a=900
httpd = make_server('', a, yingyong)
httpd.serve_forever()

