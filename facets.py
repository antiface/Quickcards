class Facets(dict):

def __init__(self, slug, name, facets=[], description=""):
        self.name = name
        self.slug = slug
        self._facet_lookup = {}
        self.description = description

""" Snippet for reference for json objects later on.
{
        "pk": 1,
        "model": "tests.user",
        "fields": {
            "username": "alex",
            "status": 1,
            "first_name": "",
            "last_name": "",
            "favorite_books": [1, 2],
            "is_active": false
        }
"""
