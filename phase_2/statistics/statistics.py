import docker
import time


def make_float(string):
    try:
        return float(string)
    except ValueError:
        return False


def get_logs():
    avg_response_time = 0
    counter = 0

    docker_client = docker.from_env()
    clients = [container for container in docker_client.containers.list() if ('client' in container.name)]

    for client in clients:
        logs = client.logs()
        for log in logs.decode("utf-8").split("\n"):
            response_time = make_float(log.split("|")[-1])

            if not response_time:
                continue

            if not counter:
                counter = 1
                avg_response_time = response_time

            # Compute the new avg response time
            counter, avg_response_time = counter + 1, (avg_response_time * counter + response_time) / (counter + 1)

    return counter, avg_response_time


if __name__ == "__main__":
    while True:
        time.sleep(10)
        counter, avg_response_time = get_logs()
        print(f"Average time for resolving {counter} requests: {avg_response_time}")
