# Generated by Django 5.1.1 on 2024-11-13 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='totaltest',
            name='budget_approach',
        ),
        migrations.RemoveField(
            model_name='cafewaittime',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='cafe_wait_time',
        ),
        migrations.RemoveField(
            model_name='dinnerchoice',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='dinner_choice',
        ),
        migrations.RemoveField(
            model_name='firststop',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='first_stop',
        ),
        migrations.RemoveField(
            model_name='luggageamount',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='luggage_amount',
        ),
        migrations.RemoveField(
            model_name='routepreference',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='route_preference',
        ),
        migrations.RemoveField(
            model_name='seadiscovery',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='sea_discovery',
        ),
        migrations.RemoveField(
            model_name='transportation',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='transportation',
        ),
        migrations.RemoveField(
            model_name='travelstyle',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='travel_style',
        ),
        migrations.RemoveField(
            model_name='tripplanningstyle',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='totaltest',
            name='trip_planning_style',
        ),
        migrations.AddField(
            model_name='totaltest',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='question.test'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BudgetApproach',
        ),
        migrations.DeleteModel(
            name='CafeWaitTime',
        ),
        migrations.DeleteModel(
            name='DinnerChoice',
        ),
        migrations.DeleteModel(
            name='FirstStop',
        ),
        migrations.DeleteModel(
            name='LuggageAmount',
        ),
        migrations.DeleteModel(
            name='RoutePreference',
        ),
        migrations.DeleteModel(
            name='SeaDiscovery',
        ),
        migrations.DeleteModel(
            name='Transportation',
        ),
        migrations.DeleteModel(
            name='TravelStyle',
        ),
        migrations.DeleteModel(
            name='TripPlanningStyle',
        ),
    ]
