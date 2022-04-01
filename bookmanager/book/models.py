from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''书籍类'''
    # 标题
    title = models.CharField(max_length=128)
    # 出版日期
    publish_date = models.DateField()
    # 软删除标志
    is_delete = models.BooleanField(default=False)
    # 显示标志
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # 元信息类
    class Meta:
        verbose_name = '书籍'


class PeopleInfo(models.Model):
    '''人类'''
    # 人名
    name = models.CharField(max_length=32)
    # 年龄
    age = models.IntegerField()
    # gender为性别，True表示男，GENDER_CHOICE为性别元组值
    GENDER_CHOICE = ((True, '男'), (False, '女'))
    # 性别
    gender = models.BooleanField(default=True, choices=GENDER_CHOICE)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人'
