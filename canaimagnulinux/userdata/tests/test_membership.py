# -*- coding: utf-8 -*-

from canaimagnulinux.userdata.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing.interfaces import TEST_USER_ID

import unittest

FIELDS = [
    'firstname',
    'lastname',
    'gender',
    'birthdate',
    'mobile',
    'officephone',
    'irc',
    'telegram',
    'skype',
    'country',
    'city',
    'institution',
    'instadd',
    'position',
    'profession',
    # 'newsletter',
    'accept',
]


class MembershipPropertiesTestCase(unittest.TestCase):

    """Ensure membership properties are properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_memberdata_properties(self):
        memberdata = self.portal['portal_memberdata']
        for f in FIELDS:
            self.assertTrue(
                memberdata.hasProperty(f), 'not found: {0}'.format(f))

    def test_user_registration_fields(self):
        site_properties = self.portal['portal_properties'].site_properties
        user_registration_fields = site_properties.user_registration_fields
        for f in FIELDS:
            self.assertIn(
                f, user_registration_fields, 'not found: {0}'.format(f))

