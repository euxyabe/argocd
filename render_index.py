from html import escape
from pathlib import Path
import os


def build_value(name: str, default: str) -> str:
    return escape(os.environ.get(name, default), quote=True)


replacements = {
    "__PAGE_TITLE__": build_value("PAGE_TITLE", "Nginx Demo"),
    "__PAGE_MESSAGE__": build_value(
        "PAGE_MESSAGE",
        "Deployed by GitHub Actions, ECR, Argo CD, and EKS.",
    ),
    "__GIT_SHA__": build_value("GIT_SHA", "local"),
    "__GITHUB_RUN_NUMBER__": build_value("GITHUB_RUN_NUMBER", "local"),
    "__BUILD_TIME__": build_value("BUILD_TIME", "local"),
}

page = Path("index.html.template").read_text(encoding="utf-8")

for placeholder, value in replacements.items():
    page = page.replace(placeholder, value)

Path("index.html").write_text(page, encoding="utf-8")
