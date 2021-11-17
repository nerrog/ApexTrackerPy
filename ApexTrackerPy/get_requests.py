# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import requests

def get_request(url, headers):
    """
    Get request
    """
    try:
        r = requests.get(url,headers=headers,timeout=10)
        time_elapsed = r.elapsed.total_seconds()
        return r, "".join([str(round(time_elapsed, 2)), " sec"])
    except Exception as e:
        return e