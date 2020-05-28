import json

from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework_jwt.settings import api_settings

from medical.address.models import Address
from medical.queueup.models import Queue
from medical.users.models import User
from medical.utils.helpers import response_success, response_fail, response_success_with_data
from medical.queueup.forms import QueueForm


@require_POST
@csrf_exempt
def lineup_view(request):
    """排队接口"""
    _POST = json.loads(request.body)
    user = get_user_instance(request)

    form = QueueForm(data=_POST)
    if form.is_valid() and user:
        # 表单校验通过
        address = form.cleaned_data['address'] # 医务室id
        address_id = address.pk
        if is_exist(address_id, user.pk):
            return response_fail("不能重复排队")

        queue = Queue(**form.cleaned_data)
        queue.user = user
        queue.save()
        queue_id = queue.pk

        if push(address_id, str(queue_id) + ":" + str(user.pk)):
            return response_success_with_data({"queue_id": queue.pk})

        return response_fail("排队失败")

    else:
        return response_fail("排队信息填写不完整")



@require_POST
@csrf_exempt
def cancel_lineup_view(request):
    """取消排队接口"""
    _POST = json.loads(request.body)
    user = get_user_instance(request)
    queue_id = _POST.get("queue_id") # 排队编号
    address_id = _POST.get('address')  # 医务室id
    if user and is_exist(address_id, user.pk):
        if pop(address_id, str(queue_id) + ":" + str(user.pk)):
            return response_success()

    return response_fail("取消排队失败")



@csrf_exempt
def get_queue_list_view(request):
    """获取当前队列情况"""
    return_data = []
    addresses = Address.objects.all()
    for address in addresses:
        obj = {}
        address_queue = get_list_with_name(address.pk) # 每个医务室的队列情况
        obj['id'] = address.pk
        obj['name'] = address.name
        obj['queue'] = address_queue
        obj['queue_num'] = len(address_queue)
        obj['queue_estimate_time'] = len(address_queue) * 5
        return_data.append(obj)

    return response_success_with_data(return_data)




def push(key, value):
    """
    排队
    :param key: 医务室的id
    :param value: Queue的uuid
    :return: boolean
    """
    try:
        queue = cache.get(key)
        if queue:
            # 已经有队列
            queue.append(value)
            cache.set(key, queue)
        else:
            # 还没有队列,设置新列表
            cache.set(key, [value])
    except Exception as e:
        raise e
    else:
        return True


def pop(key, value):
    """
    取消排队
    :param key: 医务室的id
    :param value: Queue的uuid
    :return: boolean
    """
    queue = cache.get(key)
    if queue:
        try:
            queue.remove(value)
        except ValueError:
            return False
        cache.set(key, queue)
        return True
    return False


def is_exist(key, user_id):
    """是否存在排队信息"""
    queue = cache.get(key)
    if queue:
        for q in queue:
            if ":" + str(user_id) in q:
                return True
    return False


def get_length(key):
    """获取队列长度"""
    queue = cache.get(key)
    if queue:
        return len(queue)
    return 0


def get_estimate(key):
    """获取预计排队用时"""
    length = get_length(key)
    if length > 0:
        return length * 5
    return 0


def get_list_with_name(key):
    """获取队列，以姓名填充"""
    return_data = []
    queue = cache.get(key) or []
    for q in queue:
        queue_id = q.split(':')[0]
        queue_instance = Queue.objects.get(pk=queue_id)
        return_data.append(queue_instance.name)
    return return_data


def get_jwt_token(request):
    jwt_token = request.headers['Authorization'] or None
    if jwt_token:
        try:
            token = jwt_token.split(' ')[1]
        except Exception as e:
            return None
        return token
    return None


def get_user_instance(request):
    try:
        token = get_jwt_token(request)
        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        user_dict = jwt_decode_handler(token)
        user_id = user_dict['user_id']
    except Exception as e:
        return None
    try:
        user = User.objects.get(id=int(user_id))
    except User.DoesNotExist:
        return None
    else:
        return user
