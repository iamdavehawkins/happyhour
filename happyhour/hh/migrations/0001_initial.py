# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HappyHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('start_time', models.TimeField(verbose_name=b'start time', choices=[(datetime.time(0, 0), b'12:00 AM'), (datetime.time(0, 30), b'12:30 AM'), (datetime.time(1, 0), b'1:00 AM'), (datetime.time(1, 30), b'1:30 AM'), (datetime.time(2, 0), b'2:00 AM'), (datetime.time(2, 30), b'2:30 AM'), (datetime.time(3, 0), b'3:00 AM'), (datetime.time(3, 30), b'3:30 AM'), (datetime.time(4, 0), b'4:00 AM'), (datetime.time(4, 30), b'4:30 AM'), (datetime.time(5, 0), b'5:00 AM'), (datetime.time(5, 30), b'5:30 AM'), (datetime.time(6, 0), b'6:00 AM'), (datetime.time(6, 30), b'6:30 AM'), (datetime.time(7, 0), b'7:00 AM'), (datetime.time(7, 30), b'7:30 AM'), (datetime.time(8, 0), b'8:00 AM'), (datetime.time(8, 30), b'8:30 AM'), (datetime.time(9, 0), b'9:00 AM'), (datetime.time(9, 30), b'9:30 AM'), (datetime.time(10, 0), b'10:00 AM'), (datetime.time(10, 30), b'10:30 AM'), (datetime.time(11, 0), b'11:00 AM'), (datetime.time(11, 30), b'11:30 AM'), (datetime.time(12, 0), b'12:00 PM'), (datetime.time(12, 30), b'12:30 PM'), (datetime.time(13, 0), b'1:00 PM'), (datetime.time(13, 30), b'1:30 PM'), (datetime.time(14, 0), b'2:00 PM'), (datetime.time(14, 30), b'2:30 PM'), (datetime.time(15, 0), b'3:00 PM'), (datetime.time(15, 30), b'3:30 PM'), (datetime.time(16, 0), b'4:00 PM'), (datetime.time(16, 30), b'4:30 PM'), (datetime.time(17, 0), b'5:00 PM'), (datetime.time(17, 30), b'5:30 PM'), (datetime.time(18, 0), b'6:00 PM'), (datetime.time(18, 30), b'6:30 PM'), (datetime.time(19, 0), b'7:00 PM'), (datetime.time(19, 30), b'7:30 PM'), (datetime.time(20, 0), b'8:00 PM'), (datetime.time(20, 30), b'8:30 PM'), (datetime.time(21, 0), b'9:00 PM'), (datetime.time(21, 30), b'9:30 PM'), (datetime.time(22, 0), b'10:00 PM'), (datetime.time(22, 30), b'10:30 PM')])),
                ('end_time', models.TimeField(verbose_name=b'end time', choices=[(datetime.time(0, 0), b'12:00 AM'), (datetime.time(0, 30), b'12:30 AM'), (datetime.time(1, 0), b'1:00 AM'), (datetime.time(1, 30), b'1:30 AM'), (datetime.time(2, 0), b'2:00 AM'), (datetime.time(2, 30), b'2:30 AM'), (datetime.time(3, 0), b'3:00 AM'), (datetime.time(3, 30), b'3:30 AM'), (datetime.time(4, 0), b'4:00 AM'), (datetime.time(4, 30), b'4:30 AM'), (datetime.time(5, 0), b'5:00 AM'), (datetime.time(5, 30), b'5:30 AM'), (datetime.time(6, 0), b'6:00 AM'), (datetime.time(6, 30), b'6:30 AM'), (datetime.time(7, 0), b'7:00 AM'), (datetime.time(7, 30), b'7:30 AM'), (datetime.time(8, 0), b'8:00 AM'), (datetime.time(8, 30), b'8:30 AM'), (datetime.time(9, 0), b'9:00 AM'), (datetime.time(9, 30), b'9:30 AM'), (datetime.time(10, 0), b'10:00 AM'), (datetime.time(10, 30), b'10:30 AM'), (datetime.time(11, 0), b'11:00 AM'), (datetime.time(11, 30), b'11:30 AM'), (datetime.time(12, 0), b'12:00 PM'), (datetime.time(12, 30), b'12:30 PM'), (datetime.time(13, 0), b'1:00 PM'), (datetime.time(13, 30), b'1:30 PM'), (datetime.time(14, 0), b'2:00 PM'), (datetime.time(14, 30), b'2:30 PM'), (datetime.time(15, 0), b'3:00 PM'), (datetime.time(15, 30), b'3:30 PM'), (datetime.time(16, 0), b'4:00 PM'), (datetime.time(16, 30), b'4:30 PM'), (datetime.time(17, 0), b'5:00 PM'), (datetime.time(17, 30), b'5:30 PM'), (datetime.time(18, 0), b'6:00 PM'), (datetime.time(18, 30), b'6:30 PM'), (datetime.time(19, 0), b'7:00 PM'), (datetime.time(19, 30), b'7:30 PM'), (datetime.time(20, 0), b'8:00 PM'), (datetime.time(20, 30), b'8:30 PM'), (datetime.time(21, 0), b'9:00 PM'), (datetime.time(21, 30), b'9:30 PM'), (datetime.time(22, 0), b'10:00 PM'), (datetime.time(22, 30), b'10:30 PM')])),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('drink', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]
