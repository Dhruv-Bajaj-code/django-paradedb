from django.db.models import Func

class BM25Score(Func):
    function = 'paradedb.score'
    arity = 1