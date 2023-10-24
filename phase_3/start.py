import subprocess


def execute_command(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())


if __name__ == "__main__":
    # Execute the commands with real-time output
    execute_command("docker-compose down")
    execute_command("docker container prune -f")
    execute_command("docker build  --no-cache --secret id=nginx-key,src=nginx-repo.key "
                    "--secret id=nginx-crt,src=nginx-repo.crt -t nginxplus .")
    execute_command("docker-compose up")
