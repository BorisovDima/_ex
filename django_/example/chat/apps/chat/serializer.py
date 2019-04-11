from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField, \
    HyperlinkedIdentityField, CharField, IntegerField, DateTimeField, ImageField, SerializerMethodField, BooleanField

from .models import Room, Message
from chat.apps.myauth.serializer import UserSerializer
from .signals import create
from django.conf import settings
from rest_framework.reverse import reverse
from django.conf import settings

callback = settings.REST_CALLBACK


class MessageSerializer(HyperlinkedModelSerializer):

    author = UserSerializer(read_only=True)
    room = HyperlinkedRelatedField(view_name='room-detail', read_only=True)
    view_it = SerializerMethodField()


    def get_view_it(self, obj):
        return reverse('message-viewed', kwargs={'pk': obj.id})

    def create(self, validated_data):
        self.instance = super().create(validated_data)
        create.send(sender=type(self), instance=self.instance, json=self.data, callback=callback['msg_create'])
        return self.instance


    class Meta:
        model = Message
        fields = ('text', 'room', 'author',  'id', 'date_created',  'url', 'view_it')



class RoomSerializer(HyperlinkedModelSerializer):

    # image = ImageField(source='get_image')

    name = CharField(read_only=True)
    last_msg = CharField(read_only=True)
    count_msgs = IntegerField(source='get_count_msgs', read_only=True)
    count_users = IntegerField(source='get_count_users', read_only=True)
    unviewed_messages = SerializerMethodField()
    messages = SerializerMethodField()

    users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    author = UserSerializer(read_only=True)



    def create(self, validated_data):
        author, user = validated_data['author'], validated_data['user']
        # self.instance = Room.objects.get_or_create_dialog(author, user)
        # create.send(sender=type(self), instance=self.instance, json=self.data, callback=callback['room_create'])
        return Room.objects.get_or_create_dialog(author, user)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context['request']
        ret['name'] = instance.get_room_name(request)
        ret['last_msg'] = MessageSerializer(instance=instance.get_last_msg(), context={'request': request}).data
        return ret


    def get_unviewed_messages(self, obj):
        return obj.get_unviewed_messages(self.context['request']).count()


    def get_messages(self, obj):
        return reverse('room-messages', kwargs={'pk': obj.id}, request=self.context['request'])


    class Meta:
        model = Room
        fields = ('author', 'unviewed_messages', 'id', 'url',
                  'count_msgs', 'count_users', 'name', 'last_msg', 'messages', 'users')









