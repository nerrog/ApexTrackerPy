# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

# Class for Apex Legends API data

# PlayerData
class A_Player_Data:
    def __init__(self, row_json,
    name, uid, avatar_url, level, Isban, Rank_RP, CurrentRank, Arena_Rank_RP, Arena_Current_Rank, battlepass_level, badges_json, 
    Player_status, legends_json, total_kill, total_damage):
        self.row_json = row_json
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
        self.badges_json = badges_json
        self.Player_status = Player_status
        self.legends_json = legends_json
        self.total_kill = total_kill
        self.total_damage = total_damage

# MapRotationData
class A_Map_Rotation():
    def __init__(self, row_json,
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