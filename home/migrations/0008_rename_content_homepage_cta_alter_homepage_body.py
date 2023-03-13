# Generated by Django 4.1.7 on 2023-03-13 06:54

from django.db import migrations
import streamfields.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='content',
            new_name='cta',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streamfields.blocks.RichTextBlock()), ('simple_richtext', streamfields.blocks.SimpleRichTextBlock())], blank=True, null=True, use_json_field=None),
        ),
    ]