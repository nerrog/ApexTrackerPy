# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

# Class for Apex Legends API data

# PlayerData
class A_Player_Data:
    def __init__(self, row_json, elapsed_time,
    name, uid, avatar_url, level, Isban, Rank_RP, CurrentRank, Arena_Rank_RP, Arena_Current_Rank, battlepass_level, battlepass_history_list, badges_json, 
    Player_status, legends_json, total_kill, total_damage, lobbyState, IsOnline, IsInGame,
    canJoin, PartyFull, Selected_legend, CurrentState):
        self.row_json = row_json
        self.elapsed_time = elapsed_time
        self.name = name
        self.uid = uid
        self.avatar_url = avatar_url
        self.level = level
        self.Isban = Isban
        self.Rank_RP = Rank_RP
        self.CurrentRank = CurrentRank
        self.Arena_Rank_RP = Arena_Rank_RP
        self.Arena_Current_Rank = Arena_Current_Rank
        self.battlepass_level = battlepass_level
        self.battlepass_history_list = battlepass_history_list
        self.badges_json = badges_json
        self.Player_status = Player_status
        self.legends_json = legends_json
        self.total_kill = total_kill
        self.total_damage = total_damage
        #v1.8
        self.lobbyState = lobbyState
        self.IsOnline = IsOnline
        self.IsInGame = IsInGame
        self.canJoin = canJoin
        self.PartyFull = PartyFull
        self.Selected_legend = Selected_legend
        self.CurrentState = CurrentState



# MapRotationData
class A_Map_Rotation():
    def __init__(self, row_json, elapsed_time,
    #バトロワ(Current)
    BattleRoyal_Current_Map, BattleRoyal_Current_Image, BattleRoyal_Current_Start_Time, BattleRoyal_Current_End_Time,
    BattleRoyal_Current_Start_Time_datetime, BattleRoyal_Current_End_Time_datetime,BattleRoyal_Current_remainingTimer,
    #バトロワ(Next)
    BattleRoyal_Next_Map, BattleRoyal_Next_Start_Time, BattleRoyal_Next_End_Time,
    BattleRoyal_Next_Start_Time_datetime, BattleRoyal_Next_End_Time_datetime,
    #アリーナ(Current)
    Arena_Current_Map, Arena_Current_Image, Arena_Current_Start_Time, Arena_Current_End_Time,
    Arena_Current_Start_Time_datetime, Arena_Current_End_Time_datetime, Arena_Current_remainingTimer,
    #アリーナ(Next)
    Arena_Next_Map, Arena_Next_Start_Time, Arena_Next_End_Time,Arena_Next_Start_Time_datetime, Arena_Next_End_Time_datetime,
    #Ranked(Current, Next)
    Ranked_Current_Map, Ranked_Current_Image, Ranked_next_Map,
    #アリーナランク(Current)
    ArenaRanked_Current_Map, ArenaRanked_Current_Image, ArenaRanked_Current_Start_Time, ArenaRanked_Current_End_Time,
    ArenaRanked_Current_Start_Time_datetime, ArenaRanked_Current_End_Time_datetime, ArenaRanked_Current_remainingTimer,
    #アリーナランク(Next)
    ArenaRanked_Next_Map, ArenaRanked_Next_Start_Time, ArenaRanked_Next_End_Time,
    ArenaRanked_Next_Start_Time_datetime, ArenaRanked_Next_End_Time_datetime):
        self.row_json = row_json
        self.elapsed_time = elapsed_time
        self.BattleRoyal_Current_Map = BattleRoyal_Current_Map
        self.BattleRoyal_Current_Image = BattleRoyal_Current_Image
        self.BattleRoyal_Current_Start_Time = BattleRoyal_Current_Start_Time
        self.BattleRoyal_Current_End_Time = BattleRoyal_Current_End_Time
        self.BattleRoyal_Current_Start_Time_datetime = BattleRoyal_Current_Start_Time_datetime
        self.BattleRoyal_Current_End_Time_datetime = BattleRoyal_Current_End_Time_datetime
        self.BattleRoyal_Current_remainingTimer = BattleRoyal_Current_remainingTimer
        self.BattleRoyal_Next_Map = BattleRoyal_Next_Map
        self.BattleRoyal_Next_Start_Time = BattleRoyal_Next_Start_Time
        self.BattleRoyal_Next_End_Time = BattleRoyal_Next_End_Time
        self.BattleRoyal_Next_Start_Time_datetime = BattleRoyal_Next_Start_Time_datetime
        self.BattleRoyal_Next_End_Time_datetime = BattleRoyal_Next_End_Time_datetime
        self.Arena_Current_Map = Arena_Current_Map
        self.Arena_Current_Image = Arena_Current_Image
        self.Arena_Current_Start_Time = Arena_Current_Start_Time
        self.Arena_Current_End_Time = Arena_Current_End_Time
        self.Arena_Current_Start_Time_datetime = Arena_Current_Start_Time_datetime
        self.Arena_Current_End_Time_datetime = Arena_Current_End_Time_datetime
        self.Arena_Current_remainingTimer = Arena_Current_remainingTimer
        self.Arena_Next_Map = Arena_Next_Map
        self.Arena_Next_Start_Time = Arena_Next_Start_Time
        self.Arena_Next_End_Time = Arena_Next_End_Time
        self.Arena_Next_Start_Time_datetime = Arena_Next_Start_Time_datetime
        self.Arena_Next_End_Time_datetime = Arena_Next_End_Time_datetime
        self.Ranked_Current_Map = Ranked_Current_Map
        self.Ranked_Current_Image = Ranked_Current_Image
        self.Ranked_next_Map = Ranked_next_Map
        self.ArenaRanked_Current_Map = ArenaRanked_Current_Map
        self.ArenaRanked_Current_Image = ArenaRanked_Current_Image
        self.ArenaRanked_Current_Start_Time = ArenaRanked_Current_Start_Time
        self.ArenaRanked_Current_End_Time = ArenaRanked_Current_End_Time
        self.ArenaRanked_Current_Start_Time_datetime = ArenaRanked_Current_Start_Time_datetime
        self.ArenaRanked_Current_End_Time_datetime = ArenaRanked_Current_End_Time_datetime
        self.ArenaRanked_Current_remainingTimer = ArenaRanked_Current_remainingTimer
        self.ArenaRanked_Next_Map = ArenaRanked_Next_Map
        self.ArenaRanked_Next_Start_Time = ArenaRanked_Next_Start_Time
        self.ArenaRanked_Next_End_Time = ArenaRanked_Next_End_Time
        self.ArenaRanked_Next_Start_Time_datetime = ArenaRanked_Next_Start_Time_datetime
        self.ArenaRanked_Next_End_Time_datetime = ArenaRanked_Next_End_Time_datetime


