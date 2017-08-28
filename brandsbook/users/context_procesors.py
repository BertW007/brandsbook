import datetime


def my_footer(request):
    return {'now': datetime.datetime.now, 'author': 'Bobi'}
