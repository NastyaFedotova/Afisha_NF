from django.shortcuts import render
from bmstu_lab.models import Cities, Events


def cities():
    return [
        {
            'id': 0,
            'city': 'Париж',
            'events': [
                {
                    'eventTitle': 'День влюбленных',
                    'description': 'Праздник католического происхождения, который отмечается 14 февраля во многих странах мира.',
                    'img': 'https://interesnoznat.com/wp-content/uploads/01_23.jpg'
                },
            ]
        },
        {
            'id': 1,
            'city': 'Рим',
            'events': [
                {
                    'eventTitle': 'La Tomatina',
                    'description': 'Праздник, в котором участники бросают помидоры и участвуют в помидорной борьбе исключительно в развлекательных целях.',
                    'img': 'https://festivalsherpa-wpengine.netdna-ssl.com/wp-content/uploads/2015/08/4.jpg'
                }
            ]
        },
        {
            'id': 2,
            'city': 'Москва',
            'events': [
                {
                    'eventTitle': 'Новый Год',
                    'description': 'Праздник, когда все люди страны едят оливье и селедку под шубой',
                    'img': 'https://moyidorogi.ru/wp-content/uploads/2019/08/01_1.jpg'
                },
                {
                    'eventTitle': '8 марта',
                    'description': 'Важный и всеми любимый праздник. 8 марта – это день, когда по всей стране разом пустеют цветочные магазины.',
                    'img': 'https://www.davno.ru/assets/images/cards/big/vosmoe-marta-596.jpg'
                }

            ],
        },
    ]


def GetCities(request):
    return render(request, 'cities.html', {'data': {
        'cities': cities()
    }})


def GetCity(request, id):
    return render(request, 'city.html', {'data': cities()[id]})
