import uuid

from braces import views
from django.conf import settings
from django.core import signing
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from law.content.models import CommonContent
from .models import Annotation


class RootAnnotationView(views.CsrfExemptMixin, views.JsonRequestResponseMixin,
                         View):
    def get(self, request, *args, **kwargs):
        base_url = reverse('annotations:root')
        result = {
            "message": "Annotator Store API",
            "links": {
                "annotation": {
                    "create": {
                        "desc": "Create a new annotation",
                        "method": "POST",
                        "url": reverse('annotations:create')
                    },
                    "delete": {
                        "desc": "Delete an annotation",
                        "method": "DELETE",
                        "url": base_url + ":id/"
                    },
                    "read": {
                        "desc": "Get an existing annotation",
                        "method": "GET",
                        "url": base_url + ":id/"
                    },
                    "update": {
                        "desc": "Update an existing annotation",
                        "method": "PUT",
                        "url": base_url + ":id/"
                    }
                },
                "search": {
                    "desc": "Basic search API",
                    "method": "GET",
                    "url": reverse('annotations:search')
                }
            }
        }

        return self.render_json_response(result)


class APIAnnotationView(views.CsrfExemptMixin, views.JsonRequestResponseMixin,
                        View):
    require_json = True

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        uri = self.request_json['uri']
        obj_params = signing.loads(uri, key=settings.PASSWORD_ENC_KEY)

        user = request.user
        content = get_object_or_404(CommonContent, **obj_params)

        ann_id = str(uuid.uuid4())
        self.request_json['id'] = ann_id
        ann = Annotation(pk=ann_id, user=user, content=content,
                         annotation_object=self.request_json)
        ann.save()

        return self.render_json_response(self.request_json)


class SearchAnnotationView(views.CsrfExemptMixin, views.JSONResponseMixin,
                           View):

    def get(self, request, *args, **kwargs):

        uri = request.GET.get('uri')

        if not uri:
            result = {'total': 0, 'rows': []}
        else:
            content_id, user_id = signing.loads(uri,
                                                key=settings.PASSWORD_ENC_KEY)
            qs = Annotation.objects.filter(user_id=user_id,
                                           content_id=content_id)
            annotations = list(qs.values_list('annotation_object', flat=True))
            result = {'total': len(annotations), 'rows': annotations}

        return self.render_json_response(result)


class UpdateDeleteAnnotationView(views.CsrfExemptMixin,
                                 views.JsonRequestResponseMixin, View):

    def get_annotation(self, request, annotation_id):

        if not request.user.is_authenticated:
            raise ObjectDoesNotExist

        annotation = get_object_or_404(Annotation, pk=uuid.UUID(annotation_id))

        if request.user != annotation.user:
            raise PermissionDenied

        return annotation

    def delete(self, request, *args, **kwargs):
        annotation = self.get_annotation(request, kwargs.get('annotation_id'))

        annotation.delete()

        return HttpResponse(status=204)

    def put(self, request, *args, **kwargs):
        annotation = self.get_annotation(request, kwargs.get('annotation_id'))

        annotation.annotation_object.update(self.request_json)
        annotation.save()

        return self.render_json_response(annotation.annotation_object)
