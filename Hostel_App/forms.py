from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms import FileInput

from Hostel_App.models import Login, Student, Parent, Weekly_Foods, Notifications


# DateInput class
class DateInput(forms.DateInput):
    input_type = 'date'


# Registration form
class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username',)


# Student SignUp form

class StudForm(forms.ModelForm):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'autofocus': True}))
    dob = forms.DateField(label="Date Of Birth", widget=DateInput)
    ch = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    gender = forms.CharField(widget=forms.RadioSelect(choices=ch))
    d_ch = (
        ('initial', '--Please Select--'), ('CS', 'Computer Science'), ('EEE', 'EEE'), ('ECE', 'ECE'),
        ('Civil', 'Civil'),
        ('Mech', 'Mechanical'))
    department = forms.CharField(widget=forms.Select(choices=d_ch))
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])
    photo = forms.ImageField(widget=FileInput)  # in order to avoid currently field in update student form photo field

    # pip install image is needed
    class Meta:
        model = Student
        fields = (
            'name', 'dob', 'gender', 'address', 'department', 'phone', 'regno', 'photo',
            'email')

    def check_dob(self):
        date1 = self.cleaned_data['dob']
        age = (date.today() - date1).days / 365
        if age < 18:
            self.add_error('dob', 'Must be at least 18 years old to register!')
        return date1

    def check_dpt(self):
        dpt1 = self.cleaned_data['department']
        if dpt1 == 'initial':
            self.add_error('department', 'Choose a department')
        return dpt1

    def clean(self):
        cleaned_data = super().clean()
        self.check_dob()
        self.check_dpt()


# Parent SignUp form
class ParentForm(forms.ModelForm):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'autofocus': True}))
    ch_gen = (('Male', 'Male'), ('Female', 'Female'), ('Others', "Others"))
    gender = forms.CharField(widget=forms.RadioSelect(choices=ch_gen))
    ch_rel = (('Parent', 'Parent'), ('Guardian', 'Guardian'))
    relation = forms.CharField(widget=forms.RadioSelect(choices=ch_rel))
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])

    class Meta:
        model = Parent
        fields = (
            'name', 'gender', 'relation', 'address', 'regno', 'phone', 'email')


# Weekly Food entering form
class WeeklyFoodForm(forms.ModelForm):
    ch_day = (('initial', 'Choose a Day'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
              ('Thursday', 'Thursday'),
              ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))
    day = forms.ChoiceField(choices=ch_day)
    ch_brk = (('initial', 'Choose Breakfast'), ('Masala Dosa', 'Masala Dosa'), ('Idli & Chutney', 'Idli & Chutney'),
              ('Pathiri & Chicken Curry', 'Pathiri & Chicken Curry'), ('Appam & Veg Stew', 'Appam & Veg Stew'),
              ('Aloo Paratha', 'Aloo Paratha'),
              ('Puttu & Kadala Curry', 'Puttu & Kadala Curry'), ('Porotta & Beef Fry', 'Porotta & Beef Fry'))
    breakfast = forms.ChoiceField(choices=ch_brk)
    ch_lun = (('initial', 'Choose Lunch'), ('Ghee Rice & Chicken Curry', 'Ghee Rice & Chicken Curry'),
              ('Veg Biriyani', 'Veg Biriyani'), ('Chicken Biriyani', 'Chicken Biriyani'),
              ('Chicken Fried Rice', 'Chicken Fried Rice'), ('Veg Fried Rice', 'Veg Fried Rice'),
              ('Curd Rice', 'Curd Rice'), ('Veg Mixed Paratha', 'Veg Mixed Paratha'))
    lunch = forms.ChoiceField(choices=ch_lun)
    ch_din = (('initial', 'Choose Dinner'), ('Tandoori Chicken', 'Tandoori Chicken'),
              ('Roti & Chicken Tikka', 'Roti & Chicken Tikka'),
              ('Paratha & Paneer Butter Masala', 'Paratha & Paneer Butter Masala'), ('Veg SandWitch', 'Veg SandWitch'),
              ('Pineapple Raita', 'Pineapple Raita'), ('Naan & Butter Chicken', 'Naan & Butter Chicken'),
              ('Roti & Paneer Tikka', 'Roti & Paneer Tikka'))
    dinner = forms.ChoiceField(choices=ch_din)

    class Meta:
        model = Weekly_Foods
        fields = (
            'day', 'breakfast', 'lunch', 'dinner')

    def check_selected(self):
        day = self.cleaned_data['day']
        breakfast = self.cleaned_data['breakfast']
        lunch = self.cleaned_data['lunch']
        dinner = self.cleaned_data['dinner']
        if day == 'initial':
            self.add_error('day', 'Choose a day')
        if breakfast == 'initial':
            self.add_error('breakfast', 'Choose breakfast')
        if lunch == 'initial':
            self.add_error('lunch', 'Choose a lunch')
        if dinner == 'initial':
            self.add_error('dinner', 'Choose a dinner')

    def clean(self):
        cleaned_data = super().clean()
        self.check_selected()


# Notification form
class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notifications
        fields = ('date', 'description')

    def check_selected(self):
        date1 = self.cleaned_data['date']
        description = self.cleaned_data['description']
        if date1 < date.today():
            self.add_error('date', 'Date cannot be in the past!')
        return date1

    def clean(self):
        cleaned_data = super().clean()
        self.check_selected()
