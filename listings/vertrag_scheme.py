import ExactComparator, NameComparator, DateComparator, BooleanComparator

SCHEME = {
  "type": {"type": "string", "comparator": ExactComparator()},
  "name_child": {"type": "string", "comparator": NameComparator()},
  "birthday_child": {"type": "date", "comparator": DateComparator()},
  "start_date_apprenticeship": {"type": "date", "comparator": DateComparator()},
  "end_date_apprenticeship": {"type": "date", "comparator": DateComparator()},
  "date_document": {"type": "date", "comparator": DateComparator()},
  "stamp_company": {"type": "boolean", "comparator": BooleanComparator()},
  "signature_company": {"type": "boolean", "comparator": BooleanComparator()},
  "signature_child": {"type": "boolean", "comparator": BooleanComparator()},
  "signature_legal_guardian": {"type": "boolean", "comparator": BooleanComparator()},
}