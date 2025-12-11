from django.urls import path
from .views import *

app_name = "homepage"

urlpatterns = [
    path("mainpage/", Mainpage, name="mainpage"),

    path("show_employees/", Show_employees, name="show-employees"),

    path("add_employees/", Add_employees, name="add-employees"),

    path("deleteEmployees/<int:Eid>/", deleteEmployees),

    path("update_employees/<int:Eid>/", Update_employees, name="update-employees"),

    path("show_crops/", Show_crops, name="show-crops"),

    path("add-crops/", Add_crops, name="add-crops"),

    path("update_crops/<int:Cid>/", Update_crops, name="update-crops"),

    path("delete_crops/<int:Cid>/", Delete_crops),

    path('show_machinery/', Show_machinery, name="show-machinery"),

    path("add-machinery/", Add_machinery, name="add-machinery"),

    path("delete_machinery/<str:Number_plate>/", Delete_machinery),

    path("update_machinery/<str:Number_plate>/", Update_machinery, name="update-machinery"),

    path("show_livestock/", Show_livestock, name="show-livestock"),

    path("add_livestock/", Add_livestock,name="add-livestock"),

    path("update_livestock/<str:Tag_number>/", Update_livestock, name="update-livestock" ),

    path("deleteLivestock/<str:Tag_number>/",deleteLivestock),

    path('show_livestockproduction/<str:Tag_number>/', Show_livestock_production, name='show-livestockproduction'),

    path('add_livestockproduction/<str:Tag_number>/',Add_livestock_production, name='add-livestockproduction'),

    path('deleteLivestockproduction/<str:Tag_number>/<slug:Production_date>/', deleteLivestock_production),

    path('update_livestockproduction/<str:Tag_number>/<slug:Production_date>/', Update_livestock_production, name='update-livestockproduction'),

    path('show_cropexpenses/<int:Cid>/', Show_crop_expenses, name='show-cropexpenses'),

    path('add_cropexpenses/<int:Cid>/', Add_crop_expenses, name="add-cropexpenses"),

    path('update_cropexpense/<int:Cid>/<slug:Expense_date>/', Update_crop_expenses, name='update-cropexpenses'),

    path('delete_cropexpenses/<int:Cid>/<slug:Expense_date>/', delete_cropexpenses),

    path('show_cropsales/<int:Cid>/', Show_crop_sales, name="show-cropsales"),

    path('add_cropsales/<int:Cid>/', Add_crop_sales, name='add-cropsales'),

    path('delete_cropsales/<int:Cid>/<slug:Sale_date>/<str:Invoice_number>/', Delete_crop_sales, name='delete-cropsales'),

    path('update_cropsales/<int:Cid>/<slug:Sale_date>/', Update_crop_sales, name='update-cropsales'),

    path('show_cropoperations/<int:Cid>/', Show_crop_operations, name='show-cropoperations'),

    path('add_cropoperations/<int:Cid>/', Add_crop_operations, name='add-cropoperations'),

    path('delete_cropoperations/<int:Cid>/<slug:Operation_date>/<str:Operation_name>/', Delete_crop_operations),

    path('update_cropoperations/<int:Cid>/<slug:Operation_date>/', Update_crop_operations, name='update-cropoperations'),

    path('show_machineryactivities/<str:Number_plate>/', Show_machinery_activities, name='show-machineryactivities'),

    path('add_machineryactivirties/<str:Number_plate>/', Add_machinery_activities, name="add-machineryactivities"),

    path('Delete_machineryactivities/<str:Number_plate>/<slug:Activity_date>/<str:Activity_type>/', Delete_machinery_activity),

    path('update_machineryactivities/<str:Number_plate>/<slug:Activity_date>/', Update_machinery_activities, name='update-machineryactivities'),

    path('show_machinerymaintenance/<str:Number_plate>/', Show_machinery_maintenance, name='show-machinerymaintenance'),

    path('add_machinerymaintenance/<str:Number_plate>/', Add_machinery_maintenance, name='add-machinerymaintenance'),

    path('delete_machinerymaintenance/<str:Number_plate>/<slug:Date>/<str:Machinery_part>/', Delete_machinery_maintenance),

    path('update_machinerymaintenance/<str:Number_plate>/<slug:Date>/', Update_machinery_maintenance, name='update-machinerymaintenance'),

    path('select_yearmonth/', Select_year_month, name='select-yearmonth'),

    path('milk_productionbymonth/<int:selected_year>/<int:selected_month>/', Milk_production_by_month, name='milk-productionbymonth'),

    path('add_milkproductionbymonth/<int:selected_year>/<int:selected_month>/', Add_milk_production_by_month, name='add-milkproductionbymonth'),

    path('Delete_milk_production_by_month/<int:selected_year>/<int:selected_month>/<int:Day>/', Delete_milk_production_by_month),

    path('update_milkproductionbymonth/<int:selected_year>/<int:selected_month>/<int:Day>/', Update_milk_production_by_month,name='update-milkproductionbymonth'),

    path('select_yearandmonth/', Select_year_month_egg, name='select-yearandmonth'),

    path('egg_productionrecord/<int:selected_year>/<int:selected_month>', Egg_production_record, name='egg-productionrecord'),

    path('add_eggproductionbymonth/<int:selected_year>/<int:selected_month>/', Add_egg_production_by_month, name='add-eggproduction'),

    path('delete_eggproductionbymonth/<int:selected_year>/<int:selected_month>/<int:Day>/', Delete_egg_production_by_month),

    path('update_eggproductionbymonth/<int:selected_year>/<int:selected_month>/<int:Day>/',Update_egg_production_by_month, name='update-eggproduction'),

    path('help/', Help, name='help'),

    path('logOut/', logOut, name='logOut'),

]
