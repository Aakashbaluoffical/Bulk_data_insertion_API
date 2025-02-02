from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import  GetAllData, UploadCSV


print("open in URL")




urlpatterns = [
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('get_all/', GetAllData.as_view(), name='get-all-data'),
    path('upload/', UploadCSV.as_view(), name='Upload-CSV'),

]



print("close in URL")
