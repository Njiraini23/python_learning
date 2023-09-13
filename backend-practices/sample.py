import logging

logger = logging.getlogger(__name__)

logging.basicConfig(filename='employee.log', level=logging_INFO,
        format='%(levelname)s:%(name)s:%(message)s')

class Employee:
    """A simple Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

        @property
        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)

        @property
        def fullname(self):
            return '{} {}'.format(self.first, self.last)
