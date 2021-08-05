from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    """Post Form."""

    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])
