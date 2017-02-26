import logging
def funcn(w):
    logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s   %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    logging.info(w)
