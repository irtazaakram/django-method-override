from method_override.templatetags.method_override import method_override


def test_method_override():
    result = method_override('PUT')
    assert result == '<input type="hidden" name="_method" value="PUT">'


def test_method_override_marked_safe():
    result = method_override('PUT')
    assert hasattr(result, '__html__')
