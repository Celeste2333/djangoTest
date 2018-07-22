from django.shortcuts import render
from .models import UserMessage
# Create your views here.


def getstart(request):
    message = None   # 开始时message是没有数据的
    all_messages = UserMessage.objects.filter(name = "newbee")  # 过滤查找是否存在我们想要的数据
    if all_messages:  # 如果存在的话，返回值是一个列表
        message = all_messages[0]     # 取出返回值的第一个元素

    # if request.method == "POST":
    #     name = request.POST.get('name', '')     # 根据dict里面的键值对（key对应value值）来取出相应的属性，取不到默认为空。
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #
    #     user_message = UserMessage()  # 实例化对象
    #
    #     user_message.name = name   # 将取到的html的数据传入我们实例化的对象（数据库对象）.
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "2333"    # 随便写一个即可
    #
    #     user_message.save()   # 调用save方法进行保存
    #
    #     # filter取出符合指定条件的值，逗号代表and ,必须同时满足两个（这里只设定了2个）条件才返回值，否则为空。
    #     all_message = UserMessage.objects.filter(name='newbai', address='珠海')  # 数据库里保存着可以匹配到该条数据的一行。
    #
    #     all_message.delete()   # 删除操作：使用delete方法删除all_message
    #
    #     for message in all_message:
    #         # 删除取到的message对象
    #         message.detele()
    #         # print message.name

        return render(request, 'start.html',{
            "my_message": message
        })