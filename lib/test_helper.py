from .helper import extract_value, extract_german_date


def test_extract_value():
    assert extract_value('12 %') == 12
    assert extract_value('12,2 %') == 12.2
    assert extract_value('12%') == 12
    assert extract_value('12,2%') == 12.2
    assert extract_value('xxxx') == 'xxxx'
    assert extract_value(12) == 12


def test_extract_german_date():
    assert extract_german_date('xxx') == 'xxx'
    assert extract_german_date('7. Wahl vom 22. März 1970') == '1970-03-22'
