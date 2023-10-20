import subprocess


class BaseCommand():

    @staticmethod
    def cmd_run(command: [str], capture_output=True, text=True) -> list[str]:
        result = subprocess.run(command, capture_output=capture_output, text=text)
        return BaseCommand._clear(result.stdout.strip().split("\n"))

    @staticmethod
    def cmd_pipe_run(*commands) -> list[str]:
        prev_process = process = None
        for cmd in commands:
            if prev_process is None:
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
            else:
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=prev_process.stdout, text=True)
            prev_process = process

        result, _ = process.communicate()

        return BaseCommand._clear(result.strip().split("\n"))

    @staticmethod
    def _clear(lst):
        return list(filter(None, lst))
