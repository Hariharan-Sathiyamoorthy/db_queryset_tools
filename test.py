from db_queryset_tools_pkg import DB_queryset_tools

tools = DB_queryset_tools()
quer_lists = tools.queryset_to_list("queryset")

print(quer_lists)
