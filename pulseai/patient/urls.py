from django.urls import path
from patient import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    path("take_a_test/",views.take_a_test,name="test")
]