# NewsData (return json only)
class A_News():
    def __init__(self, row_json, elapsed_time):
        self.row_json = row_json
        self.elapsed_time = elapsed_time

# Server Data Class
class Origin_login():
    EU_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    EU_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_Central = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    SouthAmerica = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    Asia = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}

class EA_novafusion():
    EU_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    EU_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_Central = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    SouthAmerica = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    Asia = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}

class EA_accounts():
    EU_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    EU_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_Central = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    SouthAmerica = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    Asia = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}

class ApexOauth_Crossplay():
    EU_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    EU_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_West = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_Central = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    US_East = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    SouthAmerica = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}
    Asia = {'Status': 'UNKNOWN', 'HTTPCode': 0, "ResponseTime": 0}

class CSServer():
    Playstation_Network = {'Status': 'UNKNOWN'}
    Xbox_Live = {'Status': 'UNKNOWN'}


# ServerData (return list)
class A_Server_Data(Origin_login, EA_novafusion, EA_accounts, ApexOauth_Crossplay, CSServer):

    def __init__(self, row_json, elapsed_time,
    Origin_login_EU_West, Origin_login_EU_East, Origin_login_US_West, Origin_login_US_Central, Origin_login_US_East, Origin_login_SouthAmerica, Origin_login_Asia,
    EA_novafusion_EU_West, EA_novafusion_EU_East, EA_novafusion_US_West, EA_novafusion_US_Central, EA_novafusion_US_East, EA_novafusion_SouthAmerica, EA_novafusion_Asia,
    EA_accounts_EU_West, EA_accounts_EU_East, EA_accounts_US_West, EA_accounts_US_Central, EA_accounts_US_East, EA_accounts_SouthAmerica, EA_accounts_Asia,
    ApexOauth_Crossplay_EU_West, ApexOauth_Crossplay_EU_East, ApexOauth_Crossplay_US_West, ApexOauth_Crossplay_US_Central, ApexOauth_Crossplay_US_East, ApexOauth_Crossplay_SouthAmerica, ApexOauth_Crossplay_Asia,
    CSServer_Playstation_Network, CSServer_Xbox_Live):

        self.row_json = row_json
        self.elapsed_time = elapsed_time

        Origin_login.EU_West = Origin_login_EU_West
        Origin_login.EU_East = Origin_login_EU_East
        Origin_login.US_West = Origin_login_US_West
        Origin_login.US_Central = Origin_login_US_Central
        Origin_login.US_East = Origin_login_US_East
        Origin_login.SouthAmerica = Origin_login_SouthAmerica
        Origin_login.Asia = Origin_login_Asia

        EA_novafusion.EU_West = EA_novafusion_EU_West
        EA_novafusion.EU_East = EA_novafusion_EU_East
        EA_novafusion.US_West = EA_novafusion_US_West
        EA_novafusion.US_Central = EA_novafusion_US_Central
        EA_novafusion.US_East = EA_novafusion_US_East
        EA_novafusion.SouthAmerica = EA_novafusion_SouthAmerica
        EA_novafusion.Asia = EA_novafusion_Asia

        EA_accounts.EU_West = EA_accounts_EU_West
        EA_accounts.EU_East = EA_accounts_EU_East
        EA_accounts.US_West = EA_accounts_US_West
        EA_accounts.US_Central = EA_accounts_US_Central
        EA_accounts.US_East = EA_accounts_US_East
        EA_accounts.SouthAmerica = EA_accounts_SouthAmerica
        EA_accounts.Asia = EA_accounts_Asia

        ApexOauth_Crossplay.EU_West = ApexOauth_Crossplay_EU_West
        ApexOauth_Crossplay.EU_East = ApexOauth_Crossplay_EU_East
        ApexOauth_Crossplay.US_West = ApexOauth_Crossplay_US_West
        ApexOauth_Crossplay.US_Central = ApexOauth_Crossplay_US_Central
        ApexOauth_Crossplay.US_East = ApexOauth_Crossplay_US_East
        ApexOauth_Crossplay.SouthAmerica = ApexOauth_Crossplay_SouthAmerica
        ApexOauth_Crossplay.Asia = ApexOauth_Crossplay_Asia

        CSServer.Playstation_Network = CSServer_Playstation_Network
        CSServer.Xbox_Live = CSServer_Xbox_Live


    def Origin_login(self, region):
        try:
            res = Origin_login.__dict__[region]
        except:
            raise Exception("Region not found")

        return res

    def EA_novafusion(self, region):
        try:
            res = EA_novafusion.__dict__[region]
        except:
            raise Exception("Region not found")

        return res

    def EA_accounts(self, region):
        try:
            res = EA_accounts.__dict__[region]
        except:
            raise Exception("Region not found")

        return res

    def ApexOauth_Crossplay(self, region):
        try:
            res = ApexOauth_Crossplay.__dict__[region]
        except:
            raise Exception("Region not found")

        return res

    def CSServer(self, platform):
        try:
            res = CSServer.__dict__[platform]
        except:
            raise Exception("Platform not found")

        return res

