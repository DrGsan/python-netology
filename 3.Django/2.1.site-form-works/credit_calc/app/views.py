from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    form_class = CalcForm
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        value = request.GET
        if value:
            result = int(value['initial_fee']) + int(value['initial_fee']) * float(value['rate'])/ 100
            context['result'] = round(result / float(value['rate']), 2)
            context['common_result'] = round(result, 2)
            context['form'] = CalcForm(request.GET)
            return self.render_to_response(context)
        else:
            context['form'] = CalcForm()
            return self.render_to_response(context)