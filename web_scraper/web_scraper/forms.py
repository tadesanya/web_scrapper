from django import forms


class ScrapeRequestForm(forms.Form):
    result_size = forms.IntegerField(label='Result Size', initial=5)

    def clean_result_size(self):
        result_size = self.cleaned_data['result_size']
        if not result_size:
            result_size = 5
        return result_size
