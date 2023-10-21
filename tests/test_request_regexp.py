import pytest
from src.log_parser import LogParser


@pytest.mark.parametrize("pattern, request_log, exp_result", [(
    r"(?P<ip>(?:\d{1,3}\.){3}\d{1,3}) \S+ \S+ "
    r"\[(?P<datetime>\d{1,2}/[a-z]+/\d{4}(?:\:\d{2}){3} \+\d{4})\] "
    r"\"(?P<method>[HEAD|POST|GET|OPTIONS|DELETE|PUT|CONNECT|TRACE|PATCH]+) (?P<url>/[^ ]+) "
    r"HTTP/[\d\.]+\" \d{3} "
    r"\d+ \".+\" \".+\" (?P<duration>\d+)",

    "100.1.14.108 - - [22/Sep/2019:22:53:30 +0200] \"HEAD "
    "/index.php?option=com_content&view=article'A=0&id=46&Itemid=54 HTTP/1.1\" 500 0 \"-\" "
    "\"python-requests/2.22.0\" 9149",

    "HEAD /index.php?option=com_content&view=article'A=0&id=46&Itemid=54 100.1.14.108 9149 22/Sep/2019:22:53:30 +0200")
])
def test_request_regexp(pattern, request_log, exp_result):
    result = LogParser("").parse_request(pattern, request_log)
    assert result == exp_result
