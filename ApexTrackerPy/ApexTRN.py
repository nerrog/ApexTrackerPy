# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import requests

API_VER = 'v2'

def checkplatform(platform):
    """
    Check if the platform is valid.
    :param platform: The platform to check.
    """
    if platform == 'origin' or platform == 'psn' or platform == 'xbl':
        return True
    else:
        return False

def GetApexPlayerStatus_TRN(api_key, platform, playerName):
    """
    Get the status of a player on Apex Legends.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param playerName: The player name to use.
    """
    if checkplatform(platform):
        url = f'https://public-api.tracker.gg/{API_VER}/apex/standard/profile/{platform}/{playerName}'
        try:
            response = requests.get(url, headers={'TRN-Api-Key': api_key})
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception('HttpError!:The API returned status code '+str(response.status_code))
        except Exception as e:
            raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))
    else:
        raise Exception('Invalid platform!')

def GetApexPlayersMatchHistory_TRN(api_key, platform, playerName):
    """
    Get the match history of a player on Apex Legends.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param playerName: The player name to use.
    """
    if checkplatform(platform):
        url = f'https://public-api.tracker.gg/{API_VER}/apex/standard/profile/{platform}/{playerName}/sessions'
        try:
            response = requests.get(url, headers={'TRN-Api-Key': api_key})
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception('HttpError!:The API returned status code '+str(response.status_code))
        except Exception as e:
            raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))
    else:
        raise Exception('Invalid platform!')