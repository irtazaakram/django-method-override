def test_noop(client):
    response = client.post('/', {'foo': 'bar'})
    assert response.wsgi_request.method == 'POST'


def test_get_param_noop(client):
    response = client.get('/', {}, HTTP_X_HTTP_METHOD_OVERRIDE='PUT')
    assert response.wsgi_request.method == 'GET'


def test_unsupported_method(client):
    response = client.post('/', {'_method': 'DESTROY'})
    assert response.wsgi_request.method == 'POST'


def test_param_override(client):
    response = client.post('/', {'_method': 'PUT'})
    assert response.wsgi_request.method == 'PUT'


def test_lowercase_param_override(client):
    response = client.post('/', {'_method': 'delete'})
    assert response.wsgi_request.method == 'DELETE'


def test_header_override(client):
    response = client.post('/', {}, HTTP_X_HTTP_METHOD_OVERRIDE='DELETE')
    assert response.wsgi_request.method == 'DELETE'
