# import requests
# import os
# import json
#
# game_ids = [4712, 9276, 4653, 5649, 7865, 9300, 11156, 10714, 4713, 9279, 8149, 8976, 7202, 9275, 9930, 9283, 12471,
#             12442, 12922, 7994, 7837, 8048, 9611, 6291, 6504, 1994, 12457, 2660]
# game_photos = {5169: ['https://www.old-games.ru//games/pc/_kkrieger__chapter_i/screenshots/5169_54c4d5bd1b48a.jpg',
#                       'https://www.old-games.ru//games/pc/_kkrieger__chapter_i/screenshots/5169_54c4d52baf4a4.jpg',
#                       'https://www.old-games.ru//games/pc/_kkrieger__chapter_i/screenshots/5169_61f410192ae27.jpg'],
#                2117: ['https://www.old-games.ru//games/pc/007_nightfire/screenshots/2117_54a7e675d6da8.jpg',
#                       'https://www.old-games.ru//games/pc/007_nightfire/screenshots/2117_49ce03ca028fb.jpg',
#                       'https://www.old-games.ru//games/pc/007_nightfire/screenshots/2117_4cb758860d59d.jpg'],
#                12361: ['https://www.old-games.ru//games/pc/007_sonic_secret_agent/screenshots/12361_62ea18f7859ca.png',
#                        'https://www.old-games.ru//games/pc/007_sonic_secret_agent/screenshots/12361_62ea18f783062.png',
#                        'https://www.old-games.ru//games/pc/007_sonic_secret_agent/screenshots/12361_62ea18f7910bc.png'],
#                11619: ['https://www.old-games.ru//games/pc/1_2_3/screenshots/11619_6179a31fc1a77.jpg',
#                        'https://www.old-games.ru//games/pc/1_2_3/screenshots/11619_6179a2c28cadd.jpg',
#                        'https://www.old-games.ru//games/pc/1_2_3/screenshots/11619_6179a2bd1ba2e.jpg'],
#                10324: ['https://www.old-games.ru//games/pc/1_day_a_mosquito/screenshots/10324_606dd0f58d50e.png',
#                        'https://www.old-games.ru//games/pc/1_day_a_mosquito/screenshots/10324_606dd0fc5b370.png',
#                        'https://www.old-games.ru//games/pc/1_day_a_mosquito/screenshots/10324_606dd0fdaae03.png'],
#                9235: ['https://www.old-games.ru//games/pc/10_2/screenshots/9235_5dff6b75b8ff5.jpg',
#                       'https://www.old-games.ru//games/pc/10_2/screenshots/9235_5dff936011437.jpg',
#                       'https://www.old-games.ru//games/pc/10_2/screenshots/9235_5dff6b8fc2a3d.jpg'],
#                12790: ['https://www.old-games.ru//games/pc/1000_ivolga/screenshots/12790_6545d0b01ad75.jpg',
#                        'https://www.old-games.ru//games/pc/1000_ivolga/screenshots/12790_6545d0b01a27c.jpg',
#                        'https://www.old-games.ru//games/pc/1000_ivolga/screenshots/12790_6545d0b01ad28.jpg'],
#                12795: ['https://www.old-games.ru//games/pc/10000/screenshots/12795_635a4d0992319.jpg',
#                        'https://www.old-games.ru//games/pc/10000/screenshots/12795_635a4d1b4119f.jpg',
#                        'https://www.old-games.ru//games/pc/10000/screenshots/12795_635a4d2949c63.jpg'], 2944: [
#         'https://www.old-games.ru//games/pc/101_the_airborne_invasion_of_normandy/screenshots/2944_54bfff26df7c6.jpg',
#         'https://www.old-games.ru//games/pc/101_the_airborne_invasion_of_normandy/screenshots/2944_54bfff3346f60.jpg',
#         'https://www.old-games.ru//games/pc/101_the_airborne_invasion_of_normandy/screenshots/2944_4e10df78c0677.jpg'],
#                8593: [
#                    'https://www.old-games.ru//games/pc/12_stulev_kak_eto_bylo_na_samom_dele/screenshots/8593_5ca0a8f45e901.jpg',
#                    'https://www.old-games.ru//games/pc/12_stulev_kak_eto_bylo_na_samom_dele/screenshots/8593_5ca0a5738bdc6.jpg',
#                    'https://www.old-games.ru//games/pc/12_stulev_kak_eto_bylo_na_samom_dele/screenshots/8593_5ca0a5770d400.jpg'],
#                11408: ['https://www.old-games.ru//games/pc/15_sharov/screenshots/11408_6238af1fba5c4.jpg',
#                        'https://www.old-games.ru//games/pc/15_sharov/screenshots/11408_6238af1d21408.jpg',
#                        'https://www.old-games.ru//games/pc/15_sharov/screenshots/11408_6238af195d0bf.jpg'],
#                12697: ['https://www.old-games.ru//games/pc/15_fifteen/screenshots/12697_634f004114d35.jpg',
#                        'https://www.old-games.ru//games/pc/15_fifteen/screenshots/12697_634f004c2e986.jpg',
#                        'https://www.old-games.ru//games/pc/15_fifteen/screenshots/12697_634f00461bdaa.jpg'],
#                328: ['https://www.old-games.ru//games/pc/1602_a_d_/screenshots/328_4a12e29e8449d.jpg',
#                      'https://www.old-games.ru//games/pc/1602_a_d_/screenshots/328_4a12e29f95460.jpg',
#                      'https://www.old-games.ru//games/pc/1602_a_d_/screenshots/328_4a12e29ec1202.jpg'], 12455: [
#         'https://www.old-games.ru//games/pc/18_wheels_of_steel_across_america/screenshots/12455_6297abe2c0657.jpg',
#         'https://www.old-games.ru//games/pc/18_wheels_of_steel_across_america/screenshots/12455_6297abd9efcc0.jpg',
#         'https://www.old-games.ru//games/pc/18_wheels_of_steel_across_america/screenshots/12455_6297abcbd78ae.jpg'],
#                12579: [
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_convoy/screenshots/12579_62e15f55381b7.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_convoy/screenshots/12579_62e15f5d20e92.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_convoy/screenshots/12579_62e15f6a956f4.jpg'],
#                12585: [
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_haulin/screenshots/12585_62efcd75aa631.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_haulin/screenshots/12585_62efcf6208c44.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_haulin/screenshots/12585_62efcf7ea4df3.jpg'],
#                12522: [
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_pedal_to_the_metal/screenshots/12522_62e7662780d5a.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_pedal_to_the_metal/screenshots/12522_62e7662c97327.jpg',
#                    'https://www.old-games.ru//games/pc/18_wheels_of_steel_pedal_to_the_metal/screenshots/12522_62e76614370e8.jpg'],
#                12781: ['https://www.old-games.ru//games/pc/1945/screenshots/12781_6358e299bf5da.jpg',
#                        'https://www.old-games.ru//games/pc/1945/screenshots/12781_6358e2b27888e.jpg',
#                        'https://www.old-games.ru//games/pc/1945/screenshots/12781_6358e29ee25ee.jpg'],
#                12818: ['https://www.old-games.ru//games/pc/1968/screenshots/12818_635971c7d99c1.jpg',
#                        'https://www.old-games.ru//games/pc/1968/screenshots/12818_635a4832398a9.jpg',
#                        'https://www.old-games.ru//games/pc/1968/screenshots/12818_635a482767800.jpg'],
#                10942: ['https://www.old-games.ru//games/pc/1995_toyota_interactive/screenshots/10942_6027553cd49e5.png',
#                        'https://www.old-games.ru//games/pc/1995_toyota_interactive/screenshots/10942_60275458dfdc9.png',
#                        'https://www.old-games.ru//games/pc/1995_toyota_interactive/screenshots/10942_6027554ab696f.png'],
#                9052: [
#                    'https://www.old-games.ru//games/pc/20_000_leagues_the_adventure_continues/screenshots/9052_5db58ae5c37ed.png',
#                    'https://www.old-games.ru//games/pc/20_000_leagues_the_adventure_continues/screenshots/9052_5db58aa59651e.png',
#                    'https://www.old-games.ru//games/pc/20_000_leagues_the_adventure_continues/screenshots/9052_5db58ae5d73ae.png'],
#                9965: ['https://www.old-games.ru//games/pc/20_000_leghe_sotto_i_mari/screenshots/9965_5f74b4b89262a.jpg',
#                       'https://www.old-games.ru//games/pc/20_000_leghe_sotto_i_mari/screenshots/9965_5f0358b86be8c.png',
#                       'https://www.old-games.ru//games/pc/20_000_leghe_sotto_i_mari/screenshots/9965_5f0358a61fe4d.png'],
#                10055: ['https://www.old-games.ru//games/pc/2002_fifa_world_cup/screenshots/10055_5f3b8517efbda.png',
#                        'https://www.old-games.ru//games/pc/2002_fifa_world_cup/screenshots/10055_5f3b851e3c049.png',
#                        'https://www.old-games.ru//games/pc/2002_fifa_world_cup/screenshots/10055_5f3b84bdb614e.png'],
#                12558: ['https://www.old-games.ru//games/pc/202_jogos/screenshots/12558_62d02f5eb3015.jpg',
#                        'https://www.old-games.ru//games/pc/202_jogos/screenshots/12558_62d02f5f739ca.jpg',
#                        'https://www.old-games.ru//games/pc/202_jogos/screenshots/12558_62d02ed7aff6b.jpg'],
#                12786: ['https://www.old-games.ru//games/pc/21_min/screenshots/12786_65472e82bd8a2.jpg',
#                        'https://www.old-games.ru//games/pc/21_min/screenshots/12786_65472e82bdc3f.jpg',
#                        'https://www.old-games.ru//games/pc/21_min/screenshots/12786_65472e82b854b.jpg'], 10465: [
#         'https://www.old-games.ru//games/pc/21st_century_of_suchi_puzzle/screenshots/10465_5fc3a44b6ae7b.png',
#         'https://www.old-games.ru//games/pc/21st_century_of_suchi_puzzle/screenshots/10465_5fc3a44b1b23a.png',
#         'https://www.old-games.ru//games/pc/21st_century_of_suchi_puzzle/screenshots/10465_5fc3a4315fc8b.png'],
#                12787: ['https://www.old-games.ru//games/pc/2261/screenshots/12787_640a33af330d8.png',
#                        'https://www.old-games.ru//games/pc/2261/screenshots/12787_640a33af4fc26.png',
#                        'https://www.old-games.ru//games/pc/2261/screenshots/12787_640a33af531ef.png'], 10896: [
#         'https://www.old-games.ru//games/pc/25_ans!_le_cd-rom_de_fluide_glacial/screenshots/10896_61efbf2dc3c31.png',
#         'https://www.old-games.ru//games/pc/25_ans!_le_cd-rom_de_fluide_glacial/screenshots/10896_61efbeffe2501.png',
#         'https://www.old-games.ru//games/pc/25_ans!_le_cd-rom_de_fluide_glacial/screenshots/10896_61efbf2f6e128.png'],
#                6627: [
#                    'https://www.old-games.ru//games/pc/3__2__1_smurf!_my_first_racing_game/screenshots/6627_5776759f181cc.jpg',
#                    'https://www.old-games.ru//games/pc/3__2__1_smurf!_my_first_racing_game/screenshots/6627_5776759827bc7.jpg',
#                    'https://www.old-games.ru//games/pc/3__2__1_smurf!_my_first_racing_game/screenshots/6627_5776758649882.jpg'],
#                5417: ['https://www.old-games.ru//games/pc/3-d_frog_man/screenshots/5417_5ff7971a4229b.png',
#                       'https://www.old-games.ru//games/pc/3-d_frog_man/screenshots/5417_5ff796fac6444.png',
#                       'https://www.old-games.ru//games/pc/3-d_frog_man/screenshots/5417_5ff7973ca2be4.png'],
#                8288: ['https://www.old-games.ru//games/pc/3-d_ultra_cool_pool/screenshots/8288_5bfe26e686962.png',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_cool_pool/screenshots/8288_5bfe266a5ec20.png',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_cool_pool/screenshots/8288_5bfe26f351c35.png'],
#                5997: ['https://www.old-games.ru//games/pc/3-d_ultra_minigolf_deluxe/screenshots/5997_5651c0a3d69d0.jpg',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_minigolf_deluxe/screenshots/5997_5651c0c54c7dc.jpg',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_minigolf_deluxe/screenshots/5997_5651c0beae5d2.jpg'],
#                5988: ['https://www.old-games.ru//games/pc/3-d_ultra_nascar_pinball/screenshots/5988_5653533c577bb.jpg',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_nascar_pinball/screenshots/5988_5653533f98bd9.jpg',
#                       'https://www.old-games.ru//games/pc/3-d_ultra_nascar_pinball/screenshots/5988_5653533b3e5e3.jpg'],
#                5166: [
#                    'https://www.old-games.ru//games/pc/3d_ultra_pinball_creep_night/screenshots/5166_54c51d2aa663a.png',
#                    'https://www.old-games.ru//games/pc/3d_ultra_pinball_creep_night/screenshots/5166_54c51d262ec21.png',
#                    'https://www.old-games.ru//games/pc/3d_ultra_pinball_creep_night/screenshots/5166_54c51d2ed7f85.png'],
#                8387: [
#                    'https://www.old-games.ru//games/pc/3-d_ultra_pinball_thrillride/screenshots/8387_5c1f957edfc39.png',
#                    'https://www.old-games.ru//games/pc/3-d_ultra_pinball_thrillride/screenshots/8387_5c1f9581b2d92.png',
#                    'https://www.old-games.ru//games/pc/3-d_ultra_pinball_thrillride/screenshots/8387_5c1f957f68b94.png'],
#                1401: [
#                    'https://www.old-games.ru//games/pc/3-d_ultra_radio_control_racers/screenshots/1401_4a182b8cc3af5.jpg',
#                    'https://www.old-games.ru//games/pc/3-d_ultra_radio_control_racers/screenshots/1401_4a182b8da3b3e.jpg',
#                    'https://www.old-games.ru//games/pc/3-d_ultra_radio_control_racers/screenshots/1401_4a182b8c2e451.jpg'],
#                12768: ['https://www.old-games.ru//games/pc/3-ij_srok/screenshots/12768_63562e0f4c365.jpg',
#                        'https://www.old-games.ru//games/pc/3-ij_srok/screenshots/12768_6356b6e5dc160.jpg',
#                        'https://www.old-games.ru//games/pc/3-ij_srok/screenshots/12768_63557bad5b41c.jpg'],
#                11695: ['https://www.old-games.ru//games/pc/360/screenshots/11695_61e526dd57cfc.png',
#                        'https://www.old-games.ru//games/pc/360/screenshots/11695_61e526dd78bf8.png',
#                        'https://www.old-games.ru//games/pc/360/screenshots/11695_61e526dd6e2d5.png'], 9976: [
#         'https://www.old-games.ru//games/pc/3d_adventures_of_sailor_moon__the/screenshots/9976_5f07e1dd70ae2.png',
#         'https://www.old-games.ru//games/pc/3d_adventures_of_sailor_moon__the/screenshots/9976_5f07e28ddb38b.png',
#         'https://www.old-games.ru//games/pc/3d_adventures_of_sailor_moon__the/screenshots/9976_5f07e30947040.png'],
#                9277: ['https://www.old-games.ru//games/pc/3d_alien_invasion/screenshots/9277_5e0bd216b530e.png',
#                       'https://www.old-games.ru//games/pc/3d_alien_invasion/screenshots/9277_5e0bd2160b0db.png',
#                       'https://www.old-games.ru//games/pc/3d_alien_invasion/screenshots/9277_5e0bd215e4687.png'],
#                4492: ['https://www.old-games.ru//games/pc/3d_astro_blaster/screenshots/4492_54d255f6e220a.jpg',
#                       'https://www.old-games.ru//games/pc/3d_astro_blaster/screenshots/4492_50eeb3cb59b54.jpg',
#                       'https://www.old-games.ru//games/pc/3d_astro_blaster/screenshots/4492_50eeb3cb5167a.jpg'],
#                9278: ['https://www.old-games.ru//games/pc/3d_block_bustin_madness/screenshots/9278_5e0bd24f8da88.png',
#                       'https://www.old-games.ru//games/pc/3d_block_bustin_madness/screenshots/9278_5e0bd24f854d7.png',
#                       'https://www.old-games.ru//games/pc/3d_block_bustin_madness/screenshots/9278_5e0bd24f9b093.png'],
#                6601: ['https://www.old-games.ru//games/pc/3d_bowling_usa/screenshots/6601_57583516a16aa.jpg',
#                       'https://www.old-games.ru//games/pc/3d_bowling_usa/screenshots/6601_575834f79b46f.jpg',
#                       'https://www.old-games.ru//games/pc/3d_bowling_usa/screenshots/6601_57583517c9eaa.jpg'],
#                8701: ['https://www.old-games.ru//games/pc/3d_bubble_burst/screenshots/8701_5cc344c6d853e.png',
#                       'https://www.old-games.ru//games/pc/3d_bubble_burst/screenshots/8701_5cc344c6dbc78.png',
#                       'https://www.old-games.ru//games/pc/3d_bubble_burst/screenshots/8701_5cc344c6dcb43.png'],
#                9280: ['https://www.old-games.ru//games/pc/3d_bug_attack/screenshots/9280_5e0bd26de4794.png',
#                       'https://www.old-games.ru//games/pc/3d_bug_attack/screenshots/9280_5e0bd26dd6ef7.png',
#                       'https://www.old-games.ru//games/pc/3d_bug_attack/screenshots/9280_5e0bd26de67ce.png'],
#                9298: ['https://www.old-games.ru//games/pc/3d_checkers/screenshots/9298_5e12732612212.png',
#                       'https://www.old-games.ru//games/pc/3d_checkers/screenshots/9298_5e1273261224c.png',
#                       'https://www.old-games.ru//games/pc/3d_checkers/screenshots/9298_5e1273261a7ad.png'],
#                9297: ['https://www.old-games.ru//games/pc/3d_chess/screenshots/9297_5e12735930bb9.png',
#                       'https://www.old-games.ru//games/pc/3d_chess/screenshots/9297_5e1273592ab96.png'],
#                9299: ['https://www.old-games.ru//games/pc/3d_chinese_chess/screenshots/9299_5e12b1026f414.png',
#                       'https://www.old-games.ru//games/pc/3d_chinese_chess/screenshots/9299_5e12b120e6627.png',
#                       'https://www.old-games.ru//games/pc/3d_chinese_chess/screenshots/9299_5e12b12ed751b.png'],
#                4697: ['game_id=12649'],
#                9292: ['https://www.old-games.ru//games/pc/3d_cubix/screenshots/9292_5e114ca7e7bb6.png',
#                       'https://www.old-games.ru//games/pc/3d_cubix/screenshots/9292_5e114cb91e912.png',
#                       'https://www.old-games.ru//games/pc/3d_cubix/screenshots/9292_5e114cbb1a240.png']}
#
# path = os.path.dirname(__file__) + os.sep + 'screenshots'
# if os.path.exists(path):
#     print(f"[INFO] Path already exists.")
# else:
#     os.mkdir(path)
#     print(f"[INFO] Path created.")
#
# while len(game_photos) != 0:
#     game_set = game_photos.popitem()
#     game_ids = game_set[0]
#     game_urls = game_set[1]
#     counter = 1
#     for url in game_urls:
#         url_num = url.find('game_id=')
#         if url_num != -1:
#             game_id = int(url[url_num + len('game_id='):])
#             response = requests.get(f'https://www.old-games.ru/game/{game_id}.html')
#             s = f"URL: https://www.old-games.ru/game/{game_id}.html\n\n\n{response.text}"
#             with open(path + os.sep + str(game_id) + '.txt', "w") as file:
#                 file.writelines(s)
#                 print(f"[INFO] File {str(game_id) + '.txt'} has been saved.")
#         else:
#             resolution = url[url.rfind('.'):]
#             filename = str(game_ids) + '_' + str(counter) + resolution
#             with open(path + os.sep + filename, "wb") as file:
#                 file.write(requests.get(url).content)
#                 print(f"[INFO] File {filename} has been downloaded and saved.")
#         counter += 1
# print(f"[INFO] Games images saved.")
