from datetime import datetime

import time_machine
from django.test import TestCase


@time_machine.travel(datetime(2023, 1, 1))
class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        print('Base class method')


class ChildTest(BaseTest):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        print('Child class method')

    def test_something(self):
        self.assertTrue(False)
