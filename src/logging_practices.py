import logging
from logging.handlers import RotatingFileHandler

"""
Logging is an essential part of any application, as it helps in monitoring, debugging, and understanding the behavior of the application. Here are some best practices for logging in Python:

### 1. Use the `logging` Module

Python's built-in `logging` module is powerful and flexible. It allows you to log messages with different severity levels and configure different handlers for output.

### 2. Set Up a Basic Configuration

Start with a basic configuration to set the logging level and format.

```python
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

### 3. Use Appropriate Logging Levels

Use the appropriate logging levels to indicate the severity of the messages:

- `DEBUG`: Detailed information, typically of interest only when diagnosing problems.
- `INFO`: Confirmation that things are working as expected.
- `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
- `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
- `CRITICAL`: A very serious error, indicating that the program itself may be unable to continue running.

### 4. Avoid Using `print` Statements for Logging

Replace `print` statements with appropriate logging calls.

```python
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

### 5. Use Loggers

Create loggers for different parts of your application. This allows you to control logging behavior for different modules independently.

```python
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

### 6. Configure Handlers

Use handlers to direct log messages to different destinations, such as the console, files, or external systems.

```python
# Create a file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

### 7. Use Contextual Information

Include contextual information in your log messages to make them more informative.

```python
user = 'Alice'
action = 'login'
logger.info('User %s performed %s action', user, action)
```

### 8. Avoid Logging Sensitive Information

Be cautious about logging sensitive information such as passwords, personal data, or confidential information.

### 9. Rotate Log Files

Use log rotation to manage log file sizes and avoid filling up the disk.

```python
from logging.handlers import RotatingFileHandler

# Create a rotating file handler
rotating_handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)
```

### 10. Use External Logging Services

For larger applications, consider using external logging services like Loggly, Splunk, or ELK Stack for centralized logging and analysis.

### Full Example

Here is a full example that incorporates these best practices:

```python
import logging
from logging.handlers import RotatingFileHandler

# Set up basic configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Create handlers
file_handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
console_handler = logging.StreamHandler()

# Set levels for handlers
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Example with contextual information
user = 'Alice'
action = 'login'
logger.info('User %s performed %

s

 action', user, action)
```

### Summary

By following these best practices, you can set up effective logging in your Python applications, making it easier to monitor, debug, and understand the behavior of your application.


"""

# Set up basic configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Create handlers
file_handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
console_handler = logging.StreamHandler()

# Set levels for handlers
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Example with contextual information
user = 'Alice'
action = 'login'
logger.info('User %s performed %s action', user, action)