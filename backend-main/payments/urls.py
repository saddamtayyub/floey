from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *

r = DefaultRouter()

r.register('promocodes',Promo)
r.register('rulesets',Rulesets)
r.register('gymrule',GymRuleAPI)
r.register('maxusage',MaxUses)
r.register('couponuserlist',CouponUsersList)
urlpatterns = [
    path('',include(r.urls)),
    path('promo/',ApplyPromocode.as_view()),
    path('removepromocode/',RemovePromocode.as_view()),
    path('invoice/',Invoice.as_view()),
    path('invoice/csv/',export_to_csv.as_view()),
    path('invoice/<str:uuid>/',InvoiceDetail.as_view()),
    # path('offerdetails',OfferDetails.as_view()),
]