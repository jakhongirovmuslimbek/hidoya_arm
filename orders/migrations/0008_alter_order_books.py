# Generated by Django 4.2.4 on 2023-11-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_location_book'),
        ('orders', '0007_remove_order_book_order_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(error_messages={'invalid': {'Bu kitobdan kutubxonada qolmagan.'}}, related_name='book_orders', to='books.book', verbose_name='kitoblar'),
        ),
    ]