from django.urls import path
from patient import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout")
]
