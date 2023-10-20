import json

import click
from src.log_parser import LogParser
from src.utils import json_dump, print_dict


def parse_access_log(logfile):
    print(f"Parse {logfile}")
    parser = LogParser(logfile)
    output = {
        "общее количество выполненных запросов": parser.get_requests_count(),
        "количество запросов по HTTP-методам": parser.get_methods_requests_count(),
        "топ 3 IP адресов, с которых были сделаны запросы": parser.get_top_ip(count=3),
    }

    return output


@click.command()
@click.option("-f", "--logfile", help="path to log file to parse")
@click.option("-d", "--logdir", help="path to log directory with log files to parse")
@click.option("-o", "--output", default="./results.json", help="path to output json file")
def parse(logfile, logdir, output):
    if logfile:
        data = parse_access_log(logfile)
        print_dict(data)
        json_dump([data], output)
    elif logdir:
        print(f"Parse {logdir}")


if __name__ == "__main__":
    parse()

