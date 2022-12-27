import unittest
from datetime import datetime
from http import HTTPStatus
from unittest.mock import Mock, call, patch

from .github_api import GitHubAPI
from .user_details import UserDetails


class TestGitHubAPI(unittest.TestCase):
    @patch("professional_python_exercises_3_api.api.github_api.Github", autospec=True)
    def test_construction(self, mock_gh_cls: Mock):
        token = "abc123"

        mock_gh = mock_gh_cls.return_value

        instance = GitHubAPI(token)

        assert instance.session == mock_gh
        mock_gh_cls.assert_called_once_with(token)

    @patch("professional_python_exercises_3_api.api.github_api.Github", autospec=True)
    def test_get_authenticated_user(self, mock_gh_cls: Mock):
        token = "abc123"
        expected_username = "tony"

        mock_gh = mock_gh_cls.return_value
        fake_gh_user = Mock()
        fake_gh_user.login = expected_username
        mock_gh.get_user.return_value = fake_gh_user

        instance = GitHubAPI(token)
        username = instance.get_authenticated_user()

        assert instance.session == mock_gh
        mock_gh_cls.assert_called_once_with(token)
        assert username == expected_username
        mock_gh.get_user.assert_called_once_with()

    @patch("professional_python_exercises_3_api.api.github_api.Github", autospec=True)
    def test_count_repos_and_stars(self, mock_gh_cls: Mock):
        token = "abc123"
        expected_username = "tony"

        mock_gh = mock_gh_cls.return_value
        fake_gh_user = Mock()
        mock_gh.get_user.return_value = fake_gh_user

        fake_repo1 = Mock()
        fake_repo1.stargazers_count = 3
        fake_repo2 = Mock()
        fake_repo2.stargazers_count = 2
        fake_gh_user.get_repos.return_value = [fake_repo1, fake_repo2]

        instance = GitHubAPI(token)
        counter = instance.count_repos_and_stars(expected_username)

        assert instance.session == mock_gh
        mock_gh_cls.assert_called_once_with(token)
        assert counter.username == expected_username
        assert counter.repo_count == 2
        assert counter.star_count == 5
        mock_gh.get_user.assert_called_once_with(expected_username)
        fake_gh_user.get_repos.assert_called_once_with()

    @patch("professional_python_exercises_3_api.api.github_api.sys.exit")
    @patch("professional_python_exercises_3_api.api.github_api.typer.echo", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.Github", autospec=True)
    def test_user_details(self, mock_gh_cls: Mock, mock_typer_echo: Mock, mock_sys_exit: Mock):
        token = "abc123"
        expected_username = "tony"

        mock_gh = mock_gh_cls.return_value
        fake_gh_user = Mock()
        mock_gh.get_user.return_value = fake_gh_user

        fake_gh_user.login = expected_username
        fake_gh_user.bio = "bio"
        fake_gh_user.blog = "blog"
        fake_gh_user.company = "company"
        fake_gh_user.contributions = "contributions"
        fake_gh_user.created_at = datetime.now()
        fake_gh_user.email = "email"
        fake_gh_user.avatar_url = "avatar_url"
        fake_gh_user.location = "location"
        fake_gh_user.hireable = "hireable"
        # gh_user.get_repos
        fake_repo1 = Mock()
        fake_repo1.stargazers_count = 3
        fake_repo2 = Mock()
        fake_repo2.stargazers_count = 2
        fake_gh_user.get_repos.return_value = [fake_repo1, fake_repo2]
        # gh_user.get_orgs
        fake_orgs = fake_gh_user.get_orgs.return_value
        fake_orgs.totalCount = 3
        # gh_user.get_starred
        fake_starred = fake_gh_user.get_starred.return_value
        fake_starred.totalCount = 3
        # gh_user.get_subscriptions
        fake_subscriptions = fake_gh_user.get_subscriptions.return_value
        fake_subscriptions.totalCount = 3
        # gh_user.get_watched
        fake_watched = fake_gh_user.get_watched.return_value
        fake_watched.totalCount = 3
        # gh_user.get_followers
        fake_followers = fake_gh_user.get_followers.return_value
        fake_followers.totalCount = 3
        # gh_user.get_following
        fake_following = fake_gh_user.get_following.return_value
        fake_following.totalCount = 3

        expected_details = UserDetails(
            username=expected_username,
            bio=fake_gh_user.bio,
            blog=fake_gh_user.blog,
            company=fake_gh_user.company,
            contributions=fake_gh_user.contributions,
            created=fake_gh_user.created_at.isoformat(),
            email=fake_gh_user.email,
            avatar_url=fake_gh_user.avatar_url,
            location=fake_gh_user.location,
            hireable=fake_gh_user.hireable,
            organization_count=3,
            star_count=5,
            repo_count=2,
            starred_count=3,
            subs_count=3,
            watched_count=3,
            follower_count=3,
            following_count=3,
        )

        instance = GitHubAPI(token)
        details = instance.user_details(expected_username)

        assert instance.session == mock_gh
        mock_gh_cls.assert_called_once_with(token)
        assert details == expected_details
        mock_gh.get_user.assert_called_once_with(expected_username)
        mock_typer_echo.assert_not_called()
        mock_sys_exit.assert_not_called()
        fake_gh_user.get_repos.assert_called_once_with()
        fake_gh_user.get_orgs.assert_called_once_with()
        fake_gh_user.get_starred.assert_called_once_with()
        fake_gh_user.get_subscriptions.assert_called_once_with()
        fake_gh_user.get_watched.assert_called_once_with()
        fake_gh_user.get_followers.assert_called_once_with()
        fake_gh_user.get_following.assert_called_once_with()

    @patch("professional_python_exercises_3_api.api.github_api.sys.exit")
    @patch("professional_python_exercises_3_api.api.github_api.typer.echo", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.requests", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.get_github_token", autospec=True)
    def test_set_status_ok(
        self, mock_get_token: Mock, mock_requests: Mock, mock_typer_echo: Mock, mock_sys_exit: Mock
    ):
        token = "abc123"

        mock_get_token.return_value = token

        fake_response = mock_requests.post.return_value
        fake_response.status_code = HTTPStatus.OK
        fake_response.json.return_value = {}

        instance = GitHubAPI(token)
        instance.set_status("emoji", "msg")

        mock_requests.post.assert_called_once()
        fake_response.json.assert_called_once()
        mock_typer_echo.assert_not_called()
        mock_sys_exit.assert_not_called()

    @patch("professional_python_exercises_3_api.api.github_api.typer.echo", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.requests", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.get_github_token", autospec=True)
    def test_set_status_request_error(
        self, mock_get_token: Mock, mock_requests: Mock, mock_typer_echo: Mock
    ):
        token = "abc123"

        mock_get_token.return_value = token

        fake_response = mock_requests.post.return_value
        fake_response.status_code = HTTPStatus.FORBIDDEN
        fake_response.json.return_value = {}

        with self.assertRaises(SystemExit) as ex:
            instance = GitHubAPI(token)
            instance.set_status("emoji", "msg")
            assert ex.exception.code == 1

        mock_requests.post.assert_called_once()
        fake_response.json.assert_not_called()
        mock_typer_echo.assert_called_once_with("Mutation failed to run by returning code of 403.")

    @patch("professional_python_exercises_3_api.api.github_api.typer.echo", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.requests", autospec=True)
    @patch("professional_python_exercises_3_api.api.github_api.get_github_token", autospec=True)
    def test_set_status_request_format_error(
        self, mock_get_token: Mock, mock_requests: Mock, mock_typer_echo: Mock
    ):
        token = "abc123"

        mock_get_token.return_value = token

        fake_response = mock_requests.post.return_value
        fake_response.status_code = HTTPStatus.OK
        fake_response.json.return_value = {
            "errors": [
                {"message": "Pewpew", "type": "type1"},
                {"message": "Pewpew", "type": "type2"},
            ]
        }

        with self.assertRaises(SystemExit) as ex:
            instance = GitHubAPI(token)
            instance.set_status("emoji", "msg")
            assert ex.exception.code == 1

        mock_requests.post.assert_called_once()
        fake_response.json.assert_called_once_with()
        mock_typer_echo.assert_has_calls([call("type1: Pewpew"), call("type2: Pewpew")])
