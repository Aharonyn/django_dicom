from django.urls import path, include
from django_dicom import views
from rest_framework import routers

app_name = "dicom"
router = routers.DefaultRouter()
router.register(r"image", views.ImageViewSet)
router.register(r"series", views.SeriesViewSet)
router.register(r"study", views.StudyViewSet)
router.register(r"patient", views.PatientViewSet)


urlpatterns = [
    path("dicom/", include(router.urls)),
    path(
        "dicom/patient/<str:uid>/download/",
        views.PatientViewSet.as_view({"get": "download_series_set"}),
        name="download_series_set",
    ),
    path(
        "dicom/manufacturersList/",
        views.SeriesViewSet.as_view({"get": "get_manufacturers"}),
        name="get_manufacturers",
    ),
    path(
        "dicom/series/get_csv/",
        views.SeriesViewSet.as_view({"get": "get_csv"}),
        name="get_csv",
    ),
    path(
        "dicom/series/<int:pk>/download/",
        views.SeriesViewSet.as_view({"get": "download_series"}),
        name="download_series",
    ),
]
