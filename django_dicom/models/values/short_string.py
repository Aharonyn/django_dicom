"""
Definition of the
:class:`~django_dicom.models.values.short_string.ShortString` model.
"""


from django.db import models
from django_dicom.models.values.data_element_value import DataElementValue


class ShortString(DataElementValue):
    """
    A :class:`~django.db.models.Model` representing a single *ShortString*
    data element value.
    """

    #: Overrides
    #: :attr:`~django_dicom.models.values.data_element_value.DataElementValue.value`
    #: to assign a :class:`~django.db.models.CharField`.
    value = models.CharField(max_length=16, blank=True, null=True)

    #: Overrides
    #: :attr:`~django_dicom.models.values.data_element_value.DataElementValue.raw`
    #: to assign a :class:`~django.db.models.CharField`.
    raw = models.CharField(max_length=16, blank=True, null=True)


# flake8: noqa: E501
