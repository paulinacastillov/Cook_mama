from re import A
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectMultipleField, validators, widgets
from wtforms.validators import DataRequired, Length

ALERGIAS = ["Mariscos", 
            "Gluten", 
            #"Maní",'Pescado',
            #'Frutos secos',
            'Lácteos'
            ]

INGREDIENTES = ['fresas', 'yogurt natural', 'estevia', 'naranja','jamon','caldo','pollo','pimienta','aceite_oliva','apio','cebolla','pimenton_pimiento','ajo','arroz']

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
    
class RequiredIfChoice(validators.DataRequired):
    # a validator which makes a field required if
    # another field is set and has a truthy value

    def __init__(self, other_field_name, desired_choice, *args, **kwargs):
        self.other_field_name = other_field_name
        self.desired_choice = desired_choice
        super(RequiredIfChoice, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        for value, label, checked in other_field.iter_choices():
            if label == self.desired_choice and checked:
                super(RequiredIfChoice, self).__call__(form, field)
                



class SearchForm(FlaskForm):
    input_ingredients = TextAreaField("input_text", validators=[DataRequired(), Length(max=1000)], default=None)
    input_allergies = MultiCheckboxField('Multibox', choices=ALERGIAS)
    searchButton = SubmitField("Search")
    