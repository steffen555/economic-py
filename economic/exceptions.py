# coding=UTF-8
def is_ok_or_throw_exception(request):
    if request.status_code == 400:
        raise Exception('400 Bad Request. The request you made was somehow malformed. A malformed request could be '
                        'failed validation on creation or updating. If you try to filter on something that isn’t '
                        'filterable this is also what you’ll see. Whenever possible we will also try to include a '
                        'developer hint to help you get around this issue.')
    if request.status_code == 401:
        raise Exception('401 Unauthorized. The credentials you supplied us with weren’t correct, or perhaps you forgot '
                        'them all together. If an agreement has revoked the grant they gave your app, this is what you '
                        'will see.')
    if request.status_code == 403:
        raise Exception('403 Forbidden. You won’t necessarily have access to everything. So even though you were '
                        'authorized we might still deny access to certain resources. This depends on the roles asked '
                        'for when the grant was issued.')
    if request.status_code == 404:
        raise Exception('404 Not Found This is returned when you try to request something that doesn’t exist. This '
                        'could be a resource that has been deleted or just a url you tried to hack. If you see a lot '
                        'of these, it could be an indication that you aren’t using the links provided by the API. You '
                        'should never need to concatenate any urls. The API should provide you with the links needed.')
    if request.status_code == 405:
        raise Exception('405 Method Not Allowed. Not all endpoints support all http methods. If you try issue a PUT '
                        'request to a collection resource this is what you get.')
    if request.status_code == 415:
        raise Exception('415 Unsupported Media Type. Our API is a JSON api. If you ask us to give you anything else, '
                        'we give you this, and tell you why in the JSON body of the response.')
