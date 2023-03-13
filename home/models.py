from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from streamfields import blocks



class HomePageCarouselImages(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_image"),
    ]



class HomePage(RoutablePageMixin, Page):
    body = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
        ],
        null=True,
        blank=True
    )

    max_count = 1

    cta = StreamField(
        [
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )



    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, min_num=1, label="image"),
        ], heading="Carousel Images"), 
        StreamFieldPanel("cta"),
    ]

    @route(r'^subscribe/$')
    def the_subscribe_page(self,request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['a_special_test'] = "Hello world 123123"
        return render(request, "home/subscribe.html", context)