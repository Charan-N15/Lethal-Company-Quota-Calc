
def calc_days(curr_quota, days_comp, target_quota):
    #calculate number of days to fulfill target quota
    #calc is short for calcualtor if youre new to the stream
    return ((target_quota - curr_quota) * 3) - days_comp

def calc_scrap_needed(curr_quota, ship_loot, target_quota, avg_quotas):
    t_v = avg_quotas[target_quota]
    c_v = avg_quotas[curr_quota]
    return (t_v - c_v - ship_loot)

def calc_avg():
    curr_quota = int(input("Enter quota number:\t"))
    days_comp = int(input("Days completed in current quota (0-2):\t"))
    ship_loot = int(input("Enter the loot on your ship:\t"))
    # dictionary of quotas and their avg value
    avg_quotas = {1: 0,
                  2: 130,
                  3: 366,
                  4: 727,
                  5: 1245,
                  6: 1962,
                  7: 2936,
                  8: 4235,
                  9: 5940,
                  10: 8145,
                  11: 10956,
                  12: 14492,
                  13: 18885,
                  14: 24277,
                  15: 30826,
                  16: 38700,
                  17: 48080,
                  18: 59160,
                  19: 72146,
                  20: 87257}
    avg_quota_vals = {1:130,
                      2:230,
                      3:350,
                      4:500,
                      5:700,
                      6:800,
                      7:1300,
                      8:1700,
                      9:2200,
                      10:2800,
                      11:3550,
                      12:4400,
                      13:5400,
                      14:6550,
                      15:7900,
                      16:9400,
                      17:11000,
                      18:13000,
                      19:15000,
                      20:17500}

    for i in range(curr_quota + 1,21):
        print(f"Quota (~{avg_quota_vals[i]}): {i} \t Average per day: {calc_scrap_needed(curr_quota,ship_loot,i,avg_quotas) / calc_days(curr_quota,days_comp,i)} ")

calc_avg()



