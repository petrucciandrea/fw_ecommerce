# Generated by Django 4.2.21 on 2025-07-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_is_returned_orderitem_review_alter_item_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='review',
            new_name='review_text',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='review_star',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
