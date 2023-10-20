import click
from src.log_parser import LogParser


@click.command()
@click.option("-f", "--logfile", help="absolute/relative path to log file to parse")
@click.option("-d", "--logdir", help="absolute/relative path to log directory with log files to parse")
def parse(logfile, logdir):
    if logfile:
        print(f"Parse {logfile}")
        parser = LogParser(logfile)
        print(f"общее количество выполненных запросов: {parser.get_requests_count()}")
        print(f"количество запросов по HTTP-методам: {parser.get_methods_requests_count()}")
        print(f"топ 3 IP адресов, с которых были сделаны запросы: {parser.get_top_ip(count=3)}")
    elif logdir:
        print(f"Parse {logdir}")


if __name__ == "__main__":
    parse()
