# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

#Class for Apex Legends API data
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
