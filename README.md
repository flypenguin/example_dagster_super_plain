# weird job behavior

## TL;DR

```
pip install .
python -m dagster dev -m user
```

## Observations

- the "nothing job" is executed _twice_ on startup,
- then regularly once per minute,
- while the called operation is not executed at all.

relevant code:

```python
# user/__init__.py, line 14
@job
def nothing_job():
    print("nothing job")
    nothing_op()
```

## Console output

```
$ python -m dagster dev -m user
2023-02-26 14:05:54 +0100 - dagster - INFO - Using temporary directory /some/dir/dagster_playground/tmpiinl8zni for storage. This will be removed when dagster dev exits.
2023-02-26 14:05:54 +0100 - dagster - INFO - To persist information across sessions, set the environment variable DAGSTER_HOME to a directory to use.
2023-02-26 14:05:55 +0100 - dagster - INFO - Launching Dagster services...
nothing job
2023-02-26 14:05:56 +0100 - dagster.daemon - INFO - Instance is configured with the following daemons: ['BackfillDaemon', 'SchedulerDaemon', 'SensorDaemon']
2023-02-26 14:05:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:05:57 +0100 - dagit - WARNING - Port 3000 is in use - using port 57048 instead
2023-02-26 14:05:57 +0100 - dagit - INFO - Serving dagit on http://127.0.0.1:57048 in process 56236
2023-02-26 14:06:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:07:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:08:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:09:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:10:56 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:11:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:12:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:13:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:14:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:15:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job
2023-02-26 14:16:57 +0100 - dagster.daemon.SensorDaemon - INFO - Not checking for any runs since no sensors have been started.
nothing job

...
```
