from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')


games_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2', 'Witcher 3', 'Elden Ring', 'Dark Souls']


def games(request):
    context = {
        'games': games_list
    }
    return render(request, 'third_task/games.html', context)


def card(request):
    game = games_list[0]
    context = {
        'game': game
    }
    return render(request, 'third_task/card.html', context)
