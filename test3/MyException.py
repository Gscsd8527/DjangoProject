from django.http import HttpResponse
# 定义一个异常类，注册到setting的中间件中
from django.utils.deprecation import MiddlewareMixin
class Myexception(MiddlewareMixin):
    # def process_request(self, request):
    #     print("MD1里面的 process_request")
    #
    # def process_response(self, request, response):
    #     print("MD1里面的 process_response")
    #     return response
    def process_exception(request, response, exception):
        print('process_exception-----', exception)
        return HttpResponse(exception)
