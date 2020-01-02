from requests.compat import urljoin

from ..utils.urls import URL

__all__ = ["Resource"]


class Resource:
    endpoint = None

    def __init__(self, client=None):
        self.client = client

    def _get(self, url, data, **kwargs):
        return self.client.get(url, data, **kwargs)

    def _patch(self, url, data, **kwargs):
        return self.client.patch(url, data, **kwargs)

    def _post(self, url, data, **kwargs):
        return self.client.post(url, data, **kwargs)

    def _put(self, url, data, **kwargs):
        return self.client.put(url, data, **kwargs)

    def _delete(self, url, data, **kwargs):
        return self.client.delete(url, data, **kwargs)

    def _get_url(self, *args):
        return urljoin(
            URL.BASE,
            "/".join([URL.VERSION, self.endpoint] + [str(arg) for arg in args]),
        )

    def create(self, data, **options):
        url = self._get_url()
        return self._post(url, data, **options)

    def list(self, data=None, **options):
        url = self._get_url()
        return self._get(url, data, **options)

    def read(self, id_, data=None, **options):
        url = self._get_url(id_)
        return self._get(url, data, **options)

    def update(self, id_, data=None, **options):
        url = self._get_url(id_)
        return self._patch(url, data, **options)

    def delete(self, id_, data=None, **options):
        url = self._get_url(id_)
        return self._delete(url, data, **options)
