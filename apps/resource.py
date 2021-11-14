from django.db.models import fields
from import_export import resources
from apps.models import PostAgenda


class AgendaResource(resources.ModelResource):
    class Meta:
        model = PostAgenda
        fields = ['kegiatan','tempat','waktu','tanggal']