from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.bundle import Bundle
from tastypie.http import HttpBadRequest
from tastypie.serializers import Serializer
from tastypie.authentication import Authentication
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth.models import User

from pinry.pins.models import Pin
from pinry.pins.models import Like
from pinry.pins.models import Comment
from pinry.core.models import Member

class PinAuthorization(Authorization):
    def is_authorized(self, request, object=None):
        # only logged in user will can modify pins
        if request.method in ("PUT", "DELETE"):
            return request.user.is_authenticated()
        return True

    def apply_limits(self, request, object_list=None):
        # only allow delete pin belong to this user
        if request.method in ("DELETE", "PUT"):
            return object_list.filter(submitter=request.user.get_profile())

        return object_list

class PinResource(ModelResource):  # pylint: disable-msg=R0904
    tags = fields.ListField()
    author = fields.CharField()
    is_owner = fields.BooleanField()

    class Meta:
        queryset = Pin.objects.all()
        resource_name = 'pin'
        list_allowed_method = ["GET"]
        details_allowd_method = ["GET", "PUT", "DELETE"]
        include_resource_uri = False
        authorization = PinAuthorization()
        serializer = Serializer(["json"])
        filtering = {
            'published': ['gt'],
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PinResource, self).build_filters(filters)

        if 'tag' in filters:
            orm_filters['tags__name__in'] = filters['tag'].split(',')

        return orm_filters

    def dehydrate_tags(self, bundle):
        return map(str, bundle.obj.tags.all())

    def dehydrate_author(self, bundle):
        return bundle.obj.submitter.user.username

    def dehydrate_is_owner(self , bundle):
        if not bundle.request.user.is_authenticated():
            return False
        else:
            return bundle.request.user.pk == bundle.obj.submitter.user.pk

    def save_m2m(self, bundle):
        tags = bundle.data.get('tags', [])
        bundle.obj.tags.set(*tags)
        return super(PinResource, self).save_m2m(bundle)

class LikeResource(ModelResource):
    username = fields.CharField()
    avatar = fields.CharField()

    class Meta:
        queryset = Like.objects.all()
        resource_name = 'like'
        filtering = {
            'created_time': ['gt'],
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(LikeResource, self).build_filters(filters)

        if 'pin_id' in filters:
            orm_filters['pin__pk'] = filters['pin_id']
        else:
            raise HttpBadRequest("need pid_id parameter")

        return orm_filters

    def dehydrate_username(self, bundle):
        return bundle.obj.author.user.username

    def dehydrate_avatar(self, bundle):
        return bundle.obj.author.avatar_url


class CommentResource(ModelResource):
    pass

class RepinResource(ModelResource):
    pass

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
