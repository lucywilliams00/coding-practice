## An instructor has been booked on clashing events,
## so we want to highlight conflicting events in their schedule
## Given a list of their events with start and end times,
## can you return a list of conflicts?
Event = namedtuple('Event', ['id', 'start', 'end'])
list = [
  Event(1, 1, 2),
  Event(2, 2, 4),
  Event(3, 3, 5),
  Event(4, 5, 8),
  Event(5, 9, 12),
  Event(6, 10, 16),
  Event(7, 11, 13),
  Event(8, 14, 15),
  Event(9, 17, 18),
  Event(10, 17, 18),
]
def find_conflicts(events: List[Event]):
  conflicts = []
  for event, i in enumerate(events):
    if i == len(events):
        continue
    if events[i].end > events[i+1].start:
        conflicts.append((events[i].id, events[i+1].id))
  return conflicts

    
    
find_conflicts(instructor_events)
#conflict end > start
#for i in list
#if i(end)>i+1(start) = conflict
#if i = len(list) end

# [(2,3)]