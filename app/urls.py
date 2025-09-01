
from django.urls import path
from . import views
urlpatterns = [
    path('feedback/',views.feedback_form),
    path('form-status/<int:batch_id>/',views.check_form_status),
    path('batch/',views.get_dashboard),
]