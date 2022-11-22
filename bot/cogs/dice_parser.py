from Fortuna import dice


def parse_dice(dice_expression):
    if "+" in dice_expression:
        op = "+"
        dice_expression, modifier = dice_expression.split(op)
        modifier = int(modifier)
    elif "-" in dice_expression:
        op = "-"
        dice_expression, modifier = dice_expression.split(op)
        modifier = abs(int(modifier))
    else:
        modifier = ""
        op = ""

    if "d" in dice_expression:
        rolls, sides = dice_expression.split('d')
        rolls = int(rolls) if rolls else 1
        sides = int(sides) if sides else 20
    else:
        rolls = 1
        sides = int(dice_expression)

    if op == "+":
        output = {
            "Expression": f'`{rolls if rolls != 1 else ""}d{sides}+{modifier}`',
            "Roll": f'{dice(rolls, sides) + modifier}',
        }
    elif op == '-':
        output = {
            "Expression": f'`{rolls if rolls != 1 else ""}d{sides}-{modifier}`',
            "Roll": f'{dice(rolls, sides) - modifier}',
        }
    else:
        output = {
            "Expression": f'`{rolls if rolls != 1 else ""}d{sides}`',
            "Roll": f'{dice(rolls, sides)}',
        }

    return f"{output['Expression']} => {output['Roll']}"
