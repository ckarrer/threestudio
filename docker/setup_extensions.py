import git
import os
import getpass

repos = [
    "https://github.com/ckarrer/threestudio-3dgs.git",
    "https://github.com/ashawkey/diff-gaussian-rasterization.git",
    "https://github.com/DSaurus/simple-knn.git"
]

userName = getpass.getuser()
os.chdir(f"/home/{userName}/threestudio/custom")
git.Repo.clone_from("https://github.com/ckarrer/threestudio-3dgs.git", "threestudio-3dgs")
os.chdir("threestudio-3dgs")
git.Repo.clone_from("https://github.com/ashawkey/diff-gaussian-rasterization.git", "diff-gaussian-rasterization")
git.Repo.clone_from("https://github.com/DSaurus/simple-knn.git", "simple-knn")
