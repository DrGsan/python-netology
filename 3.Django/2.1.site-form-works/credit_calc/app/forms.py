# from django import forms
#
#
# class CalcForm(forms.Form):
#     initial_fee = forms.IntegerField(label="Стоимость товара")
#     rate = forms.CharField(label="Процентная ставка")
#     months_count = forms.IntegerField(label="Срок кредита в месяцах")
#
#     def clean_initial_fee(self):
#         # валидация одного поля, функция начинающаяся на `clean_` + имя поля
#         initial_fee = self.cleaned_data.get('initial_fee')
#         if not initial_fee or initial_fee < 0:
#             raise forms.ValidationError("Стоимость товара не может быть отрицательной")
#         return initial_fee
#
#     def clean(self):
#         # общая функция валидации
#         return self.cleaned_data

from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.FloatField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        if not months_count or months_count < 0 or months_count > 360:
            raise forms.ValidationError("Срок кредита должен быть разумный")
        return months_count

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if not rate or rate < 0 or rate > 99:
            raise forms.ValidationError("Такая процентная ставка не возможна")
        return rate


    def clean(self):
        # общая функция валидации
        return self.cleaned_data