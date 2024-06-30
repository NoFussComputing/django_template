import pytest
import unittest
import requests

from django.test import TestCase, Client

from access.tests.abstract.tenancy_object import TenancyObject

from itam.models.device import DeviceSoftware



class DeviceSoftwareTenancyObject(
    TestCase,
    TenancyObject
):

    model = DeviceSoftware
