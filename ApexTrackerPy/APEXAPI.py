# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import requests
import ApexTrackerPy.Apexclass

# private void
def _checkplatform(platform):
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

    if _checkplatform(platform or Isuid):
        url = ""
        if Isuid:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&uid={playerName}'
        else:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={playerName}'
        try:
            response = requests.get(url, headers={'Authorization': api_key})
            if response.status_code == 200:
                r = response.json()
                res = ApexTrackerPy.Apexclass.A_Player_Data(
                    row_json=r, 
                    name=r["global"]["name"], 
                    uid=r["global"]["uid"],
                    avatar_url=r["global"]["avatar"],
                    level=r["global"]["level"], 
                    Isban=r["global"]["bans"]["isActive"],
                    Rank_RP=r["global"]["rank"]["rankScore"],
                    CurrentRank=r["global"]["rank"]["rankName"], 
                    Arena_Rank_RP=r["global"]["arena"]["rankScore"],
                    Arena_Current_Rank=r["global"]["arena"]["rankName"],
                    battlepass_level=r["global"]["battlepass"]["level"],
                    badges_json=r["global"]["badges"],
                    Player_status=r["realtime"],
                    legends_json=r["legends"],
                    total_kill=r["total"]["kills"]["value"],
                    total_damage=r["total"]["damage"]["value"]
                    )
                return res
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
            r =  response.json()
            res = ApexTrackerPy.Apexclass.A_Map_Rotation(
                row_json=r,
                BattleRoyal_Current_Map=r["battle_royale"]["current"]["map"],
                BattleRoyal_Current_Image=r["battle_royale"]["current"]["asset"],
                BattleRoyal_Current_Start_Time=r["battle_royale"]["current"]["start"],
                BattleRoyal_Current_Start_Time_datetime=r["battle_royale"]["current"]["readableDate_start"],
                BattleRoyal_Current_End_Time=r["battle_royale"]["current"]["end"],
                BattleRoyal_Current_End_Time_datetime=r["battle_royale"]["current"]["readableDate_end"],
                BattleRoyal_Current_remainingTimer=r["battle_royale"]["current"]["remainingTimer"],
                BattleRoyal_Next_Map=r["battle_royale"]["next"]["map"],
                BattleRoyal_Next_Start_Time=r["battle_royale"]["next"]["start"],
                BattleRoyal_Next_End_Time=r["battle_royale"]["next"]["end"],
                BattleRoyal_Next_Start_Time_datetime=r["battle_royale"]["next"]["readableDate_start"],
                BattleRoyal_Next_End_Time_datetime=r["battle_royale"]["next"]["readableDate_end"],
                Arena_Current_Map=r["arenas"]["current"]["map"],
                Arena_Current_Image=r["arenas"]["current"]["asset"],
                Arena_Current_Start_Time=r["arenas"]["current"]["start"],
                Arena_Current_Start_Time_datetime=r["arenas"]["current"]["readableDate_start"],
                Arena_Current_End_Time=r["arenas"]["current"]["end"],
                Arena_Current_End_Time_datetime=r["arenas"]["current"]["readableDate_end"],
                Arena_Current_remainingTimer=r["arenas"]["current"]["remainingTimer"],
                Arena_Next_Map=r["arenas"]["next"]["map"],
                Arena_Next_Start_Time=r["arenas"]["next"]["start"],
                Arena_Next_End_Time=r["arenas"]["next"]["end"],
                Arena_Next_Start_Time_datetime=r["arenas"]["next"]["readableDate_start"],
                Arena_Next_End_Time_datetime=r["arenas"]["next"]["readableDate_end"],
                Ranked_Current_Map=r["ranked"]["current"]["map"],
                Ranked_Current_Image=r["ranked"]["current"]["asset"],
                Ranked_next_Map=r["ranked"]["next"]["map"],
                ArenaRanked_Current_Map=r["arenasRanked"]["current"]["map"],
                ArenaRanked_Current_Image=r["arenasRanked"]["current"]["asset"],
                ArenaRanked_Current_Start_Time=r["arenasRanked"]["current"]["start"],
                ArenaRanked_Current_End_Time=r["arenasRanked"]["current"]["end"],
                ArenaRanked_Current_Start_Time_datetime=r["arenasRanked"]["current"]["readableDate_start"],
                ArenaRanked_Current_End_Time_datetime=r["arenasRanked"]["current"]["readableDate_end"],
                ArenaRanked_Current_remainingTimer=r["arenasRanked"]["current"]["remainingTimer"],
                ArenaRanked_Next_Map=r["arenasRanked"]["next"]["map"],
                ArenaRanked_Next_Start_Time=r["arenasRanked"]["next"]["start"],
                ArenaRanked_Next_End_Time=r["arenasRanked"]["next"]["end"],
                ArenaRanked_Next_Start_Time_datetime=r["arenasRanked"]["next"]["readableDate_start"],
                ArenaRanked_Next_End_Time_datetime=r["arenasRanked"]["next"]["readableDate_end"]
                )
            return res
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

def GetUIDbyName(api_key, platform, PlayerName):
    """
    Get the UUID of a player by his name.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param PlayerName: The player name to use.
    """
    if _checkplatform(platform):
        url = f'https://api.mozambiquehe.re/nametouid?player={PlayerName}&platform={platform}'
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