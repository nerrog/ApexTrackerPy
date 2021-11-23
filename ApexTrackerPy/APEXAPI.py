# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import ApexTrackerPy.Apexclass
from ApexTrackerPy.get_requests import get_request
from ApexTrackerPy.lang import translate

# private void
def _checkplatform(platform):
    """
    Check if the platform is valid.
    :param platform: The platform to check.
    """
    if platform == 'PC' or platform == 'PS4' or platform == 'X1' or platform == 'SWITCH':
        return True
    else:
        return False

def _fixplatform(p):
    """
    Fix the platform.
    :param platform: The platform to fix.
    """
    if p == 'pc' or p == 'origin' or p == 'ORIGIN':
        return 'PC'
    elif p == 'ps4' or p == 'psn' or p == 'PSN' or p == 'PS5' or p == 'ps5':
        return 'PS4'
    elif p == 'x1' or p == 'xbox' or p == 'XBOX':
        return 'X1'
    elif p == 'switch' or p == 'SWITCH' or p == 'NINTENDO' or p == 'nintendo':
        return 'SWITCH'
    else:
        return p

def _1_ToTrue(val):
    """
    Convert 1 to True.
    :param val: The value to convert.
    """
    if val == 1:
        return True
    elif val == 0:
        return False
    else:
        return val

