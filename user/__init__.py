from dagster import job, op, asset, repository


@asset
def nothing_asset():
    return "./nothing.txt"


@op
def nothing_op():
    print("nothing op")


@job
def nothing_job():
    print("nothing job")
    nothing_op()
