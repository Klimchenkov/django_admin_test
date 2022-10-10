from django.db import models


class User(models.Model):
    '''
        Пользователь - User (id, email: str)
    '''

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Event(models.Model):
    '''
        Событие - Event (id, name: str)
    '''
    name = models.CharField(
        max_length=120,
        verbose_name="Имя"
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.name


class ProblemType(models.Model):
    '''
        Тип задачи - Problem Type (id, name: str)
    '''
    name = models.CharField(
        max_length=120,
        verbose_name="Имя"
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Тип задачи"
        verbose_name_plural = "Типы задач"

    def __str__(self):
        return self.name


class EventUserProblemType(models.Model):
    '''
        таблица, связывающая все сущности
        EventUserProblemType (id, event_id, user_id, problem_type_id)
    '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event_user_problem_type',
        verbose_name='Пользователь',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_user_problem_type',
        verbose_name='Событие',
    )
    problem_type = models.ForeignKey(
        ProblemType,
        on_delete=models.CASCADE,
        related_name='event_user_problem_type',
        verbose_name='Тип задачи',
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Связывающая таблица"
        verbose_name_plural = "Связывающие таблицы"

    def __str__(self):
        return f'{self.problem_type} {self.event} {self.user}'
