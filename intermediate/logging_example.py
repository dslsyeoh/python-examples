import logging.config

# logging.basicConfig(filename='log/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
#
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')
#
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')
#
logging.config.fileConfig(fname='../resources/config/logger.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
