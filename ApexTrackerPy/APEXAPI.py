# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import requests


def checkplatform(platform):
    """
    Check if the platform is valid.
    :param platform: The platform to check.
    """
    if platform == 'PC' or platform == 'PS4' or platform == 'X1':
        return True
    else:
        return False

def GetApexPlayerStatus(api_key, platform, playerName, *Isuid):
    """
    Get the status of a player on Apex Legends.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param playerName: The player name to use.
    :param Isuid: If the player name is a UUID.
    """
    if checkplatform(platform or Isuid):
        url = ""
        if Isuid:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&uid={playerName}'
        else:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={playerName}'
        try:
            response = requests.get(url, headers={'Authorization': api_key})
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception('HttpError!:The API returned status code '+str(response.status_code))
        except Exception as e:
            raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))
    else:
        raise Exception('Invalid platform!')


def GetApexMapRotation(api_key):
    """
    Get the map rotation of Apex Legends.
    :param api_key: The API key to use.
    """
    url = f'https://api.mozambiquehe.re/maprotation?version=2'
    try:
        response = requests.get(url, headers={'Authorization': api_key})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('HttpError!:The API returned status code '+str(response.status_code))
    except Exception as e:
        raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))

def GetApexNews(api_key, *language):
    """
    Get the news of Apex Legends.
    :param api_key: The API key to use.
    :param language: The language to use.(default: en-us)
    """
    url = ''
    if language:
        url = f'https://api.mozambiquehe.re/news?lang={language}'
    else:
        url = f'https://api.mozambiquehe.re/news?lang=en-us'
    try:
        response = requests.get(url, headers={'Authorization': api_key})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('HttpError!:The API returned status code '+str(response.status_code))
    except Exception as e:
        raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))


def GetApexServerStatus(api_key):
    """
    get the status of Apex Legends servers.
    :param api_key: The API key to use.
    Warning
    You must put either a clickable link to "https://apexlegendsstatus.com" OR have a message such as "Data from apexlegendsstatus.com" when displaying data coming from this API. Your key may be suspended otherwise.
    """
    url = 'https://api.mozambiquehe.re/servers'
    try:
        response = requests.get(url, headers={'Authorization': api_key})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('HttpError!:The API returned status code '+str(response.status_code))
    except Exception as e:
        raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))


def CallOriginAPI(api_key, PlayerName):
    """
    Call the Origin API.
    :param api_key: The API key to use.
    :param PlayerName: The player name to use.
    """
    url = f'https://api.mozambiquehe.re/origin?player={PlayerName}'
    try:
        response = requests.get(url, headers={'Authorization': api_key})
        if response.status_code == 200 or response.status_code == 500:
            # 何故か現状500が返ってくる
            return response.json()
        else:
            raise Exception('HttpError!:The API returned status code '+str(response.status_code))
    except Exception as e:
        raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))