def GetApexPlayerStatus(api_key, platform, playerName, *Isuid):
    """
    Get the status of a player on Apex Legends.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param playerName: The player name to use.
    :param Isuid: If the player name is a UUID.
    """

    platform = _fixplatform(platform)

    if _checkplatform(platform or Isuid):
        url = ""
        if Isuid:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&uid={playerName}'
        else:
            url = f'https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={playerName}'
        try:
            res = get_request(url, {'Authorization': api_key})
            response = res[0]
            if response.status_code == 200:
                r = response.json()

                TMP_RANKED = ""
                TMP_ARENA_RANKED = ""
                if r.get("global", {}).get("rank", {}).get("rankName", {}) == None or r.get("global", {}).get("rank", {}).get("rankDiv", {}) == None:
                    TMP_RANKED = None
                else:
                    TMP_RANKED = r.get("global", {}).get("rank", {}).get("rankName", {}) + " " + str(r.get("global", {}).get("rank", {}).get("rankDiv", {}))
                if r.get("global", {}).get("arena", {}).get("rankName", {}) == None or r.get("global", {}).get("arena", {}).get("rankDiv", {}) == None:
                    TMP_ARENA_RANKED = None
                else:
                    TMP_ARENA_RANKED = r.get("global", {}).get("arena", {}).get("rankName", {}) + " " + str(r.get("global", {}).get("arena", {}).get("rankDiv", {}))

                res = ApexTrackerPy.Apexclass.A_Player_Data(
                    row_json=r, 
                    elapsed_time=res[1],
                    name=r.get("global", {}).get("name"),
                    uid=r.get("global", {}).get("uid"),
                    avatar_url=r.get("global", {}).get("avatar"),
                    level=r.get("global", {}).get("level"),
                    Isban=r.get("global", {}).get("bans", {}).get("isActive"),
                    Rank_RP=r.get("global", {}).get("rank", {}).get("rankScore"),
                    CurrentRank=translate(TMP_RANKED, "Ranked"),
                    Arena_Rank_RP=r.get("global", {}).get("arena", {}).get("rankScore"),
                    Arena_Current_Rank=translate(TMP_ARENA_RANKED, "Ranked"),
                    battlepass_level=r.get("global", {}).get("battlepass", {}).get("level"),
                    battlepass_history_list=r.get("global", {}).get("battlepass", {}).get("history"),
                    badges_json=r.get("global", {}).get("badges"),
                    Player_status=r.get("realtime"),
                    legends_json=r.get("legends"),
                    total_kill=r.get("total", {}).get("kills", {}).get("value"),
                    total_damage=r.get("total", {}).get("damage", {}).get("value"),
                    #v1.8
                    lobbyState=r.get("realtime", {}).get("lobbyState"),
                    IsOnline=_1_ToTrue(r.get("realtime", {}).get("isOnline")),
                    IsInGame=_1_ToTrue(r.get("realtime", {}).get("isInGame")),
                    canJoin=_1_ToTrue(r.get("realtime", {}).get("canJoin")),
                    PartyFull=_1_ToTrue(r.get("realtime", {}).get("partyFull")),
                    Selected_legend=r.get("realtime", {}).get("selectedLegend"),
                    CurrentState=r.get("realtime", {}).get("currentState"),
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
        res = get_request(url, {'Authorization': api_key})
        response = res[0]
        if response.status_code == 200:
            r = response.json()
            res = ApexTrackerPy.Apexclass.A_Map_Rotation(
                row_json=r,
                elapsed_time=res[1],
                BattleRoyal_Current_Map=translate(r["battle_royale"]["current"]["map"], "Map"),
                BattleRoyal_Current_Image=r["battle_royale"]["current"]["asset"],
                BattleRoyal_Current_Start_Time=r["battle_royale"]["current"]["start"],
                BattleRoyal_Current_Start_Time_datetime=r["battle_royale"]["current"]["readableDate_start"],
                BattleRoyal_Current_End_Time=r["battle_royale"]["current"]["end"],
                BattleRoyal_Current_End_Time_datetime=r["battle_royale"]["current"]["readableDate_end"],
                BattleRoyal_Current_remainingTimer=r["battle_royale"]["current"]["remainingTimer"],
                BattleRoyal_Next_Map=translate(r["battle_royale"]["next"]["map"], "Map"),
                BattleRoyal_Next_Start_Time=r["battle_royale"]["next"]["start"],
                BattleRoyal_Next_End_Time=r["battle_royale"]["next"]["end"],
                BattleRoyal_Next_Start_Time_datetime=r["battle_royale"]["next"]["readableDate_start"],
                BattleRoyal_Next_End_Time_datetime=r["battle_royale"]["next"]["readableDate_end"],
                Arena_Current_Map=translate(r["arenas"]["current"]["map"], "Map"),
                Arena_Current_Image=r["arenas"]["current"]["asset"],
                Arena_Current_Start_Time=r["arenas"]["current"]["start"],
                Arena_Current_Start_Time_datetime=r["arenas"]["current"]["readableDate_start"],
                Arena_Current_End_Time=r["arenas"]["current"]["end"],
                Arena_Current_End_Time_datetime=r["arenas"]["current"]["readableDate_end"],
                Arena_Current_remainingTimer=r["arenas"]["current"]["remainingTimer"],
                Arena_Next_Map=translate(r["arenas"]["next"]["map"], "Map"),
                Arena_Next_Start_Time=r["arenas"]["next"]["start"],
                Arena_Next_End_Time=r["arenas"]["next"]["end"],
                Arena_Next_Start_Time_datetime=r["arenas"]["next"]["readableDate_start"],
                Arena_Next_End_Time_datetime=r["arenas"]["next"]["readableDate_end"],
                Ranked_Current_Map=translate(r["ranked"]["current"]["map"], "Map"),
                Ranked_Current_Image=r["ranked"]["current"]["asset"],
                Ranked_next_Map=translate(r["ranked"]["next"]["map"], "Map"),
                ArenaRanked_Current_Map=translate(r["arenasRanked"]["current"]["map"], "Map"),
                ArenaRanked_Current_Image=r["arenasRanked"]["current"]["asset"],
                ArenaRanked_Current_Start_Time=r["arenasRanked"]["current"]["start"],
                ArenaRanked_Current_End_Time=r["arenasRanked"]["current"]["end"],
                ArenaRanked_Current_Start_Time_datetime=r["arenasRanked"]["current"]["readableDate_start"],
                ArenaRanked_Current_End_Time_datetime=r["arenasRanked"]["current"]["readableDate_end"],
                ArenaRanked_Current_remainingTimer=r["arenasRanked"]["current"]["remainingTimer"],
                ArenaRanked_Next_Map=translate(r["arenasRanked"]["next"]["map"], "Map"),
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
        res = get_request(url, {'Authorization': api_key})
        response = res[0]
        if response.status_code == 200:
            res = ApexTrackerPy.Apexclass.A_News(
                row_json=response.json(),
                elapsed_time=res[1]
            )
            return res
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
        res = get_request(url, {'Authorization': api_key})
        response = res[0]
        if response.status_code == 200:
            r = response.json()
            res = ApexTrackerPy.Apexclass.A_Server_Data(
                row_json=r,
                elapsed_time=res[1],
                Origin_login_EU_West=r["Origin_login"]["EU-West"],
                Origin_login_EU_East=r["Origin_login"]["EU-East"],
                Origin_login_US_West=r["Origin_login"]["US-West"],
                Origin_login_US_East=r["Origin_login"]["US-East"],
                Origin_login_US_Central=r["Origin_login"]["US-Central"],
                Origin_login_Asia=r["Origin_login"]["Asia"],
                Origin_login_SouthAmerica=r["Origin_login"]["SouthAmerica"],

                EA_novafusion_EU_West=r["EA_novafusion"]["EU-West"],
                EA_novafusion_EU_East=r["EA_novafusion"]["EU-East"],
                EA_novafusion_US_West=r["EA_novafusion"]["US-West"],
                EA_novafusion_US_East=r["EA_novafusion"]["US-East"],
                EA_novafusion_US_Central=r["EA_novafusion"]["US-Central"],
                EA_novafusion_Asia=r["EA_novafusion"]["Asia"],
                EA_novafusion_SouthAmerica=r["EA_novafusion"]["SouthAmerica"],

                EA_accounts_EU_West=r["EA_accounts"]["EU-West"],
                EA_accounts_EU_East=r["EA_accounts"]["EU-East"],
                EA_accounts_US_West=r["EA_accounts"]["US-West"],
                EA_accounts_US_East=r["EA_accounts"]["US-East"],
                EA_accounts_US_Central=r["EA_accounts"]["US-Central"],
                EA_accounts_Asia=r["EA_accounts"]["Asia"],
                EA_accounts_SouthAmerica=r["EA_accounts"]["SouthAmerica"],

                ApexOauth_Crossplay_EU_West=r["ApexOauth_Crossplay"]["EU-West"],
                ApexOauth_Crossplay_EU_East=r["ApexOauth_Crossplay"]["EU-East"],
                ApexOauth_Crossplay_US_West=r["ApexOauth_Crossplay"]["US-West"],
                ApexOauth_Crossplay_US_East=r["ApexOauth_Crossplay"]["US-East"],
                ApexOauth_Crossplay_US_Central=r["ApexOauth_Crossplay"]["US-Central"],
                ApexOauth_Crossplay_Asia=r["ApexOauth_Crossplay"]["Asia"],
                ApexOauth_Crossplay_SouthAmerica=r["ApexOauth_Crossplay"]["SouthAmerica"],

                CSServer_Playstation_Network=r["otherPlatforms"]["Playstation-Network"],
                CSServer_Xbox_Live=r["otherPlatforms"]["Xbox-Live"],

            )
            return res
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
        res = get_request(url, {'Authorization': api_key})
        response = res[0]
        if response.status_code == 200 or response.status_code == 500:
            # 何故か現状500が返ってくる
            r = response.json()
            res = ApexTrackerPy.Apexclass.A_Origin_API(
                row_json=r,
                elapsed_time=res[1],
                name=r["name"],
                uid=r["uid"],
                pid=r["pid"],
                avater=r["avatar"]
            )
            return res
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
    platform = _fixplatform(platform)
    
    if _checkplatform(platform):
        url = f'https://api.mozambiquehe.re/nametouid?player={PlayerName}&platform={platform}'
        try:
            res = get_request(url, {'Authorization': api_key})
            response = res[0]
            if response.status_code == 200:
                r = response.json()
                res = ApexTrackerPy.Apexclass.A_Origin_API(
                    row_json=r,
                    elapsed_time=res[1],
                    name=r["name"],
                    uid=r["uid"],
                    pid=r["pid"],
                    avater=r["avatar"]
                )
                return res
            else:
                raise Exception('HttpError!:The API returned status code '+str(response.status_code))
        except Exception as e:
            raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))
    else:
        raise Exception('Invalid platform!')