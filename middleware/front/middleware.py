from django.utils.deprecation import MiddlewareMixin


class MiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print('MY Middleware process_request')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('MY Middleware process_view')

    def process_response(self,request,response):
        print('My Middleware process_response')
        return response #必须返回response

    def process_exception(self,request,exception):
        print('My Middleware process_exception')


