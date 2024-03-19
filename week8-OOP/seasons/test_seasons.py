import pytest
from datetime import datetime
from seasons import convert_to_data_type


def test_convert_to_data_type():
    date_string = "1995-02-27"
    expected_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    assert convert_to_data_type(date_string) == expected_date
    
    with pytest.raises(SystemExit):
        convert_to_data_type("February 27, 1995")
