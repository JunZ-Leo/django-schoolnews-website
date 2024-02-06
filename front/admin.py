from django.contrib import admin
from.models import User, Topic
# Register your models here.

class NewUser(admin.ModelAdmin):
    list_display = ["username", "nickname", "email", "create_time", "updated_time"]
    list_filter = ["username", "nickname"]
    search_fields = ["username"]


admin.site.register(User, NewUser)

class NewTopic(admin.ModelAdmin):
    list_display = ["topic_title", "topic_date", "comment_number", "create_time", "updated_time"]
    list_filter = ["topic_title"]
    search_fields = ["topic_title"]

admin.site.register(Topic, NewTopic)