from django.db import models
from haystack.signals import BaseSignalProcessor

from .models import Member


class RealtimeSignalProcessor(BaseSignalProcessor):
    def setup(self):
        # Listen only to the ``Issue`` model.
        models.signals.post_save.connect(self.handle_save, sender=Member)
        models.signals.post_delete.connect(self.handle_delete, sender=Member)

    def teardown(self):
        # Disconnect only for the ``Issue`` model.
        models.signals.post_save.disconnect(self.handle_save, sender=Member)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Member)
