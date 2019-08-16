转自：https://www.django.cn/course/show-20.html



# Django REST Framework快速入门

## 项目设置

创建一个名为tutorial的新Django项目，然后启动一个quickstart的新app。

```python
pip install djangorestframework
django-admin.py startapp quickstart
```

同步数据库

```python
python manage.py makemigrations
python manage.py migrate
```

创建初始用户admin，密码xxx。

```python
python manage.py createsuperuser
```

## Serializers

创建一个新文件tutorial/quickstart/serializers.py，来用作数据表示。

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
```

注：超链接是好的restful设计

## Views

打开tutorial/quickstart/views.py开始写视图代码

```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
```

使用viewsets可以使视图逻辑组织良好，并且非常简洁

## URLS

在`tutorial/urls.py`中开始写连接API的URLs

```python
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

因为使用的是viewsets而不是views，所以我们可以通过简单地使用路由器类注册视图来自动生成api的URL conf。

再次，如果我们需要对API URL进行更多的控制，我们可以简单地将其拉出来使用常规基于类的视图，并明确地编写URL conf。

## Settings

设置一些全局设置。打开分页，希望王我们的api只能由管理员使用。设置模块都在`tutorial/settings.py` 中。

```python
INSTALLED_APPS = (
    ...
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}
```

至此，Done，我们完成了。



## 测试我们的API

```python
python manage.py runserver 8888
```

直接使用浏览器，转到URL：http://127.0.0.1:8888/users/

```python
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8888/users/2/",
        "username": "宝山",
        "email": "",
        "groups": []
    },
    {
        "url": "http://127.0.0.1:8888/users/1/",
        "username": "admin",
        "email": "admin@126.com",
        "groups": []
    }
]
```

请先登录，页面才能看到返回结果，否则，看到的是如下内容

```python
HTTP 403 Forbidden
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Authentication credentials were not provided."
}
```



感谢Django中文社区！
