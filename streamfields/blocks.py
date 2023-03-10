from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# TODO: add list block for icons
# TODO: update card block for blog posts

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )
    class Meta:
        template = "card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


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

class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold","italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, deafult='Learn More', max_length=40)

    class Meta:
        template = "cta_block.html"
        icon = "pick"
        label = "Call to Action"

class LinkStructValue(blocks.StructValue):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None


class ButtonBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=60)
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first")
    button_url = blocks.URLBlock(required=False, help_text="If added, this url will be used secondarily to the button page")

    class Meta:
        template = "button_block.html"
        icon = "pick"
        label = "Single Button"
        value_class = LinkStructValue