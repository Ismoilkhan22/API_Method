# from contextlib import closing
# from django.db import connection
# from methodism import dictfetchall, dictfetchone
# from rest_framework.decorators import api_view
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
#
#
# @api_view(['GET'])
# def search_sql(key):
#     sql = f"""
#     SELECT * from core_product
#     where name like '%{key}%' or desc like '%{key}%'
#     """
#     with closing(connection.cursor()) as cursor:
#         cursor.execute(sql)
#         result = dictfetchall(cursor)
#     return Response(result)
