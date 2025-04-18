# paradedb/lookups.py
from django.db.models import Lookup
from django.db.models.fields import Field

@Field.register_lookup
class BM25Search(Lookup):
    lookup_name = 'bm25'
    
    def as_sql(self, compiler, connection):
        if connection.vendor != 'postgresql':
            raise ValueError("BM25 search requires PostgreSQL")
            
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        return f"{lhs} @@@ {rhs}", lhs_params + rhs_params  # ParadeDB uses @@@ operator

@Field.register_lookup
class VectorSearch(Lookup):
    lookup_name = 'vec'
    
    def as_sql(self, compiler, connection):
        if connection.vendor != 'postgresql':
            raise ValueError("Vector search requires PostgreSQL")
            
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        return f"{lhs} <=> {rhs}", lhs_params + rhs_params  # ParadeDB vector operator