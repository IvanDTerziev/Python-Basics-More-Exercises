holidays = int(input())
workdays = 365 - holidays

total_time = holidays * 127 + workdays * 63
if total_time <= 30000:
    under_play_time = 30000 - total_time
    under_play_hours = under_play_time // 60
    under_play_mins = under_play_time % 60
    print("Tom sleeps well")
    print(f"{under_play_hours} hours and {under_play_mins} minutes less for play")
else:
    above_playing_time = total_time - 30000
    above_play_hours = above_playing_time // 60
    above_play_mins = above_playing_time % 60
    print("Tom will run away")
    print(f"{above_play_hours} hours and {above_play_mins} minutes more for play")