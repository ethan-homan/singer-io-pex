import subprocess
import tempfile
import os

from fastapi import APIRouter

from app.types import GitHubSyncConfig

router = APIRouter()


@router.post("/sync-repository/")
def get_performance_lists(
    request: GitHubSyncConfig,
) -> str:
    git_config_file = tempfile.NamedTemporaryFile("w", delete=False)
    git_config_file.write(request.json())
    git_config_file.close()
    in_process = subprocess.Popen(
        [
            "tap-github",
            "--config",
            git_config_file.name,
            "--properties",
            "src/tap_github_svc/schemas/commits.json",
        ],
        stdout=subprocess.PIPE,
    )
    subprocess.run(
        ["dist/src.target_csv_bin/target_csv_bin.pex"],
        stdin=in_process.stdout,
    )
    os.remove(git_config_file.name)
