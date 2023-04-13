import numpy as np

def crush_ice(hammers):
    originalHammers = hammers
    if hammers <= 0: return

    layers = [0.125, 0.083, 0.125, 0.083, 0.063, 0.125, 0.083, 0.125, 0.083, 0.063]\
    + [0.125, 0.083, 0.125, 0.083, 0.063, 0.063, 0.083, 0.063, 0.063, 0.05]*14

    for layer, prob in enumerate(layers):
        if hammers <= 0: break

        bonus = 2
        steps = 0
        isPromotion = False

        while(hammers > 0 and steps < 28 and not isPromotion):
            steps += 1
            hammers -= 1

            if steps == 28:
                isPromotion = True
                break

            isPromotion = np.random.choice([False, True], p = [1 - prob, prob])


            if isPromotion:
                break

            bonusProb = bonus / (28 - steps + 1)
            isBonus = True if 28 - steps < bonus else np.random.choice([False, True], p = [1 - bonusProb, bonusProb])

            if isBonus:
                hammers += 1
                bonus -= 1

        if not isPromotion: break

    return [originalHammers, layer + 1]