from django.contrib import admin
from django.forms import widgets
from django.db import models 
from django.utils.html import mark_safe
from django.urls import reverse
from .inlines import *
from core.models import *
from core.forms import RaceForm
from django import forms
from django.http import HttpResponse 
# from import_export.admin import ImportExportModelAdmin
import csv 



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = ['Места'] + [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = f'attachement; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            seats = ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
            # row = writer.writerow([getattr(obj, field) for field in field_names[1:]])
            writer.writerow([seats] + [getattr(obj, field) for field in field_names[1:]])
        return response
    export_as_csv.short_description = "Export Selected"


# core 

class DirectionAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    "code",
    "name",
  ]
  list_editable = [
    'name',
  ]
  formfield_overrides = {
    models.ManyToManyField:{'widget':forms.CheckboxSelectMultiple}
  }


class TimeAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'time',
  ]
  list_editable = [
    'time',
  ]


class StopAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'name',
  ]
  list_editable = [
    'name',
  ]


class SeatAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'number'
  ]
  list_editable = [
    'number',
  ]
  list_display_links = [
    'id'
  ]


class SeatInOrderAdmin(admin.ModelAdmin):
  def get_order(self, obj):
  #   option = "change" # "delete | history | change"
  #   massiv = []
  #   if obj.order:
  #     obj  = obj.order
  #     app   = obj._meta.app_label
  #     model = obj._meta.model_name
  #     url   = f'admin:{app}_{model}_{option}'
  #     args  = (obj.pk,)
  #     href  = reverse(url, args=args)
  #     name  = f'{obj.order.full_name}, {obj.order.phone}, {obj.order.race.direction}'
  #     link = f"<a href={href}>{name}</a>"
  #     return mark_safe(link)
    return f'{obj.order.full_name}, {obj.order.phone}'#, {obj.order.race.direction}'

  get_order.short_description = "Заказ"
  def get_race(self, obj):
    # option = "change" # "delete | history | change"
    # massiv = []
    # if obj.race:
    #   obj  = obj.race
    #   app   = obj._meta.app_label
    #   model = obj._meta.model_name
    #   url   = f'admin:{app}_{model}_{option}'
    #   args  = (obj.pk,)
    #   href  = reverse(url, args=args)
    #   name  = f'{obj.race.direction}, {obj.race.time.time}, {obj.race.date}, {obj.race.price}, {obj.race.is_full}'
    #   link = f"<a href={href}>{name}</a>"
    #   return mark_safe(link)
    f'{obj.race.direction}, {obj.race.time.time}, {obj.race.date}, {obj.race.price}, {obj.race.is_full}'
  get_race.short_description = "Рейс"
  list_display = [
    'seat',
    'get_race',
    'get_order',
  ]
  fields = [
    'seat',
    'get_race',
    'get_order',
  ]
  readonly_fields = [
    'seat',
    'get_race',
    'get_order',
  ]


class RaceAdmin(admin.ModelAdmin):
  # def save_model(self, request, obj, form, change):
  #   date_from = request.POST.get('date_from', '')
  #   date_to   = request.POST.get('date_to', '')
  #   start     = datetime.strptime(date_from, '%Y-%m-%d')
  #   end       = datetime.strptime(date_to, '%Y-%m-%d')
  #   dates = []
  #   while start <= end:
  #     dates.append(start.date())
  #     start += timedelta(days=1)
  #   for date in dates:
  #     print(date)
  #     race, created = Race.objects.get_or_create(
  #       date=date,
  #       time=Time.objects.get(id=request.POST.get('time', '')),
  #     )
  #     if created:
  #       race.direction=Direction.objects.get(id=request.POST.get('direction', ''))
  #       race.price    =request.POST.get('price', '')
  #       race.save()
  #   return super().save_model(request, obj, form, change)
  # actions = []
  actions_on_top = True
  acitons_on_bottom = True 
  actions_selection_couner = True 
  date_hierarchy = 'date' # 'created' | 'updated' |'date'
  empty_value_display = '???'
  change_list_template = 'races_change_list.html'
  # form = RaceForm
  # exclude = [
  # ]
  fields = []
  # fieldsets = []
  # filter_horizontal = ()
  # filter_vertical = ()
  # form # get_form()
  # formfield_overrides = {
  #     models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
  #     # models.DateTimeField: {'widget': widgets.TextInput}
  # }
  inlines = [
    # StopInRaceInline, 
    SeatInOrderInline
  ]
  list_display = [
    'id',
    'direction',
    'time',
    'date',
    'price'
  ]
  list_display_links = [
  ]
  list_editable = [
    'price'
  ]
  list_filter = [
    'direction',
    'time',
    'date',
    'price'
  ]
  list_max_show_all = 300
  list_per_page = 20
  list_select_related = False
  ordering = (
    '-id',
  )
  # paginator
  # prepopulated_fields
  # preserve_filters
  # radio_fields
  # autocomplete_fields
  raw_id_fields = [
  ]
  readonly_fields = [
    # "direction",
    # "time",
    # "date",
    # "price",
    "is_full",
  ]
  save_as = False
  save_as_continue = True 
  save_on_top = True
  search_fields = [
    "direction__name",
  ]
  # show_full_result_count
  # sortable_by
  view_on_site = False 


