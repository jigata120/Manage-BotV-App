from django.test import TestCase

from Chatbots.templatetags import chatbots_custom_filters


# from Chatbots.templatetags import chatbots_custom_filters

class TemplateFiltersTestCase(TestCase):
    def test_format_number(self):
        self.assertEqual(chatbots_custom_filters.format_number(1000), "1,000")
        self.assertEqual(chatbots_custom_filters.format_number(1234567), "1,234,567")

        self.assertEqual(chatbots_custom_filters.format_number("invalid"), "invalid")
        self.assertEqual(chatbots_custom_filters.format_number(None), None)

    def test_format_to_k(self):
        self.assertEqual(chatbots_custom_filters.format_to_k(924), "924")
        self.assertEqual(chatbots_custom_filters.format_to_k(1334), "1.3K")
        self.assertEqual(chatbots_custom_filters.format_to_k(1334214), "1,334.2K")

        self.assertEqual(chatbots_custom_filters.format_to_k("invalid"), "invalid")
        self.assertEqual(chatbots_custom_filters.format_to_k(None), None)

    def test_attr(self):
        from django import forms

        class TestForm(forms.Form):
            test_field = forms.CharField()

        form = TestForm()
        field = form['test_field']
        rendered_field = chatbots_custom_filters.attr(field, "class:form-control")

        self.assertIn('class="form-control"', rendered_field)
