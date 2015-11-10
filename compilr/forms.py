from django import forms

class NameForm(forms.Form):
	
	CATEGORIES = (  
    ('C', 'C'),
    ('CPP', 'C++'),
    ('CPP11', 'C++11'),
    ('CLOJURE', 'Clojure'),
    ('CSHARP', 'C#'),
    ('JAVA', 'Java'),
    ('JAVASCRIPT', 'JavaScript'),
    ('HASKELL', 'Haskell'),
    ('PERL', 'Perl'),
    ('PHP', 'PHP'),
    ('PYTHON', 'Python'),
    ('RUBY', 'Ruby'),
	)

	INPUT_CHOICE = ( 
		('input_check','Input'),
		)

	category = forms.ChoiceField(choices=CATEGORIES, required=True ,label='Select Language')
	code = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 30}))
	
	#iinput_checkbox = forms.BooleanField(attrs={'id': 'input_check'})

	iinput_checkbox = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple(attrs={'id': 'input_check'}), choices=INPUT_CHOICE)

	iinput_box = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10, 'id': 'input_box'}), label='Input')
	


