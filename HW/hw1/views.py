import logging
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }


        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>

        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. </p>


        <p><a href="/about"> Обо мне </a></p>
    </body>
    </html>
    """
    logger.info(f'Index page accessed: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

        </style>
    </head>
    <body>

        <h1>Обо мне</h1>
        <p>Привет, меня зовут Виталий Осипов</p>

        <footer>
            <p>Привет МИР!!</p>
        </footer>
    </body>
    </html>
    """

    logger.info(f'About page accessed: {datetime.now()}')
    return HttpResponse(html)