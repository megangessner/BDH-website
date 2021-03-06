# Generated by Django 2.1.dev20180415210700 on 2018-04-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(help_text='Enter Article Title', max_length=10000)),
                ('pubdate', models.DateField(auto_now=True)),
                ('text', models.CharField(help_text='Article Text Goes Here', max_length=1000000000)),
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('d', 'Draft'), ('p', 'Published')], default='d', help_text='Publication Status', max_length=1)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('rank', models.CharField(blank=True, choices=[('con', 'Contributing Writer'), ('ssw', 'Senior Staff Writer'), ('stw', 'Staff Writer')], default='con', help_text='Author Rank', max_length=3)),
                ('year', models.CharField(blank=True, choices=[('fr', 'Freshman'), ('so', 'Sophomore'), ('ju', 'Junior'), ('se', 'Senior')], default='', help_text='Author Year', max_length=2)),
                ('articles', models.ManyToManyField(to='newspaper.Article')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(help_text='Select Author Names', to='newspaper.Author'),
        ),
    ]
