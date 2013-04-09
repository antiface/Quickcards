class Card(object):
"""A class representing the card structure."""

def __init__(self,
               created_at=None,
               id=None,
               text=None,
               user=None,
               source=None,
               urls=None,
               hashtags=None,
               place=None,
               contributors=None):
               
    """An object to hold card contents.
    
    self.created_at = created_at
    self.id = id
    self.text = text
    self.user = user
    self.source = source
    self.urls = urls
    self.hashtags = hashtags
    self.place = place
    self.contributors = contributors
    """
    
  def GetCreatedAt(self):
    '''Get the time this card was created.

    Returns:
      The time this card was created.
    '''
    return self._created_at

  def SetCreatedAt(self, created_at):
    '''Set the time this card was created.

    Args:
      created_at:
        The time this card was created
    '''
    self._created_at = created_at

  created_at = property(GetCreatedAt, SetCreatedAt,
                        doc='The time this card was created.')

  def GetId(self):
    '''Get the unique id of this card.

    Returns:
      The unique id of this card.
    '''
    return self._id

  def SetId(self, id):
    '''Set the unique id of this card.

    Args:
      id:
        The unique id of this card.
    '''
    self._id = id

  id = property(GetId, SetId,
                doc='The unique id of this card.')
                
  def GetText(self):
    '''Get the text of card.

    Returns:
      The text of this card.
    '''
    return self._text

  def SetText(self, text):
    '''Set the text of this card.

    Args:
      text:
        The text of this card.
    '''
    self._text = text

  text = property(GetText, SetText,
                  doc='The text of this card')
