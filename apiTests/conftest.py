import pytest
from petstore import BASE_URL

from petstore import Petstore

@pytest.fixture
def api(request):
    yield Petstore(BASE_URL)