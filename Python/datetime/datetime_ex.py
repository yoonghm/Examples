import datetime

print(f'Local time                     = {datetime.datetime.now()}')
print(f'Local to ISO8601               = {datetime.datetime.now().isoformat()}')
print(f'UTC to ISO8601                 = {datetime.datetime.utcnow().isoformat()}')
print(f'Local to ISO8601 without ms    = {datetime.datetime.now().replace(microsecond=0).isoformat()}')
print(f'Local to ISO8601 with timezone = {datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()}')

"""
Local time                     = 2018-05-20 08:25:52.644539
Local to ISO8601               = 2018-05-20T08:25:52.660137
UTC to ISO8601                 = 2018-05-20T00:25:52.660137
Local to ISO8601 without ms    = 2018-05-20T08:25:52
Local to ISO8601 with timezone = 2018-05-20T00:25:52.660137+00:00
"""
