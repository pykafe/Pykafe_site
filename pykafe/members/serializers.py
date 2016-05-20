from models import Member
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('url', 'job_title', 'bio_text', 'photo')
