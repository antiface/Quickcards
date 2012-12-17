# Concept inventory for reference card system

# High Level
# card, cardBox, cardReferences, cardType, cardElements, referenceDict, cardCollection,
# collectionID, referenceID

# Low Level
# Concepts: card, create, delete, add_to, project,
# priority, priorityList, task, TaskGroup, taskDict,
# items, context, pending[], getFile, fetch, source,
# class Event(object), class CollectionStartEvent(NodeEvent),
# node, edge, anchor, token/tag, refcard, log_file. See: Gitmarks
#
# Classes/Entities, Events
# 
# Basically, you have Cards, Collections of Cards, the Content of Cards, and References
# between Cards. The Card itself is a dictionary in Python, but could be a bit of JSON.
# Simply put, Cards are Nodes in a network. This is very hypertextual.
#
#
#
#
#
#