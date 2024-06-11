from movieblog import forms
from movieblog import models


# def get_social_links(request):
#     return {'social_links': models.SocialLinksModel.objects.all()}

def get_search_form(request):
    return {'search_form': forms.SearchForm()}