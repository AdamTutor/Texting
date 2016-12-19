from db import *

def testCountEvents():
    """
    Tests if count of events is 0 after all events deleted.
    Tests if count is 1 after an event is registered
    """
    deleteTeams()
    id1 = registerTeam('blue')
    id2 = registerTeam('red')
    deleteEvents()
    c = countEvents()
    assert c == 0,  "countEvents should return 0 after deletion"
    registerEvent(id1, id2, '20120618 10:34:09', 'Event')
    c = countEvents()
    assert c == 1, "Event has been registerd, count should return 1. Function returned {num}".format(num=c)
    registerEvent(id1, id2, '20120618 10:34:09', 'Event')
    c = countEvents()
    assert c == 2, "Event has been registerd, count should return 1. Function returned {num}".format(num=c)
    deleteEvents()
    c = countEvents()
    assert c == 0, "Events deleted but count did not return 0"

def testCountTeams():
    """
    Tests if count of events is 0 after all events deleted.
    Tests if count is 1 after an event is registered
    """
    deleteTeams()
    c = countTeams()
    assert c == 0,  "countTeams should return 0 after deletion"
    registerTeam('blue')
    c = countTeams()
    assert c == 1, "Team has been registerd, count should return 1. Function returned {num}".format(num=c)
    registerTeam('red')
    c = countTeams()
    assert c == 2, "Team has been registerd, count should return 1. Function returned {num}".format(num=c)
    deleteTeams()
    c = countTeams()
    assert c == 0, "Teams deleted but count did not return 0"
