# examples/python-volume-writers

This repository contains a Python application demonstrating shared volume use between services for deployment on Convox. The application comprises two writing services, each persistently writing to its designated file within a shared volume, showcasing data persistence and sharing capabilities.

Key components:
* [Dockerfile](Dockerfile)
* [convox.yml](convox.yml)
* [writer1.py](writer1.py)
* [writer2.py](writer2.py)

## Features

1. **Writer 1 Service**: Writes timestamped messages to `writer1.txt` in the shared volume at fixed intervals.
2. **Writer 2 Service**: Operates similarly to Writer 1, targeting `writer2.txt`, to illustrate multiple services writing to the same volume.

## Shared Volume

The services utilize a Docker volume mounted at `/my/shared/data`, facilitating data sharing and persistence across container restarts and deployments. This model is useful for applications requiring data availability across multiple service instances or container lifecycles.

## Setup and Deployment

For deployment on Convox, ensure the Convox CLI is installed and configured to interact with your Convox Rack. Deploy the application by executing:

```bash
convox deploy
```

This command builds and deploys the application according to the specifications in `convox.yml`, creating the necessary services and volume configuration.

## Observing Output

After deploying your services, you can inspect the operations and outputs of the writer services as follows:

1. **List Services**: Check the active services using the `convox services` command. You should see your writer services listed:

```bash
SERVICE  DOMAIN  PORTS
writer1
writer2
```

2. **Check Running Processes**: To view the currently running processes and their IDs, use `convox ps`. This will display all active processes:

```bash
ID            SERVICE  STATUS   RELEASE      STARTED         COMMAND
[PROCESS_ID]  writer1  running  [RELEASE]    27 seconds ago  sh -c 'python writer1.py'
[PROCESS_ID]  writer2  running  [RELEASE]    27 seconds ago  sh -c 'python writer2.py'
```

3. **Access Container Shell**: To exec into a running container, use `convox exec` followed by the process ID and the shell command. For example:

```bash
convox exec [PROCESS_ID] sh
```

4. **Navigate and Inspect**: Within the container's shell, navigate to the shared volume directory and inspect the files written by the services:

```bash
# Navigate to shared data directory
cd /my/shared/data
# List files to confirm presence
ls
writer1.txt  writer2.txt
# Display contents of writer1's file
cat writer1.txt
Writer 1 wrote at [timestamp]
# Display contents of writer2's file
cat writer2.txt
Writer 2 wrote at [timestamp]
```

This process allows you to directly observe the output files `writer1.txt` and `writer2.txt` being updated in real-time by the writer services, demonstrating the shared volume functionality.
