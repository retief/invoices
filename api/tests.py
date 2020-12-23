from django.test import TestCase

from api import invoices, test_data


class TestParseField(TestCase):
    def test_works(self):
        self.assertEqual(
            invoices.parse_field(
                {
                    "label": "foo",
                    "text": "bar",
                    "confidence": {
                        "foo": 1,
                    },
                }
            ),
            ("foo", "bar", 1),
        )


class TestParseFields(TestCase):
    def test_basic(self):
        self.assertEqual(
            invoices.parse_fields(
                [
                    {
                        "label": "foo",
                        "text": "bar",
                        "confidence": {
                            "foo": 1,
                        },
                    },
                    {
                        "label": "a",
                        "text": "b",
                        "confidence": {
                            "a": 1,
                        },
                    },
                ]
            ),
            {"foo": "bar", "a": "b"},
        )

    def test_better_accuracy_overrides(self):
        self.assertEqual(
            invoices.parse_fields(
                [
                    {
                        "label": "foo",
                        "text": "bash",
                        "confidence": {
                            "foo": 0.5,
                        },
                    },
                    {
                        "label": "foo",
                        "text": "bar",
                        "confidence": {
                            "foo": 0.9,
                        },
                    },
                ]
            ),
            {"foo": "bar"},
        )

    def test_lower_accuracy_no_override(self):
        self.assertEqual(
            invoices.parse_fields(
                [
                    {
                        "label": "foo",
                        "text": "bar",
                        "confidence": {
                            "foo": 0.9,
                        },
                    },
                    {
                        "label": "foo",
                        "text": "bash",
                        "confidence": {
                            "foo": 0.5,
                        },
                    },
                ]
            ),
            {"foo": "bar"},
        )


class TestParseInvoice(TestCase):
    def test_handles_real_file(self):
        self.assertEqual(invoices.parse_invoice(test_data.original), test_data.expected)
