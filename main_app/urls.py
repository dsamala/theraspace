from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('patients/', views.PatientList.as_view(), name="patient_list"),
    path('patients/new', views.Patient_New.as_view(), name="patient_new"),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name="patient_detail"),
    path('patients/<int:pk>/update', views.PatientUpdate.as_view(), name="patient_update"),
    path('patients/<int:pk>/delete', views.PatientDelete.as_view(), name="patient_delete"),
    path('clinicians/', views.ClinicianList.as_view(), name="clinician_list"),
    path('clinicians/new', views.Clinician_New.as_view(), name="clinician_new"),
    path('clinician/<int:clinician_id>', views.clinician_show, name="clinician_detail"),
    path('clinician/<int:pk>/update', views.ClinicianUpdate.as_view(), name="clinician_update"),
    path('clinician/<int:pk>/delete', views.ClinicianDelete.as_view(), name="clinician_delete"),
]