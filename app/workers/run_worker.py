import sys

from workers.whisper_worker import WhisperWorker


WORKERS = {
    "whisper": WhisperWorker,
}


def main():

    if len(sys.argv) != 2:

        raise RuntimeError(
            "Usage: python run_worker.py whisper"
        )

    worker_name = sys.argv[1]

    if worker_name not in WORKERS:

        raise RuntimeError(
            f"Unknown worker: {worker_name}"
        )

    worker = WORKERS[worker_name]()

    worker.start()


if __name__ == "__main__":

    main()