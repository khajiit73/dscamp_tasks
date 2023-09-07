coin_h_probability = [0.1, 0.2, 0.4, 0.8, 0.9]
coin_pick_chance = [0.2, 0.2, 0.2, 0.2, 0.2]
tosses = ["H", "H", "H", "T", "H", "T", "H", "H"]

def probability(prob: float, side: str):        #probability depending on the side of the coin
    return prob if side == "H"  else 1 - prob

#full probability
def full_probability(side: str):
    full_prob = 0
    for prob, pick_chance in zip(coin_h_probability, coin_pick_chance):
        prob_ = probability(prob, side)
        full_prob += prob_ * pick_chance
    return full_prob

def calc_probability(side: str):
    global coin_pick_chance

    #full probability of tossing "H" for this toss
    full_prob_current = full_probability(side)
    
    #recalculating chance that certain coin was picked according to the result of the toss
    coin_pick_chance = [
        ((probability(prob, side) * pick_chance) / full_prob_current)
        for prob, pick_chance in zip(coin_h_probability, coin_pick_chance) 
    ]

    #full probability of tossing "H" for the next toss
    full_prob_next = full_probability(side)

    return round(probability(full_prob_next, side), 2)

result = [calc_probability(toss) for toss in tosses]
print(result)

#[0.69, 0.79, 0.83, 0.74, 0.8, 0.69, 0.76, 0.8]