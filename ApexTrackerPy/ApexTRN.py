# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import ApexTrackerPy.Apexclass
from ApexTrackerPy.get_requests import get_request

API_VER = 'v2'

def _checkplatform(platform):
    """
    Check if the platform is valid.
    :param platform: The platform to check.
    """
    if platform == 'origin' or platform == 'psn' or platform == 'xbl':
        return True
    else:
        return False

def _fixplatform(p):
    """
    Fix the platform.
    :param platform: The platform to fix.
    """
    if p == 'pc' or p == 'PC' or p == 'ORIGIN':
        return 'origin'
    elif p == 'ps4' or p == 'PSN' or p == 'PS5' or p == 'ps5':
        return 'psn'
    elif p == 'x1' or p == 'xbox' or p == 'XBOX' or p == 'XBOX1' or p == 'XBL':
        return 'xbl'
    else:
        return p

def GetApexPlayerStatus_TRN(api_key, platform, playerName):
    """
    Get the status of a player on Apex Legends.
    :param api_key: The API key to use.
    :param platform: The platform to use.
    :param playerName: The player name to use.
    """
    platform = _fixplatform(platform)

    if _checkplatform(platform):
        url = f'https://public-api.tracker.gg/{API_VER}/apex/standard/profile/{platform}/{playerName}'
        try:
            res = get_request(url, {'TRN-Api-Key': api_key})
            response = res[0]
            if response.status_code == 200:
                r = response.json()
                
                list_legends_data = []
                my_append = list_legends_data.append

                for d in r['data']['segments']:
                    if d["type"] == "overview":
                        continue
                    else:
                        my_append(d)

                res = ApexTrackerPy.Apexclass.TRN_PlayerStatus(
                    row_json=r,
                    elapsed_time=res[1],
                    platformUserId=r['data']['platformInfo']['platformUserId'],
                    activelegend=r['data']['metadata']['activeLegend'],
                    userlevel=r['data']['segments'][0]['stats']['level']['value'],
                    totalkill=r['data']['segments'][0]['stats']['kills']['value'],
                    totaldamage=r['data']['segments'][0]['stats']['damage']['value'],
                    totalheadshots=r['data']['segments'][0]['stats']['headshots']['value'],
                    CurrentRank=r['data']['segments'][0]['stats']['rankScore']['metadata']['rankName'],
                    CurrentRankScore=r['data']['segments'][0]['stats']['rankScore']['value'],
                    ArenaRankedName=r['data']['segments'][0]['stats']['arenaRankScore']['metadata']['rankName'],
                    ArenaRankedScore=r['data']['segments'][0]['stats']['arenaRankScore']['value'],
                    legends_json=list_legends_data,
                )
                return res
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
    platform = _fixplatform(platform)
    
    if _checkplatform(platform):
        url = f'https://public-api.tracker.gg/{API_VER}/apex/standard/profile/{platform}/{playerName}/sessions'
        try:
            res = get_request(url, {'TRN-Api-Key': api_key})
            response = res[0]
            if response.status_code == 200:
                r = response.json()
                res = ApexTrackerPy.Apexclass.TRN_MatchHistory(
                    row_json=r,
                    elapsed_time=res[1],
                    matches_list=r['data']["items"],
                )
                return res
            else:
                raise Exception('HttpError!:The API returned status code '+str(response.status_code))
        except Exception as e:
            raise Exception('HttpError!:An error has occurred during the API call.\n'+str(e))
    else:
        raise Exception('Invalid platform!')