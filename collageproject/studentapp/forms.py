from django import forms
from .models import Student1, Subcenter, Course1, Total_fees


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ('name', 'birthdate', 'gender','blood_group','mail_id','address','course1','total_fees','center','subcenter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CHOICES=[('M','Male'),('F','Female')]
        self.fields['gender']=forms.CharField(label='gender',widget=forms.RadioSelect(choices=CHOICES))
        BG_CHOICES=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('O+','O+'),('AB-','AB-'),('O-','O-')]
        self.fields['blood_group'] = forms.ChoiceField(choices=BG_CHOICES)
        self.fields['subcenter'].queryset = Subcenter.objects.none()

        self.fields['total_fees'].queryset = Total_fees.objects.none()

        if 'center' in self.data:
            try:
                center_id = int(self.data.get('center'))
                self.fields['subcenter'].queryset = Subcenter.objects.filter(center_id=center_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['subcenter'].queryset = self.instance.center.subcenter_set.order_by('name')

        if 'course1' in self.data:
            try:
                course1_id = int(self.data.get('course1'))
                self.fields['total_fees'].queryset = Total_fees.objects.filter(course1_id=course1_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty course queryset
        # elif self.instance.pk:
        #     self.fields['total_fees'].queryset = self.instance.course1.total_fees_set.order_by('name')
