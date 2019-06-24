import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()                           # 解析命令行参数
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)]) #建立请求处理集合
    # HTTPServer是一个单线程的非阻塞的HTTP服务器
    http_server = tornado.httpserver.HTTPServer(app)
    # 监听我们传入的端口值，建立了单进程的http服务
    http_server.listen(options.port)
    # 表示可以接受浏览器请求，相当于Javaweb中启动了tomcat服务器
    tornado.ioloop.IOLoop.instance().start()
   # 此时在浏览器输入localhost:8090
