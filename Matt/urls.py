"""Matt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import PlotLoan1, PlotLoan2, PlotLoan3, PlotLoan4, PlotLoan5, PlotLoan6, PlotLoan7, PlotLoan8, \
    PlotLoan9, PlotLoan10
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='webapp/welcome.html'), name='homepage'),
    path('plot1/<int:pk>', PlotLoan1.as_view(), name='loan1'),
    path('plot2/<int:pk>', PlotLoan2.as_view(), name='loan2'),
    path('plot3/<int:pk>', PlotLoan3.as_view(), name='loan3'),
    path('plot4/<int:pk>', PlotLoan4.as_view(), name='loan4'),
    path('plot5/<int:pk>', PlotLoan5.as_view(), name='loan5'),
    path('plot6/<int:pk>', PlotLoan6.as_view(), name='loan6'),
    path('plot7/<int:pk>', PlotLoan7.as_view(), name='loan7'),
    path('plot8/<int:pk>', PlotLoan8.as_view(), name='loan8'),
    path('plot9/<int:pk>', PlotLoan9.as_view(), name='loan9'),
    path('plot10/<int:pk>', PlotLoan10.as_view(), name='loan10'),

    path('admin/', admin.site.urls),

]

admin.site.site_header = 'SpreadSheet Administration'
