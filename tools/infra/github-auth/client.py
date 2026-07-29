"""GitHub credential registration for sandboxes.

Carries the GITHUB_TOKEN secret declaration in pyproject.toml. The exposed
method is a health check so the declaration lives on a real, discoverable tool.
"""


class GithubAuthClient:
    def check(self) -> dict:
        """Report whether the proxy-injected GitHub credential works."""
        import httpx

        response = httpx.get(
            "https://api.github.com/installation/repositories",
            headers={"authorization": "Bearer GITHUB_TOKEN"},
            timeout=15,
        )
        return {"status_code": response.status_code, "ok": response.status_code == 200}


def _client() -> GithubAuthClient:
    return GithubAuthClient()
