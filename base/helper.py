from rest_framework.response import Response


class MethodNot:
    def get(selfs, req):
        return Response({
            "error": "bu zaprost ishlamaydi"
        })

    def post(selfs, req):
        return Response({
            "error": "bu zaprost ishlamaydi"
        })

    def put(selfs, req):
        return Response({
            "error": "bu zaprost ishlamaydi"
        })

    def putch(selfs, req):
        return Response({
            "error": "bu zaprost ishlamaydi"
        })

    def delete(selfs, req):
        return Response({
            "error": "bu zaprost ishlamaydi"
        })

