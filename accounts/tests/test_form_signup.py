from django.test import TestCase

from ..forms import SignUpForm

class SignUpFormTest( TestCase ):
	form = SignUpForm()
	expected = ['username', 'email', 'password1', 'password2',]
	actual = list(form.fields)
	self.asssertSequenceEqual(expected, actual)