# pages 

class IndexAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request):
    return False
  def has_add_permission(self, request):
    count = Index.objects.all().count()
    if count == 0:
      return True
    return False
  list_display = [
    'id',
    'title',
    'description',
  ]
  list_editable = [
    'title',
    'description',
  ]
  list_display_links = [
    'id',
  ]


class AboutAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request):
    return False
  def has_add_permission(self, request):
    count = About.objects.all().count()
    if count == 0:
      return True
    return False
  list_display = [
    'id',
    'title',
    'description',
  ]
  list_editable = [
    'title',
    'description',
  ]
  list_display_links = [
    'id',
  ]


class ParkAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request):
    return False
  def has_add_permission(self, request):
    count = Park.objects.all().count()
    if count == 0:
      return True
    return False
  list_display = [
    'id',
    'title',
    'description',
  ]
  list_editable = [
    'title',
    'description',
  ]
  list_display_links = [
    'id',
  ]


class BlogAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request):
    return False
  def has_add_permission(self, request):
    count = Blog.objects.all().count()
    if count == 0:
      return True
    return False
  list_display = [
    'id',
    'title',
    'description',
  ]
  list_editable = [
    'title',
    'description',
  ]
  list_display_links = [
    'id',
  ]


class ServiceAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request):
    return False
  def has_add_permission(self, request):
    count = Service.objects.all().count()
    if count == 0:
      return True
    return False
  list_display = [
    'id',
    'title',
    'description',
  ]
  list_editable = [
    'title',
    'description',
  ]
  list_display_links = [
    'id',
  ]


# content 

class BusAdmin(admin.ModelAdmin):
  list_display = [
    "id",
    "name",
    "photo"
  ]
  list_display_links = [
    "id",
  ]
  list_editable = [
    "name",
    "photo",
  ]
  inlines = [
    BusPhotoInline,
    BusCommentInline
  ]


class BusGoodAdmin(admin.ModelAdmin):
  list_filter = [
    "bus",
  ]
  list_display = [
    "id",
    "text",
    "bus",
  ]
  list_display_links = [
    "id",
  ]
  list_editable = [
    "text",
    "bus",
  ]
  list_per_page = 100


class BusCommentAdmin(admin.ModelAdmin):
  list_display_links = [
    'id',
  ]
  list_display = [
    'id',
    'text',
    'bus',
    'moderated',
  ]
  list_editable = [
    'text',
    'bus',
    'moderated',
  ]

class BusPhotoAdmin(admin.ModelAdmin):
  list_display_links = [
    'id',
  ]
  list_display = [
    'id',
    'photo',
  ]
  list_editable = [
    'photo',
  ]

from modeltranslation.admin import TabbedTranslationAdmin

class PostAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_per_page = 100
  search_fields = [
    'title'
  ]
  list_filter = [
    'created',
    'updated',
  ]
  list_display = [
    'id',
    'title',
    'slug',
    'image',
    'created',
    'updated',
  ]
  list_display_links = [
    'id',
  ]
  list_editable = [
    'title',
    'slug',
    'image',
  ]

