from django.db import models


# Create your models here.
class UserInfo(models.Model):
    nickName = models.CharField(max_length=20, verbose_name='昵称')
    passwd = models.CharField(max_length=40, verbose_name='密码')
    userName = models.CharField(max_length=20, null=True, verbose_name='收件人')
    email = models.EmailField(null=True, verbose_name='邮箱')
    phoneNumber = models.IntegerField(null=True, verbose_name='手机号码')
    address = models.CharField(max_length=40, null=True, verbose_name='地址')

    def __str__(self):
        return self.nickName

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
