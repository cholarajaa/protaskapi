OPEN_STATUS = 'OS'
REOPENED_STATUS = 'RE'
RESOLVED_STATUS = 'RS'
CLOSED_STATUS = 'CS'
DUPLICATE_STATUS = 'DS'

STATUS_CHOICES = (
    (OPEN_STATUS, 'Open'),
    (REOPENED_STATUS, 'Reopened'),
    (RESOLVED_STATUS, 'Resolved'),
    (CLOSED_STATUS, 'Closed'),
    (DUPLICATE_STATUS, 'Duplicate'),
)

CRITICAL = 'CR'
HIGH = 'HG'
NORMAL = 'NR'
LOW = 'LW'
VERY_LOW = 'VL'

PRIORITY_CHOICES = (
    (CRITICAL, 'Critical'),
    (HIGH, 'High'),
    (NORMAL, 'Normal'),
    (LOW, 'Low'),
    (VERY_LOW, 'Very Low'),
)