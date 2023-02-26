# weird job behavior

## TL;DR

```shell
python -m dagster dev -m user
```

## Observations

- the "nothing job" is executed _twice_ on startup.

## Console output

```
$ python -m dagster dev -m user
2023-02-26 13:38:52 +0100 - dagster - INFO - Using temporary directory /some/dir/dagster_playground/tmpn0dh4hkt for storage. This will be removed when dagster dev exits.
2023-02-26 13:38:52 +0100 - dagster - INFO - To persist information across sessions, set the environment variable DAGSTER_HOME to a directory to use.
2023-02-26 13:38:52 +0100 - dagster - INFO - Launching Dagster services...
nothing job
2023-02-26 13:38:54 +0100 - dagster.daemon - INFO - Instance is configured with the following daemons: ['BackfillDaemon', 'SchedulerDaemon', 'SensorDaemon']
2023-02-26 13:38:54 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 13:38:54 +0100 - dagit - WARNING - Port 3000 is in use - using port 56389 instead
2023-02-26 13:38:54 +0100 - dagit - INFO - Serving dagit on http://127.0.0.1:56389 in process 55329
^C
2023-02-26 13:39:01 +0100 - dagster - INFO - Shutting down Dagster services...
2023-02-26 13:39:01 +0100 - dagster.daemon - INFO - Received interrupt, shutting down daemon threads...
2023-02-26 13:39:01 +0100 - dagster.daemon - INFO - Daemon threads shut down.
2023-02-26 13:39:01 +0100 - dagster - INFO - Dagster services shut down.
```
