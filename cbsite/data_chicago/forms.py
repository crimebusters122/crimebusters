from django import forms


years = [('ALL YEARS', 'ALL YEARS'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
            ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'),
            ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'),
            ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'),
            ('2017', '2017'), ('2018', '2018')]

crimes = [('ALL CRIMES', 'ALL CRIMES'),
 ('MOTOR VEHICLE THEFT', 'MOTOR VEHICLE THEFT'),
 ('ROBBERY', 'ROBBERY'),
 ('ASSAULT', 'ASSAULT'),
 ('BATTERY', 'BATTERY'),
 ('PROSTITUTION', 'PROSTITUTION'),
 ('THEFT', 'THEFT'),
 ('OTHER OFFENSE', 'OTHER OFFENSE'),
 ('NARCOTICS', 'NARCOTICS'),
 ('BURGLARY', 'BURGLARY'),
 ('OFFENSE INVOLVING CHILDREN', 'OFFENSE INVOLVING CHILDREN'),
 ('GAMBLING', 'GAMBLING'),
 ('DECEPTIVE PRACTICE', 'DECEPTIVE PRACTICE'),
 ('WEAPONS VIOLATION', 'WEAPONS VIOLATION'),
 ('SEX OFFENSE', 'SEX OFFENSE'),
 ('CRIMINAL DAMAGE', 'CRIMINAL DAMAGE'),
 ('CRIMINAL TRESPASS', 'CRIMINAL TRESPASS'),
 ('CRIM SEXUAL ASSAULT', 'CRIM SEXUAL ASSAULT'),
 ('HOMICIDE', 'HOMICIDE'),
 ('STALKING', 'STALKING'),
 ('PUBLIC PEACE VIOLATION', 'PUBLIC PEACE VIOLATION'),
 ('ARSON', 'ARSON'),
 ('INTIMIDATION', 'INTIMIDATION'),
 ('INTERFERENCE WITH PUBLIC OFFICER', 'INTERFERENCE WITH PUBLIC OFFICER'),
 ('KIDNAPPING', 'KIDNAPPING'),
 ('LIQUOR LAW VIOLATION', 'LIQUOR LAW VIOLATION'),
 ('OBSCENITY', 'OBSCENITY'),
 ('NON-CRIMINAL', 'NON-CRIMINAL'),
 ('PUBLIC INDECENCY', 'PUBLIC INDECENCY'),
 ('CONCEALED CARRY LICENSE VIOLATION', 'CONCEALED CARRY LICENSE VIOLATION'),
 ('HUMAN TRAFFICKING', 'HUMAN TRAFFICKING'),
 ('OTHER NARCOTIC VIOLATION', 'OTHER NARCOTIC VIOLATION'),
 ('RITUALISM', 'RITUALISM'),
 ('NON-CRIMINAL (SUBJECT SPECIFIED)', 'NON-CRIMINAL (SUBJECT SPECIFIED)'),
 ('NON - CRIMINAL', 'NON - CRIMINAL'),
 ('DOMESTIC VIOLENCE', 'DOMESTIC VIOLENCE')]

tooltips = [('yes', 'Yes'), ('no', 'No')]


class InputForm(forms.Form):
    yearfield = forms.CharField(label="Year", \
                    widget=forms.Select(choices=years), required=False)
    crimefield = forms.CharField(label="Crime type", \
                    widget=forms.Select(choices=crimes), required=False)
    tooltipfield = forms.CharField(label="Tooltips?", \
                    widget=forms.Select(choices=tooltips), required=False)
    datapointfield = forms.CharField(label="How many data points?", \
                    max_length=100, required=False)



