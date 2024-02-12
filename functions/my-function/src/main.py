import functions_framework
from flask import Request
from flask import Response


@functions_framework.http  # type: ignore
def handler(request: Request) -> Response:
    body = request.get_json()  # for fake response

    return Response(body)
