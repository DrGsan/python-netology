from .models import Rubric


def top_rubric(request):
    return {'top_rubric': Rubric.objects.all()}

