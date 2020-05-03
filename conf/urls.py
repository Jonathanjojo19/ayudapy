"""ayudapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from conf import api_urls
from core import views as core_views
from org import views as org_views
from org.views import RestrictedView

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('local-admin/', admin.site.urls),
    # home
    path('', core_views.home, name='home'),
    path('bantu', TemplateView.as_view(template_name="giver/info.html")),
    path('ketentuan', TemplateView.as_view(template_name="footer/legal.html"), name='legal'),
    path('relawan/ketentuan', TemplateView.as_view(template_name="volunteer/info.html"), name='voluntariolegal'),
    path('faq', core_views.view_faq, name='general_faq'),
    path('kontak', TemplateView.as_view(template_name="footer/contact_us.html"), name='contact_us'),
    # help requests
    path('permintaan', TemplateView.as_view(template_name="help_request/info.html")),
    path('daftar', core_views.request_form, name="request-form"),
    path('daftar-permintaan/<int:id>', core_views.view_request, name='pedidos-detail'),
    path('daftar-permintaan-kota/<slug:city>', core_views.list_by_city, name='pedidos-by-city'),
    path('daftar-permintaan', core_views.list_requests),
    # donations
    path('pusat-donasi', org_views.donation_form, name="donation-form"),
    path('donasi', RestrictedView.as_view()),
    path('daftar-donasi', org_views.list_donation),
    path('daftar-donasi-kota/<slug:city>', org_views.list_donation_by_city, name='donation-by-city'),
    path('daftar-donasi/<int:id>', org_views.view_donation_center, name='donaciones-detail'),
    # volunteer
    path('relawan', TemplateView.as_view(template_name="volunteer/form.html"), name='voluntario'),
    # login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += api_urls.urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
