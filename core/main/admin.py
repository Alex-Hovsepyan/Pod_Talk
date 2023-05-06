from django.contrib import admin
from .models import Header
from .models import Title
from .models import ContactGet
from .models import ContactPost
from .models import Footer
from .models import About
from .models import About_Content
from .models import LastestEpisode
from .models import TrendingEpisode
from .models import Topic
from .models import Specialist
from .models import DetailContent
from .models import Subscribe

# Register your models here.

admin.site.register(Header)
admin.site.register(Title)
admin.site.register(ContactGet)
admin.site.register(ContactPost)
admin.site.register(Footer)
admin.site.register(About)
admin.site.register(About_Content)
admin.site.register(LastestEpisode)
admin.site.register(TrendingEpisode)
admin.site.register(Topic)
admin.site.register(Specialist)
admin.site.register(DetailContent)
admin.site.register(Subscribe)