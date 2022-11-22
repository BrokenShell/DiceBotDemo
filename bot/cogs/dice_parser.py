from Fortuna import dice


def parse_dice(dice_expr):

    rolls, sides = dice_expr.split("d")
    rolls = int(rolls) if rolls else 1
    sides = int(sides) if sides else 20

    return dice(rolls, sides)
