from dagster import job, op, asset, repository


@job
def nothing_job():
    print("nothing job")


@asset
def nothing_asset():
    return "./nothing.txt"


@op
def nothing_op():
    ...


@repository
def repo():
    # no ops in repository ...
    return [
        nothing_job,
        nothing_asset,
    ]
