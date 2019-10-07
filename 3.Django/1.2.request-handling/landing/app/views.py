from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click['original'] += 1
        print(f' клики {counter_click}')
        # return render_to_response('landing.html')
    elif from_landing == 'test':
        counter_click['test'] += 1
        print(counter_click)
        return render_to_response('landing_alternate.html')
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_arg = request.GET.get('ab-test-arg', 'не верный параметр')
    if ab_test_arg == 'original':
        counter_show['original'] += 1
        print(f'показы {counter_show}')
        return render_to_response('landing.html')
    elif ab_test_arg == 'test':
        counter_show['test'] += 1
        print(f'показы {counter_show}')
        return render_to_response('landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conversion = counter_click['test'] / counter_show['test']
    original_conversion = counter_click['original'] / counter_show['original']
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })


# 123