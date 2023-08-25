from django import forms

class Advertisements81Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].wighet.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].wighet.attrs['class'] = 'form-check-input'
        self.fields['bu'].wighet.attrs['class'] = 'form-check-input'
    class Meta:
        model = Advertisements81
        fields = ('title', 'description', 'price', 'auction', 'bu', 'image')
    def clean_recipients(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Учи русский язык! Никаких вопросов в начале!')
        return title