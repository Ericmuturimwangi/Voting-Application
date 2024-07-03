from django.db import models
# creating a question class

class Question(models.Model):
    question_text = models.CharField ( max_length = 300, default='Default Question Text')
    pub_date = models.DateTimeField ('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField (max_length = 200, verbose_name = "Choice Text") 
    votes = models.IntegerField( default = 0, verbose_name= "Vote Count")

    def __str__(self):
        return self.choice_text

