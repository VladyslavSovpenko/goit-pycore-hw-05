import re

LOG_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|DEBUG|ERROR|WARNING) (.+)')
