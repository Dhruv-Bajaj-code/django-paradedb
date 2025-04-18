from django.db.models import Index

class BM25Index(Index):
    suffix = 'bm25'
    
    def __init__(self, *, with_options=None, **kwargs):
        self.with_options = with_options or {}
        super().__init__(**kwargs)
    
    def deconstruct(self):
        path, args, kwargs = super().deconstruct()
        if self.with_options:
            kwargs['with_options'] = self.with_options
        return path, args, kwargs
    
    def create_sql(self, model, schema_editor, using=''):
        fields = [model._meta.get_field(field_name) for field_name in self.fields]
        columns = [schema_editor.quote_name(field.column) for field in fields]
        
        sql = "CREATE INDEX %(name)s ON %(table)s USING bm25 (%(columns)s)" % {
            "name": schema_editor.quote_name(self.name),
            "table": schema_editor.quote_name(model._meta.db_table),
            "columns": ", ".join(columns),
        }
        
        if self.with_options:
            options = ", ".join(f"{k}='{v}'" for k, v in self.with_options.items())
            sql += f" WITH ({options})"
            
        return sql

# class HNSWIndex(Index):
#     suffix = 'hnsw'
    
#     def __init__(self, *, with_options=None, **kwargs):
#         self.with_options = with_options or {}
#         super().__init__(**kwargs)
    
#     def deconstruct(self):
#         path, args, kwargs = super().deconstruct()
#         if self.with_options:
#             kwargs['with_options'] = self.with_options
#         return path, args, kwargs
    
#     def create_sql(self, model, schema_editor, using=''):
#         field = model._meta.get_field(self.fields[0])
#         column = schema_editor.quote_name(field.column)
        
#         sql = "CREATE INDEX %(name)s ON %(table)s USING hnsw (%(column)s)" % {
#             "name": schema_editor.quote_name(self.name),
#             "table": schema_editor.quote_name(model._meta.db_table),
#             "column": column,
#         }
        
#         if self.with_options.get('operator'):
#             sql += f" {self.with_options['operator']}"
            
#         return sql