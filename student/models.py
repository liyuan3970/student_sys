from django.db import models

# Create your models here.
class Student(models.Model):
    SEX_ITEMS=[
        (1,'男'),
        (2,'女'),
        (0,'未知'),
    ]
    STATUS_ITEMS=[
        (1,'申请'),
        (2,'通过'),
        (0,'拒绝'),
    ]
    name = models.CharField(max_length=128,verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS,verbose_name="性别")
    profession=models.CharField(max_length=128,verbose_name="职业")
    email=models.EmailField(verbose_name="Email")
    qq=models.CharField(max_length=128,verbose_name="QQ")
