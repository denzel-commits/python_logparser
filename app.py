import click

from src.utils import json_dump, print_dict, get_logs
from src.log_parser import LogParser


@click.command()
@click.option("-f", "--logfile", help="path to log file to parse")
@click.option("-d", "--logdir", help="path to log directory with log files to parse")
@click.option("-o", "--output", default="results.json", help="path to output json file")
def parse(logfile, logdir, output):
    if logfile:
        data = LogParser(logfile).parse_access_log()

        print_dict(data)
        json_dump([data], output)

    elif logdir:
        data_list = []
        for logfile in get_logs(logdir):
            data = LogParser(logfile).parse_access_log()

            print_dict(data)
            data_list.append(data)

        json_dump(data_list, output)


if __name__ == "__main__":
    parse()

