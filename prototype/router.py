from doctordashboard.viewsset import PatientViewSet
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('patients', PatientViewSet)
# router.register('Appointment', AppointmentViewSet)
# router.register('user', UserViewSet)
# router.register('secretary', SecretaryViewSet)
# router.register('administrator', AdministartorViewSet)
