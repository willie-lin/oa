# Create your views here.
from django.http import HttpResponse
from io import StringIO
from random import randrange
from django.shortcuts import render


# def index()
# fruits = ['苹果', '草莓', '榴莲', '香蕉', '葡萄', '山竹', '蓝莓', '西瓜']


def index(request):
    # output = StringIO()
    # output.write('<html>\n')
    # output.write('<head>\n')
    # output.write('\t<meta charset="utf-8">\n')
    # output.write('\t<title>首页</title>')
    # output.write('</head>\n')
    # output.write('<body>\n')
    # output.write('\t<h1>Hello, World!</h1>\n')
    # output.write('\t<hr>\n')
    # output.write('\t<ol>\n')
    # for _ in range(3):
    #     rindex = randrange(0, len(fruits))
    #     output.write('\t\t<li>' + fruits[rindex] + '</li>\n')
    # output.write('\t</ol>\n')
    # output.write('\t</body>\n')
    # output.write('\t</html>\n')
    fruits = ['苹果', '草莓', '榴莲', '香蕉', '葡萄', '山竹', '蓝莓', '西瓜']
    start, end = 0, randrange(len(fruits))
    ctx = {
        'greeting': 'Hello, Django!',
        'num': end + 1,
        'fruits': fruits[start:end + 1]
    }
    # ctx = {
    #     'greeting': 'Hello, Django!',
    #     'num': end + 1,
    #     'fruits': fruits[start:end + 1]
    # }
    return render(request, 'index.html', ctx)


