import click
from src.log_parser import LogParser


@click.command()
@click.option("--logfile", help="Path to log file")
@click.option("--logdir", help="Path to log dir, only if logfile is not provided")
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
