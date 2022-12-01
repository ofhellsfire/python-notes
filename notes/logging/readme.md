# Logging Notes

The following code snippet shows how you can use all the five logging levels 
with the syntax: `logging.<level>(<message>)`

```
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
```

Defaul logging level is `WARNING`.

## Log to a File Example

```
logging.basicConfig(
    level=logging.INFO, 
    filename="py_log.log", 
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("An INFO")
logging.error("An ERROR")
```

`filemode="w"` - will overwrite logs
`filemode="a"` - will append logs

## Exception Logging Example

```
x = 10
y = 0
try:
    x/y
    logging.info(f"x/y successful with result: {x/y}.")
except ZeroDivisionError as err:
    logging.exception("ZeroDivisionError")
    # alternative
    # logging.error("ZeroDivisionError", exc_info=True)
```

## Custom Logger Example

```
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# configure the handler and formatter for logger
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# add formatter to the handler
handler.setFormatter(formatter)
# add handler to the logger
logger.addHandler(handler)

logger.info(f"Testing the custom logger for module {__name__}...")
```

## TODO: add custom logger example with console and file handlers

TODO

## Logging Best Practices

### Set the optimal logging level

Logs are helpful only when you can use them to track down important errors that 
need to be fixed. Depending on the specific application, be sure to set the optimal 
logging level. Logging too many events can be suboptimal from a debugging viewpoint 
as it’s difficult to filter through the logs to identify errors that require 
immediate attention.

### Configure loggers at the module level

When you’re working on an application with multiple modules, you should consider 
configuring a logger for each module. Setting the name of the logger to `__name__` 
helps identify the modules in your application that have issues you need to fix.

### Include timestamps and ensure consistent formatting

Always include timestamps in logs as they’re helpful in tracing back to when an 
error occurred. Format your logs consistently across the different modules in your application.

### Rotate the log files to facilitate easier debugging

When working on large applications with several modules, it’s likely that your 
log files will be very large in size. As it’s challenging to filter through such 
large logs to detect errors, you should consider rotating the log files. You can 
do this by using the `RotatingFileHandler` with the syntax: 
`logging.handlers.RotatingFileHandler(filename, maxBytes,backupCount)`
