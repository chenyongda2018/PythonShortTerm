import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import textwrap
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    # input参数将包含匹配处理函数正则表达式第一个括号里的字符串。
    def get(self,input):
        self.write(input[::-1]) # http相应的内容，会显示在浏览器中

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        width = self.get_argument("width",40)
        # textWrap用于装饰文本
        self.write(textwrap.fill(text,int(width)))

if __name__ == "__main__":
    # 解析命令行参数
    tornado.options.parse_command_line()
    # 建立请求处理集合
    app = tornado.web.Application(handlers=[
        # 访问http://localhost:8000/reverse/qwe   会显示ewq
        (r"/reverse/(\w+)",ReverseHandler),
        #
        (r"/wrap",WrapHandler)
    ])
    # HTTPServer是一个单线程的非阻塞的HTTP服务器
    http_server = tornado.httpserver.HTTPServer(app)
    # 监听我们传入的端口值，建立了单进程的http服务
    http_server.listen(options.port)
    # 表示可以接受浏览器请求，相当于Javaweb中启动了tomcat服务器
    tornado.ioloop.IOLoop.instance().start()
   # 此时在浏览器输入localhost:8090，会出现欢迎语