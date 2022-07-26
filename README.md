# random-statsd-client
Export a 'random' metric every 5 seconds.

Why create this?  Just to test statsd client in python.

## Start the Server

Start it in the background.

```
python src/mock_statsd_server.py &
```

## Start the Client

```
python src/myapp.py
```

## Options
Configuration is done via env variables.

Server and Client:
* STATSD_SERVER: server's name or address, default="localhost"
* STATSD_PORT: server's port, default=8125

Client:
* SLEEP_SECONDS: number of seconds to sleep between each update, default=5
