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

''' This script configures some basic logging

We import logging, thenconfigure our logging to output to a file, and set it

'''
