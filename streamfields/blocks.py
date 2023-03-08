from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichTextBlock(blocks.RichTextBlock):

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            features=[
            "bold",
            "italic",
            "link"
            ],
        )

    class Meta:
        template = "richtext_block.html"
        icon = "edit"
        label = "Simple RichText"