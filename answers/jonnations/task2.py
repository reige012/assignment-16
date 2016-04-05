#!/usr/bin/env python
# utf-8

"""
Assignment 8, Task 1
Jon Nations on 14 February 2016

"""



def counting(galapagos):
    # counts the number of ".'s" in the string
    c = (galapagos.count("."))
    return c


def finder(galapagos):
    # finds the position of the word "mysterious"
    f = galapagos.find("coral")
    return f


def splits(galapagos):
    # splits the two sentences into two strings
    s = galapagos.split(".")
    return s


def up(galapagos):
    # makes all lettes uppercase
    u = galapagos.upper()
    return u


def replacing(galapagos):
    # replaces "beautiful" with "magnanimous"
    r = galapagos.replace("The", "DA")
    return r

def main():
    galapagos = "THE THING WAS: One million years ago, back in 1986 A.D., Guayaquil was the chief seaport of the little South American democracy of Ecuador, whose capital was Quito, high in the Andes Mountains. Guayaquil was two degrees south of the equator, the imaginary bellyband of the planet after which the country itself was named. It was always very hot there, and humid, too, for the city was built in the doldrums on a springy marsh through which the mingled waters of several rivers draining the mountains flowed. This seaport was several kilometers from the open sea. Rafts of vegetable matter often clogged the soupy waters, engulfing pilings and anchor lines. Human beings had much bigger brains back then than they do today, and so they could be beguiled by mysteries. One such mystery in 1986 was how so many creatures which could not swim great distances had reached the Gala¡pagos Islands, an archipelago of volcanic peaks due west of Guayaquil, separated from the mainland by one thousand kilometers of very deep water, very cold water fresh from the Antarctic. When human beings discovered those islands, there were already geckos and iguanas and rice rats and lava lizards and spiders and ants and beetles and grasshoppers and mites and ticks in residence, not to mention enormous land tortoises. What form of transportation had they used? Many people were able to satisfy their big brains with this answer: They came on natural rafts. Other people argued that such rafts became waterlogged and rotted to pieces so quickly that nobody had ever seen one out of sight of land, and that the current between the islands and the mainland would carry any such rustic vessel northward rather than westward. Or they asserted that all those landlubberly creatures had walked dry-shod across a natural bridge or had swum short distances between stepping-stones, and that one such formation or another had since disappeared beneath the waves. But scientists using their big brains and cunning instruments had by 1986 made maps of the ocean floor. There wasn't a trace, they said, of an intervening land mass of any kind. Other people back in that era of big brains and fancy thinking asserted that the islands had once been part of the mainland, and had been split off by some stupendous catastrophe. But the islands didn't look as though they had been split off from anything. They were clearly young volcanoes, which had been vomited up right where they were. Many of them were such newborns out there that they could be expected to blow again at any time. Back in 1986, they hadn't even sprouted much coral yet, and so were without blue lagoons and white beaches, amenities many human beings used to regard as foretastes of an ideal afterlife."
    """print(cleaning(galapagos))"""
    counting(galapagos)
    finder(galapagos)
    splits(galapagos)
    up(galapagos)
    replacing(galapagos)


if __name__ == '__main__':
    main()
