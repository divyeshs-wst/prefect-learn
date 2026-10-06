from prefect import flow, task


@task
def read_file():
    print("Reading file...")
    return [1, 2, 3]


@task
def process_data(data):
    print("Processing data...")
    return [x * 2 for x in data]


@task
def save_data(data):
    print("Saving data...")
    print(data)


@flow
def process_file():
    data = read_file()
    processed = process_data(data)
    save_data(processed)


if __name__ == "__main__":
    process_file()