from django import forms
from .models import Profile,Order



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {'pid':'Person ID','name':'Name','email':'Email','mno':'Mobile NO'}

        widgets = {'pid':forms.NumberInput(attrs={'placeholder':'ID.123','class':'form-control'}),
                   'name':forms.TextInput(attrs={'placeholder':'eg.Ajay Ingle','class':'form-control'}),
                   'email':forms.TextInput(attrs={'placeholder':'abc@gmail.com','class':'form-control'}),
                   'mno':forms.NumberInput(attrs={'placeholder':'+91XXXXXXXX','class':'form-control'})}



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        labels = {'profile':'Profile Detail','pname':'Product Name','status':'Status'}

        widgets = {'profile':forms.Select(attrs={'class':'form-control'}),
                   'pname':forms.TextInput(attrs={'placeholder':'eg.Shoes,Mobile,Laptop','class':'form-control'}),
                   'status':forms.TextInput(attrs={'placeholder':'eg.Delivered,return,shipped','class':'form-control'})}

