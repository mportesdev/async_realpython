import queue


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f'Task {name} running')
        for x in range(count):
            total += 1
            yield
        print(f'Task {name} total: {total}')


def main():
    work_queue = queue.Queue()

    for work in [8, 5, 3, 1]:
        work_queue.put(work)

    tasks = [task('One', work_queue), task('Two', work_queue)]

    done = False
    while not done:
        for t in tasks[:]:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == '__main__':
    main()
