import random

from django.http import HttpResponse

words = ["napkelte",
         "naplemente",
         "nyugodt",
         "seprű",
         "sötét",
         "vihar",
         "villámlás",
         "veszélyes"
         ]


def index(request):
    return HttpResponse(f"The Hungarian word of the day is: {get_random_word()}")


def get_random_word():
    return random.choice(words)