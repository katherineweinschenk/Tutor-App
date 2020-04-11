# Generated by Django 3.0.3 on 2020-04-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0007_auto_20200410_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_major',
            field=models.CharField(choices=[('African American and African Studies', 'African American and African Studies'), ('American Sign Language Program', 'American Sign Language Program'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Art', 'Art'), ('Astronomy', 'Astronomy'), ('Bioethics', 'Bioethics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Comparative Literature', 'Comparative Literature'), ('Creative Writing Program', 'Creative Writing Program'), ('Disability Studies', 'Disability Studies'), ('Drama', 'Drama'), ('East Asian Languages, Literatures & Cultures', 'East Asian Languages, Literatures & Cultures'), ('Economics', 'Economics'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought & Practice', 'Environmental Thought & Practice'), ('European Studies', 'European Studies'), ('French', 'French'), ('Global Studies', 'Global Studies'), ('History', 'History'), ('Jewish Studies', 'Jewish Studies'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Mathematics', 'Mathematics'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Mellon Indigenous Arts Program', 'Mellon Indigenous Arts Program'), ('Middle Eastern & South Asian Languages & Cultures', 'Middle Eastern & South Asian Languages & Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy & Law', 'Political Philosophy, Policy & Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages & Literatures', 'Slavic Languages & Literatures'), ('Sociology', 'Sociology'), ('Spanish, Italian & Portuguese', 'Spanish, Italian & Portuguese'), ('Statistics', 'Statistics'), ('Women, Gender & Sexuality', 'Women, Gender & Sexuality'), ('Writing & Rhetoric Program', 'Writing & Rhetoric Program'), ('n/a', 'n/a')], default='n/a', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_major',
            field=models.CharField(choices=[('African American and African Studies', 'African American and African Studies'), ('American Sign Language Program', 'American Sign Language Program'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Art', 'Art'), ('Astronomy', 'Astronomy'), ('Bioethics', 'Bioethics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Comparative Literature', 'Comparative Literature'), ('Creative Writing Program', 'Creative Writing Program'), ('Disability Studies', 'Disability Studies'), ('Drama', 'Drama'), ('East Asian Languages, Literatures & Cultures', 'East Asian Languages, Literatures & Cultures'), ('Economics', 'Economics'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought & Practice', 'Environmental Thought & Practice'), ('European Studies', 'European Studies'), ('French', 'French'), ('Global Studies', 'Global Studies'), ('History', 'History'), ('Jewish Studies', 'Jewish Studies'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Mathematics', 'Mathematics'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Mellon Indigenous Arts Program', 'Mellon Indigenous Arts Program'), ('Middle Eastern & South Asian Languages & Cultures', 'Middle Eastern & South Asian Languages & Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy & Law', 'Political Philosophy, Policy & Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages & Literatures', 'Slavic Languages & Literatures'), ('Sociology', 'Sociology'), ('Spanish, Italian & Portuguese', 'Spanish, Italian & Portuguese'), ('Statistics', 'Statistics'), ('Women, Gender & Sexuality', 'Women, Gender & Sexuality'), ('Writing & Rhetoric Program', 'Writing & Rhetoric Program'), ('n/a', 'n/a')], default='n/a', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutorposting',
            name='first_major',
            field=models.CharField(choices=[('African American and African Studies', 'African American and African Studies'), ('American Sign Language Program', 'American Sign Language Program'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Art', 'Art'), ('Astronomy', 'Astronomy'), ('Bioethics', 'Bioethics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Comparative Literature', 'Comparative Literature'), ('Creative Writing Program', 'Creative Writing Program'), ('Disability Studies', 'Disability Studies'), ('Drama', 'Drama'), ('East Asian Languages, Literatures & Cultures', 'East Asian Languages, Literatures & Cultures'), ('Economics', 'Economics'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought & Practice', 'Environmental Thought & Practice'), ('European Studies', 'European Studies'), ('French', 'French'), ('Global Studies', 'Global Studies'), ('History', 'History'), ('Jewish Studies', 'Jewish Studies'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Mathematics', 'Mathematics'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Mellon Indigenous Arts Program', 'Mellon Indigenous Arts Program'), ('Middle Eastern & South Asian Languages & Cultures', 'Middle Eastern & South Asian Languages & Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy & Law', 'Political Philosophy, Policy & Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages & Literatures', 'Slavic Languages & Literatures'), ('Sociology', 'Sociology'), ('Spanish, Italian & Portuguese', 'Spanish, Italian & Portuguese'), ('Statistics', 'Statistics'), ('Women, Gender & Sexuality', 'Women, Gender & Sexuality'), ('Writing & Rhetoric Program', 'Writing & Rhetoric Program'), ('n/a', 'n/a')], default='n/a', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutorposting',
            name='second_major',
            field=models.CharField(choices=[('African American and African Studies', 'African American and African Studies'), ('American Sign Language Program', 'American Sign Language Program'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Art', 'Art'), ('Astronomy', 'Astronomy'), ('Bioethics', 'Bioethics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Comparative Literature', 'Comparative Literature'), ('Creative Writing Program', 'Creative Writing Program'), ('Disability Studies', 'Disability Studies'), ('Drama', 'Drama'), ('East Asian Languages, Literatures & Cultures', 'East Asian Languages, Literatures & Cultures'), ('Economics', 'Economics'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought & Practice', 'Environmental Thought & Practice'), ('European Studies', 'European Studies'), ('French', 'French'), ('Global Studies', 'Global Studies'), ('History', 'History'), ('Jewish Studies', 'Jewish Studies'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Mathematics', 'Mathematics'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Mellon Indigenous Arts Program', 'Mellon Indigenous Arts Program'), ('Middle Eastern & South Asian Languages & Cultures', 'Middle Eastern & South Asian Languages & Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy & Law', 'Political Philosophy, Policy & Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages & Literatures', 'Slavic Languages & Literatures'), ('Sociology', 'Sociology'), ('Spanish, Italian & Portuguese', 'Spanish, Italian & Portuguese'), ('Statistics', 'Statistics'), ('Women, Gender & Sexuality', 'Women, Gender & Sexuality'), ('Writing & Rhetoric Program', 'Writing & Rhetoric Program'), ('n/a', 'n/a')], default='n/a', max_length=50),
        ),
    ]
