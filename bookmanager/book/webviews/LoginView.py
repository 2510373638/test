# 登录视图类
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.template.context_processors import csrf
import json


class LoginView(View):
    def get(self, req):
        # 1.获取模板
        template = loader.get_template('book/login.html')
        context = {}
        context.update(csrf(req))
        # 2.渲染模板
        resp = HttpResponse(template.render(context))
        resp.set_cookie('csrf_token', context['csrf_token'])
        return resp

    def post(self, req):
        data = json.loads(req.body.decode())
        uname = data.get('uname')
        pwd = data.get('pwd')
        if uname == 'abc' and pwd == '123':
            return JsonResponse({'result': '登录成功', 'uname': uname})
        else:
            return JsonResponse({'result': '账号密码错误', 'uname': None})
