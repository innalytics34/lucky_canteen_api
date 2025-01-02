import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='canteen_error.log',  # Log file
    filemode='a'  # Append to the file
)

# Create a custom logger
logger = logging.getLogger('canteen_api')