class A_Origin_API():
    # name to uidと共用
    def __init__(self, row_json, elapsed_time,
     name, uid, pid, avater):
        self.row_json = row_json
        self.elapsed_time = elapsed_time
        self.name = name
        self.uid = uid
        self.pid = pid
        self.avater = avater

# Class for Tracker Network Data

class TRN_PlayerStatus():

    def __init__(self, row_json, elapsed_time,
    platformUserId, activelegend, userlevel, totalkill, totaldamage, totalheadshots, CurrentRankScore, CurrentRank,
    ArenaRankedScore, ArenaRankedName, legends_json):
        self.row_json = row_json
        self.elapsed_time = elapsed_time
        self.platformUserId = platformUserId
        self.activelegend = activelegend
        self.userlevel = userlevel
        self.totalkill = totalkill
        self.totaldamage = totaldamage
        self.totalheadshots = totalheadshots
        self.CurrentRankScore = CurrentRankScore
        self.CurrentRank = CurrentRank
        self.ArenaRankedScore = ArenaRankedScore
        self.ArenaRankedName = ArenaRankedName
        self.legends_json = legends_json

class TRN_MatchHistory():

    def __init__(self, row_json, elapsed_time,
    matches_list):
        self.row_json = row_json
        self.elapsed_time = elapsed_time
        self.matches_list = matches_list


# Class for Respawn API Data
# coming soon!

class RSPN_Serverlist():
    
        def __init__(self, row_json, elapsed_time,
        server_list):
            self.row_json = row_json
            self.elapsed_time = elapsed_time
            self.server_list = server_list