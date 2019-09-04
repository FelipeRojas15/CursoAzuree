# Generated by Django 2.2.2 on 2019-07-04 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_auto_20190704_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEtapas', models.CharField(choices=[('Grupo', 'Grupo'), ('Cuartos', 'Cuartos de Final'), ('Semifinal', 'Semifinal'), ('Final', 'Final')], default='Grupo', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Capitan')),
            ],
        ),
    ]
