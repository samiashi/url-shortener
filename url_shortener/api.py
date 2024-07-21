import hashlib
from datetime import datetime
from urllib.parse import urljoin

from django.shortcuts import get_object_or_404, redirect
from ninja import NinjaAPI

from url_shortener.models import Redirect
from url_shortener.schemas import AddUrlSchema

api = NinjaAPI()


@api.post("generate/")
def add_url(request, payload: AddUrlSchema):
    print(payload)
    host = request.build_absolute_uri("/")
    url_redirect = Redirect.objects.filter(original_url=payload.url)

    if url_redirect.exists():
        url_hash = url_redirect.first().url_hash
        return urljoin(host, url_hash)

    url_str = str(payload.url).encode()
    url_hash = hashlib.sha256(url_str).hexdigest()[:8]
    return_url = urljoin(host, url_hash)

    url_redirect = Redirect.objects.create(
        original_url=payload.url,
        url_hash=url_hash,
        hits=0,
    )
    return return_url


@api.get("{url_hash}/")
def get_url(request, url_hash: str):
    url_redirect = get_object_or_404(Redirect, url_hash=url_hash)

    url_redirect.hits += 1
    url_redirect.last_hit = datetime.now()
    url_redirect.save()

    return redirect(url_redirect.original_url, permanent=True)
