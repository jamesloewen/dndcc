# Generated by Django 2.0 on 2018-02-11 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_saving_throw', models.BooleanField(default=False)),
                ('category', models.IntegerField(choices=[(1, 'STR'), (2, 'DEX'), (3, 'CON'), (4, 'WIS'), (5, 'INT'), (6, 'CHA')])),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('proficiency_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='background_proficiency_1', to='basics5e.Attribute')),
                ('proficiency_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='background_proficiency_2', to='basics5e.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('spells_type', models.IntegerField(choices=[(0, 'No spellcasting ability'), (1, 'Half caster'), (2, 'Full caster'), (3, 'Arcane trickster'), (4, 'Warlock')], default=0)),
                ('hit_dice', models.IntegerField(verbose_name='sides on hit dice for this class')),
                ('proficiencies', models.ManyToManyField(related_name='class_proficiencies', to='basics5e.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('handler_fn', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('handler_fn', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('class_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basics5e.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('type', models.IntegerField(choices=[(0, 'Item'), (1, 'Weapon'), (2, 'Armor'), (3, 'Clothing'), (4, 'Ring')], default=0)),
                ('description', models.TextField(blank=True)),
                ('handler_fn', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('size', models.IntegerField(choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Huge'), (6, 'Gargantuan')])),
                ('speed', models.IntegerField()),
                ('darkvision', models.IntegerField(verbose_name='Feet of darkvision. 0 if no darkvision')),
                ('ability_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ability_increases_1', to='basics5e.Attribute')),
                ('ability_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ability_increases_2', to='basics5e.Attribute')),
                ('ability_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability_increases_3', to='basics5e.Attribute')),
                ('ability_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability_increases_4', to='basics5e.Attribute')),
                ('languages', models.ManyToManyField(to='basics5e.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('level', models.IntegerField()),
                ('description', models.TextField()),
                ('is_ritual', models.BooleanField(default=False)),
                ('ritual_time', models.DurationField(blank=True, null=True)),
                ('verbal', models.BooleanField(default=True)),
                ('material', models.BooleanField(default=True)),
                ('somatic', models.BooleanField(default=True)),
                ('range', models.IntegerField(default=-1)),
                ('cast_time', models.CharField(max_length=80)),
                ('concentration_time', models.DurationField(default=0)),
                ('damage', models.CharField(blank=True, max_length=80)),
                ('handler_fn', models.CharField(blank=True, max_length=80)),
                ('overpower_fn', models.CharField(blank=True, max_length=80)),
                ('classes', models.ManyToManyField(to='basics5e.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='traits',
            field=models.ManyToManyField(to='basics5e.Trait'),
        ),
        migrations.AddField(
            model_name='feature',
            name='trait',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basics5e.Trait'),
        ),
    ]