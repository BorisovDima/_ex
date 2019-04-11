from django.db import models
from chat.apps.core.models import BaseChatModel
from django.db.models import Count
from django.utils import timezone

class RoomManager(models.Manager):

    def get_or_create_dialog(self, author, user):
        dialogs = self.get_dialogs().filter(users__id=author.id).filter(users__id=user.id)
        room, created = dialogs.get_or_create(defaults={'author': author})
        if created:
            room.users.add(user)
        return room #, created


    def get_dialogs(self):
        return self.annotate(count=Count('users')).filter(count=2)

class Room(BaseChatModel):

    author = models.ForeignKey('myauth.User', on_delete=models.CASCADE, related_name='created_rooms') # Add to users
    users = models.ManyToManyField('myauth.User')
    is_group = models.BooleanField(default=False)
    group_name = models.CharField(null=True, blank=True, max_length=124)
    last_change = models.DateTimeField(default=timezone.now)

    objects = RoomManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.users.add(self.author)

    def get_unviewed_messages(self, request):
        return self.message_set.prefetch_related('who_viewed_it').exclude(who_viewed_it=request.user)

    def get_msgs(self, request):
        for q in self.get_unviewed_messages(request):
            q.who_viewed_it.add(request.user)
        return self.message_set.all()

    def get_image(self):
        return

    def get_count_msgs(self):
        return self.message_set.count()

    def get_count_users(self):
        return self.users.count()

    def get_last_msg(self):
        return self.message_set.last()

    def get_absolute_url(self):
        pass

    def get_room_name(self, request):
        if self.is_group:
            return self.group_name
        user = self.users.exclude(id=request.user.id).first()
        return user.username if user else self.author.username

    def __str__(self):
        return f'room-{self.id}'

    class Meta:
        ordering = ['-last_change']


class Message(BaseChatModel):

    text = models.CharField(max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey('myauth.User', on_delete=models.CASCADE)
    who_viewed_it = models.ManyToManyField('myauth.User', related_name='viewed_messages')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.room.last_change = timezone.now()
        self.room.save(update_fields=['last_change'])
        self.who_viewed_it.add(self.author)

    def get_absolute_url(self):
        pass

