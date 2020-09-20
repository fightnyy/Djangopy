from django.db import models

# Create your models here.
class Question (models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()

# makemigrations -> migrate 를 해줘야한다.
# makemigrations는 모델을 생성하거나 모델에 변화가 있을 경우에 실행해주는 명령어
# migrate는 모델을 생성해주는 명령어 (실제로 생성)