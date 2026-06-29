import logging

logging.basicConfig(
    filename = 'applog.log',
    level = logging.DEBUG,
    format=(
        '{asctime} \n'
        '{levelname} - {pathname} @line {lineno} \n'
        '{message}'
    ),
    style='{'
)

logging.debug('This is an example of a debug message.')
logging.info('This is an example of an info level message.')
logging.warning('And example of a warning log message.')
logging.error('This one is an example of an error event message.')
logging.critical('And finally, an example of a critical event message in log')

'''
This script configures basic logging for the application.

- Imports the `logging` module.
- Configures logging to write to 'applog.log'.
- Sets the logging level to DEBUG (captures DEBUG and higher).
- Defines a custom format that includes:
    * Timestamp ({asctime})
    * Log level ({levelname})
    * File path and line number ({pathname}, {lineno})
    * The log message itself ({message})

The script then demonstrates logging at all severity levels:
DEBUG, INFO, WARNING, ERROR, and CRITICAL.
'''

