from django import forms

class CreateUserForm(forms.Form):
    participant_id = forms.IntegerField(label='Particpant ID', min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data['participant_id']:
            raise forms.ValidationError('You must enter a participant id.')