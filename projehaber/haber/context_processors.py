from .models import Settings


# def SettingsList(request):
#     try:
#         context = Settings.objects.get()
#         # context = Settings.objects.first() 
#         # sadece ilk nesneyi kullanmak istiyorsak
#     except Settings.DoesNotExist:
#         context = None
#     return {'setting' : context}

def SettingsList(request):
    context = Settings.objects.first()
    return {'setting' : context}