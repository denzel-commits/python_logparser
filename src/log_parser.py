import re

from src.base_command import BaseCommand

HTTP_METHODS = ["POST", "GET", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]


class LogParser(BaseCommand):
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_access_log(self):
        print(f"Parse {self.file_path}")
        output = {
            "общее количество выполненных запросов": self.get_requests_count(),
            "количество запросов по HTTP-методам": self.get_methods_requests_count(),
            "топ 3 IP адресов, с которых были сделаны запросы": self.get_top_ip(count=3),
            "топ 3 самых долгих запросов": self.get_long_requests(count=3),
        }

        return output

    def get_methods_requests_count(self):
        requests_list = {}

        for method in HTTP_METHODS:
            method_requests = self._get_requests_by_method(method)
            requests_list[method] = method_requests

        return requests_list

    def get_requests_count(self):
        return self.cmd_pipe_run(["cat", self.file_path], ["wc", "-l"])[0]

    def _get_requests_by_method(self, method):
        return self.cmd_pipe_run(["grep", method, self.file_path], ["wc", "-l"])[0]

    def get_top_ip(self, count=3):
        result = self.cmd_pipe_run(["awk", "{print $1}", self.file_path],
                                   ["sort"],
                                   ["uniq", "-c"],
                                   ["sort", "-rn"],
                                   ["head", f"-{count}"])

        return [line.split()[1] for line in result]

    def get_long_requests(self, count=3):
        results = self.cmd_pipe_run(["grep", "-Eo", "(.*)[0-9]+$", self.file_path],
                                    ["sort", "-t", " ", "-k9,9rn"],
                                    ["head", f"-{count}"])

        return [self.parse_request((self.request_pattern()), request_log) for request_log in results]

    @staticmethod
    def parse_request(pattern, request_log):
        match = re.search(pattern, request_log, re.IGNORECASE)

        if match:
            return (f"{match.group('method')} {match.group('url')} {match.group('ip')} {match.group('duration')} "
                    f"{match.group('datetime')}")

        return None

    @staticmethod
    def request_pattern():
        return r"(?P<ip>(?:\d{1,3}\.){3}\d{1,3}) \S+ \S+ " \
               r"\[(?P<datetime>\d{1,2}/[a-z]+/\d{4}(?:\:\d{2}){3} \+\d{4})\] " \
               r"\"(?P<method>[" + ("|".join(HTTP_METHODS)) + r"]+) (?P<url>/[^ ]+) HTTP/[\d\.]+\" \d{3} " \
               r"\d+ \".+\" \".+\" (?P<duration>\d+)"
