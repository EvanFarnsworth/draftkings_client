from draft_kings_client.draft_kings_client import DraftKingsClient, Sport

contests = DraftKingsClient.get_contests(sport=Sport.nhl)

i = 0
for contest in contests.draft_groups:
    players = DraftKingsClient.get_available_players(contest.id)
    print(players)
    for player in players.player_list:
        if player.draftkings_points_per_game > 1.0:
            print(player)

