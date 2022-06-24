from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, BooleanField 
from wtforms.validators import DataRequired 
	
class UploadForm(FlaskForm):
    file = FileField('Upload an image file for the evaluation', validators=[DataRequired()])
    submit = SubmitField('Upload')
    
class ResultForm(FlaskForm):
    submit = SubmitField('Ok')