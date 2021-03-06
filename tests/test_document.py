from django.conf import settings
from mongoengine import Document, fields
from mongodbforms import DocumentForm
import unittest


class MyDocument(Document):
    mystring = fields.StringField()
    myverbosestring = fields.StringField(verbose_name="Foobar")
    myrequiredstring = fields.StringField(required=True)
    list_of_strings = fields.ListField(fields.StringField())


class MyForm(DocumentForm):
    class Meta:
        document = MyDocument


class SimpleDocumentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        settings.configure()

    def test_form(self):
        form = MyForm()
        self.assertEquals(len(form.fields), 4)
        self.assertFalse(form.fields['mystring'].required)
        self.assertEquals(form.fields['myverbosestring'].label, "Foobar")
        self.assertTrue(form.fields['myrequiredstring'].required)
        self.assertEqual(form.fields['list_of_strings'].label, "List of strings")
