from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField, StringField

class MovieReviewForms(FlaskForm):
    word = StringField('Word')
    reviewer = SelectField('Reviewer',
                       choices=[('part-time','Part-Time Reviewers'),
                                ('full-time','Full-Time Reviewers'),
                                ('all','All Reviewers')
                                ])
    picks = RadioField('Picks',
                       choices=[('picks','Yes'),
                                ('all','No')
                                ])
    submit = SubmitField('Submit')
