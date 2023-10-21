import subprocess


class BaseCommand:

    @staticmethod
    def cmd_run(command: list[str], capture_output=True, text=True) -> list[str]:
        result = subprocess.run(command, capture_output=capture_output, text=text)
        return BaseCommand._remove_empty_strings(result.stdout.strip().split("\n"))

    @staticmethod
    def cmd_pipe_run(*commands) -> list[str]:
        prev_process = process = None
        for cmd in commands:
            stdin = prev_process.stdout if prev_process else None
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=stdin, text=True)
            prev_process = process

        result, _ = process.communicate()

        return BaseCommand._remove_empty_strings(result.strip().split("\n"))

    @staticmethod
    def _remove_empty_strings(lst):
        return list(filter(None, lst))
