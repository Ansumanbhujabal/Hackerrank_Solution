"""
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost to convert a black gift into white gift or vice versa is  units.
Determine the minimum cost of Diksha's gifts.
"""


def taumBday(b, w, bc, wc, z):
    return min((b*bc+w*wc), ((b+w)*wc+b*z), ((b+w)*bc+w*z))