# order

class OrderAdmin(admin.ModelAdmin, ExportCsvMixin):
  actions = ['export_as_csv'] 
  def get_race(self, obj):
    option = "change" # "delete | history | change"
    massiv = []
    try:
      obj  = obj.race
      app   = obj._meta.app_label
      model = obj._meta.model_name
      url   = f'admin:{app}_{model}_{option}'
      args  = (obj.pk,)
      href  = reverse(url, args=args)
      name  = obj
      link = f"<a href={href}>{name}</a>"
      return mark_safe(link)
    except: pass
    return obj
  get_race.short_description = "Рейc"
  def get_direction(self, obj):
    option = "change" # "delete | history | change"
    massiv = []
    if obj.direction:
      obj  = obj.direction
      app   = obj._meta.app_label
      model = obj._meta.model_name
      url   = f'admin:{app}_{model}_{option}'
      args  = (obj.pk,)
      href  = reverse(url, args=args)
      name  = obj
      link = f"<a href={href}>{name}</a>"
      return mark_safe(link)
  get_direction.short_description = "Напрямок"
  def seats1(obj):
    # seats_in_order = SeatInOrder.objects.filter(order=obj)
    # if seats_in_order.exists():
    return ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
  def seats2(self, obj):
    # seats_in_order = SeatInOrder.objects.filter(order=obj)
    # if seats_in_order.exists():
    return ','.join([seat_in_order.seat.number for seat_in_order in SeatInOrder.objects.filter(order=obj)])
  seats1.short_description = 'Места'
  seats1.empty_value_display = '????'
  seats2.short_description = 'Места'
  seats2.empty_value_display = '????'
  # actions = []
  actions_on_top = True 
  acitons_on_bottom = True 
  actions_selection_couner = True 
  date_hierarchy = 'created' # 'created' | 'updated' |'date'
  empty_value_display = '???'
  exclude = [
    'sk',
    'race',
    'direction'
  ]
  formfield_overrides = {
      models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
      # models.DateTimeField: {'widget': widgets.TextInput}
  }
  inlines = [
    SeatInOrderInline, 
    PaymentInline
  ]
  list_display = [
    "id",
    # "sk",
    "get_race",
    # seats1,
    'seats2',
    "full_name",
    "phone",
    "email",
    "departion",
    "arrival",
    "ordered",
    "pdf",
    # "direction",
    # "date",
    # "time",
    "created",
    "updated",
  ]
  list_display_links = [
    'id', 
  ]
  list_editable = []
  list_filter = [
    # "direction",
    # "date",
    # "time",
    'departion',
    'arrival',
    'ordered',
    'created',
    'updated',
  ]
  list_max_show_all = 100
  list_per_page = 100
  # list_select_related = False
  ordering = (
    '-id',
  )
  readonly_fields = [
    # 'full_name',
    # 'phone',
    # 'email',
    # 'departion',
    # 'arrival',
    # 'get_race',
    # 'get_direction',
    # 'date',
    # 'time',
    'ordered',
    'pdf',
    'created',
    'updated',
  ]
  save_as = False
  save_as_continue = True 
  save_on_top = True 
  search_fields = [
    "full_name",
    "phone",
    "email",
  ]
  view_on_site = False 


class PaymentAdmin(admin.ModelAdmin):
  exclude = []


class ContactAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'phone',
    'email',
    'comment',
    'created',
    'updated',
  ]
  list_filter = [
    "created",
    'updated',
  ] 
  search_fields = [
    'name',
    'phone',
    'email',
  ]


class EuropeContactAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'phone',
    'email',
    'comment',
    'peoples',
    'created',
    'updated',
  ]
  list_filter = [
    "peoples",
    "created",
    'updated',
  ] 
  search_fields = [
    'name',
    'phone',
    'email',
  ]


class BusContactAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'phone',
    'email',
    'comment',
    'peoples',
    'created',
    'updated',
  ]
  list_filter = [
    "peoples",
    "created",
    'updated',
  ] 
  search_fields = [
    'name',
    'phone',
    'email',
  ]  

