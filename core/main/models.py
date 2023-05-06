from django.db import models

# Create your models here.

class Header(models.Model):

    img = models.ImageField('Header Icon Image', upload_to='images')
    title1 = models.CharField('Title-1', max_length=80)
    title2 = models.CharField('Title-2', max_length=20)
    title3 = models.CharField('Title-3', max_length=20)
    subtitle1 = models.CharField('Title-3', max_length=20)
    subtitle2 = models.CharField('Title-3', max_length=20)
    title4 = models.CharField('Title-4', max_length=20)
    btn_name = models.CharField('Button Name', max_length=25)
    
class Title(models.Model):

    title = models.CharField('Title-1', max_length=40)
    title2 = models.CharField('Title-2', max_length=40)
    title3 = models.CharField('Title-3', max_length=40)
    title4 = models.CharField('Title-4', max_length=40)
    title5 = models.CharField('Title-5', max_length=40)
    subtitle = models.CharField('SubTitle', max_length=50)
    btn_name = models.CharField('Button Name', max_length=25)
    latest_title = models.CharField('Latest Episode General Title', max_length=30)
    trending_title = models.CharField('Trending Episode General Title', max_length=30)
    related_episodes = models.CharField('Related Episodes Title', max_length=30)
    topic_title = models.CharField('Topic Title', max_length=30)

class ContactGet(models.Model):

    title = models.CharField('Contact Title', max_length=50)
    subtitle1 = models.CharField('Phone Number', max_length=20)
    subtitle_info1 = models.CharField('Phone Info', max_length=30)
    subtitle2 = models.CharField('Email', max_length=20)
    subtitle_info2 = models.EmailField('Email Info')
    subtitle3 = models.CharField('Location', max_length=25)
    subtitle_info3 = models.CharField('Location Info', max_length=60)
    title2 = models.CharField('Contact Title 2', max_length=40)
    btn_name = models.CharField('Button Name', max_length=20)
    
class ContactPost(models.Model):

    user_name = models.CharField('User Name', max_length=40)
    user_email = models.EmailField('User Email')
    company_name = models.CharField('Company Name', max_length=50)
    user_message = models.TextField('User Message')

    def __str__(self) -> str:
        return self.user_name
    
class Footer(models.Model):

    title = models.CharField('Footer Title', max_length=30)
    li1 = models.CharField('Footer li-1', max_length=30)
    li2 = models.CharField('Footer li-2', max_length=30)
    li3 = models.CharField('Footer li-3', max_length=30)
    li4 = models.CharField('Footer li-4', max_length=30)
    subtitle = models.CharField('Footer Subtitle', max_length=30)
    social = models.CharField('Footer Social', max_length=25)
    footer_info = models.CharField('Footer Info', max_length=60)
    img1 = models.ImageField('Social Image 1', upload_to='images')
    img2 = models.ImageField('Social Image 2', upload_to='images')


class About(models.Model):

    title1 = models.CharField('About First Title', max_length=30)
    text1 = models.TextField('About First Text')
    text2 = models.TextField('About Second Text')
    img = models.ImageField('About Image', upload_to='images')
    title2 = models.CharField('About Second Title', max_length=30)

class About_Content(models.Model):
    
    img = models.ImageField('About Content Image', upload_to='images')
    name = models.CharField('About Content Name', max_length=20)
    profession = models.TextField('About Content Profession')
    social = models.CharField('About Content social', max_length=80)
    symbol_img = models.ImageField('About Content Verified', upload_to='images')


class LastestEpisode(models.Model):

    img = models.ImageField('Latest First Image', upload_to='images')
    btn_name = models.CharField('Latest Episodes Button', max_length=25)
    title = models.CharField('Latest Episodes Title', max_length=35)
    minutes = models.CharField('Latest Episodes Minutes', max_length=30)
    episodes = models.CharField('Latest Episodes', max_length=40)
    user_img = models.ImageField('Latest Episodes Image', upload_to='images')
    name_profession = models.CharField('Latest Episodes name and prof', max_length=30)
    text = models.CharField('Latest Episodes Text', max_length=50)
    airpods = models.CharField('Latest Episodes Airpods', max_length=10)
    likes = models.CharField('Latest Episodes Likes', max_length=10)
    comments = models.CharField('Latest Episodes Comments', max_length=10)
    downloads = models.CharField('Latest Episodes Downloads', max_length=10)
    symbol_img = models.ImageField('About Content Verified', upload_to='images')

class TrendingEpisode(models.Model):

    img = models.ImageField('Lastest First Image', upload_to='images')
    title = models.CharField('Latest Episodes Title', max_length=25)
    user_img2 = models.ImageField('Latest Episodes Images', upload_to='images')
    name_profession = models.CharField('Latest Episodes name and prof', max_length=30)
    text = models.CharField('Latest Episodes Text', max_length=50)
    airpods = models.CharField('Latest Episodes Airpods', max_length=10)
    likes = models.CharField('Latest Episodes Likes', max_length=10)
    comments = models.CharField('Latest Episodes Comments', max_length=10)
    symbol_img = models.ImageField('About Content Verified', upload_to='images')
    check_btn = models.BooleanField('YES/NO')

class Topic(models.Model):

    img = models.ImageField('Topic Image', upload_to='images')
    title = models.CharField('Topic Title', max_length=20)
    episodes = models.CharField('Topic Episodes', max_length=25)

class Specialist(models.Model):

    img = models.ImageField('Specialist Image', upload_to='images')
    name = models.CharField('Specialist Name', max_length=20)
    profession = models.CharField('Specialist Profession', max_length=70)
    symbol_img = models.ImageField('Specialist Verified', upload_to='images')
    social = models.CharField('Specialist Social', max_length=60)
    check_btn = models.BooleanField('YES/NO')


class DetailContent(models.Model):

    title1 = models.CharField('Detail Title', max_length=30)
    img = models.ImageField('Detail Image', upload_to='images')
    play = models.CharField('Detail Play', max_length=25)
    minute = models.CharField('Detail Minute', max_length=25)
    episode = models.CharField('Detail Episode', max_length=30)
    title2 = models.CharField('Detail Title', max_length=30)
    text1 = models.TextField('Detail Text')
    text2 = models.TextField('Detail Text')
    text3 = models.TextField('Detail Text')
    user_img = models.ImageField('Detail User Image', upload_to='images')
    name = models.CharField('Detail Name', max_length=40)
    symbol_img = models.ImageField('Detail Image', upload_to='images')
    social = models.CharField('Detail Social', max_length=50)

class Subscribe(models.Model):

    subscribe_email = models.EmailField('User Subscribe Email')

    def __str__(self) -> str:
        return self.subscribe_email