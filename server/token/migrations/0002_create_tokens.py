# Generated by Django 2.1.12 on 2019-09-12 04:30

import base64
import OpenSSL

from django.conf import settings
from django.db import migrations


def create_tokens(apps, schema_editor):
    private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM,
                                                 settings.PRIVATE_KEY)
    User = apps.get_model('auth', 'User')
    Token = apps.get_model('token', 'Token')
    db_alias = schema_editor.connection.alias
    for u in User.objects.using(db_alias).all():
        try:
            u.token
        except Token.DoesNotExist:
            id = str(u.pk)
            sig = OpenSSL.crypto.sign(private_key, id.encode(), 'sha256')
            token = id + ':' + base64.b64encode(sig).decode()
            Token.objects.create(user=u, token=token)


class Migration(migrations.Migration):

    dependencies = [
        ('token', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_tokens),
    ]