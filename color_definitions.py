"""Color definitions for various CSS frameworks."""

from collections import namedtuple
from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _

Color = namedtuple("Color", ["name", "bg_css_class", "text_css_class"])


class Bootstrap5(Enum):
    BLUE = Color("Blue", "bg-primary", "text-primary")
    GREEN = Color("Green", "bg-success", "text-success")
    YELLOW = Color("Yellow", "bg-warning", "text-warning")
    RED = Color("Red", "bg-danger", "text-danger")
    PURPLE = Color("Purple", "bg-purple", "text-purple")
    INDIGO = Color("Indigo", "bg-indigo", "text-indigo")
    PINK = Color("Pink", "bg-pink", "text-pink")
    ORANGE = Color("Orange", "bg-orange", "text-orange")
    TEAL = Color("Teal", "bg-teal", "text-teal")
    CYAN = Color("Cyan", "bg-cyan", "text-cyan")
    GRAY = Color("Gray", "bg-gray", "text-gray")


class TestTextChoices(models.TextChoices):
    TEST = "rand-val1", _("Test Random Val")
