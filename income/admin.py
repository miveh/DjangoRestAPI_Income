from django.contrib import admin

from income.models import *


# maybe customize later
admin.site.register(Courier)
admin.site.register(Trip)
admin.site.register(Income)
admin.site.register(IncreaseIncome)
admin.site.register(DeductionIncome)
admin.site.register(DailyIncome)
admin.site.register(WeeklyIncome)
