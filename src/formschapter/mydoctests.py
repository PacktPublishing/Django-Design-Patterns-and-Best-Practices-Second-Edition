"""
Code examples from Forms Chapter
#####################################################################

# Forms in Django
>>> from .forms import PersonDetailsForm

>>> f = PersonDetailsForm()
>>> print(f.as_p())
<p><label for="id_name">Name:</label> <input type="text" name="name" maxlength="100" required id="id_name" /></p>
<p><label for="id_age">Age:</label> <input type="number" name="age" required id="id_age" /></p>
>>> f.is_bound
False

>>> g = PersonDetailsForm({"name": "Blitz", "age": "30"})

>>> print(g.as_p())
<p><label for="id_name">Name:</label> <input type="text" name="name" value="Blitz" maxlength="100" required id="id_name" /></p>
<p><label for="id_age">Age:</label> <input type="number" name="age" value="30" required id="id_age" /></p>

>>> g.is_bound
True


# Why Does Data Need Cleaning?
>>> fill = {"name": "Blitz", "age": "30"}

>>> g = PersonDetailsForm(fill)

>>> g.is_valid()
True

>>> g.cleaned_data == {'age': 30, 'name': 'Blitz'}  # Dict ordering varies hence example changed
True

>>> type(g.cleaned_data["age"]) ==  type(1)  # Example changed as type represenation changes with Python version
True

"""
