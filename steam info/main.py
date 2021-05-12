import requests
import json

API_KEY = '9B6AEF864268499EBCF6EB27474219B9'
STEAM_ID = 76561198097056975

# # 获取用户数据
# URL_PLAYER_SUMMARIES = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}'
# res0 = requests.get(URL_PLAYER_SUMMARIES).content
# res0 = json.loads(res0)
# res1 = res0['response']['players'][0]   # 得到了一个dict，里面的key都写在下面了
# # keys = res1.keys()
# # steamid
# # communityvisibilitystate
# # profilestate
# # personaname
# # commentpermission
# # profileurl
# # avatar
# # avatarmedium
# # avatarfull
# # avatarhash
# # lastlogoff
# # personastate
# # primaryclanid
# # timecreated
# # personastateflags


# # 查询某用户某APP成就
# APP_ID = 440    # 你要查询的游戏ID
# URL_PLAYER_ACHIEVEMENTS = f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={APP_ID}&key={API_KEY}&steamid={STEAM_ID}'
# res0 = requests.get(URL_PLAYER_ACHIEVEMENTS).content
# res0 = json.loads(res0)['playerstats']
# # print(res0)
# steamID = res0['steamID']
# gameName = res0['gameName']
# achievements = res0['achievements'] # dicts in list, keys ['apiname', 'achieved', 'unlocktime']
# success = res0['success']



# # 好像没啥用
# APP_ID = 440    # 你要查询的游戏ID
# URL_GAME_ACHIEVEMENTS = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={APP_ID}&key={API_KEY}&steamid={STEAM_ID}'
# res0 = requests.get(URL_GAME_ACHIEVEMENTS).content
# res0 = json.loads(res0)


# 查询玩家游戏时长
URL_PLAYER_GAME = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=true'
res0 = requests.get(URL_PLAYER_GAME).content
res0 = json.loads(res0)['response']
game_count = res0['game_count']
games = res0['games']   # dicts in list, keys ['appid', 'name', 'playtime_2weeks', 'playtime_forever', 'img_icon_url', 'img_logo_url']   游戏时间单位分钟, 剩下一些都没用
# 游戏信息
appid = res0['games'][0]['appid']
name = res0['games'][0]['name']
icon_hash = res0['games'][0]['img_icon_url']
logo_hash = res0['games'][0]['img_logo_url']
icon_url = f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{icon_hash}.jpg'
logo_url = f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{logo_hash}.jpg'