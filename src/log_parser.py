import subprocess

from src.base_command import BaseCommand

HTTP_METHODS = ["POST", "GET", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]


class LogParser(BaseCommand):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_methods_requests_count(self):
        requests_list = {}

        for method in HTTP_METHODS:
            method_requests = self._get_requests_by_method(method)
            requests_list[method] = len(method_requests)

        return requests_list

    def get_requests_count(self):
        return len(self.cmd_run(["cat", self.file_path]))

    def _get_requests_by_method(self, method):
        return self.cmd_pipe_run(["cat", self.file_path], ["grep", method])

    def get_top_ip(self, count=3):
        result = self.cmd_pipe_run(["awk", "{print $1}", self.file_path],
                                   ["sort"],
                                   ["uniq", "-c"],
                                   ["sort", "-rn"],
                                   ["head", f"-{count}"])

        return [line.split()[1] for line in result]

    def get_long_requests(self, count=3, sort="DESC"):
        pass
