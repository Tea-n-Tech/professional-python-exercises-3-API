from contextlib import suppress
import requests
from github_cli import _rate_stars_to_repos
from github_cli import setstatus
from unittest import mock


class TestStarRater:
    def test_ratings(self):
        assert _rate_stars_to_repos(0, 10) == "This poor fellar. Work harder!"
        assert _rate_stars_to_repos(0, 0) == "This poor fellar. Work harder!"
        assert _rate_stars_to_repos(1, 10) == "Keep doing what you're doing. But do more!"
        assert _rate_stars_to_repos(20, 10) == "Not bad ey, not bad."
        assert _rate_stars_to_repos(2000, 10) == "Greetings, Mr. Starlord"


class TestSetStatus:
    @mock.patch("github_cli.requests.post", autospec=True)
    def test_set_status_all_good(self, request_mock: mock.Mock):
        all_good_response = requests.Response()
        all_good_response.status_code = 200
        request_mock.return_value = all_good_response
        success = setstatus()
        assert request_mock.called
        assert success

    @mock.patch("github_cli.requests.post", autospec=True)
    def test_set_status_not_good(self, request_mock: mock.Mock):
        not_good_response = requests.Response()
        not_good_response.status_code = 401
        request_mock.return_value = not_good_response
        with suppress(Exception):
            success = setstatus()
        assert request_mock.called
        assert success is False
