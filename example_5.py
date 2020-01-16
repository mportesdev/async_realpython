import queue

from codetiming import Timer
import requests


def task(name, work_queue):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    with requests.Session() as session:
        while not work_queue.empty():
            url = work_queue.get()
            print(f'Task {name} getting URL: {url}')
            timer.start()
            session.get(url)
            timer.stop()
            yield


def main():
    work_queue = queue.Queue()

    for url in [
        'https://google.com',
        'https://yahoo.com',
        'https://linkedin.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://facebook.com',
        'https://twitter.com',
    ]:
        work_queue.put(url)

    tasks = [task('One', work_queue), task('Two', work_queue)]

    done = False
    with Timer(text='\nTotal elapsed time: {:.1f}'):
        while not done:
            for t in tasks:
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)
                if len(tasks) == 0:
                    done = True


if __name__ == '__main__':
    main()
