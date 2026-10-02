from django import forms


class TaskForm(forms.Form):
    title = forms.CharField()

    priority = forms.ChoiceField(
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
        ]
    )