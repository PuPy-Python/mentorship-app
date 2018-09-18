# Contributing

Guidelines and expectations for contributing to this open source project.


## Git Hygiene

Following are expectations for developers contributing to this repo.

1. Fork the project repository to create a personal working repo
2. Push all feature branches to your personal repo
3. All feature branches must be rebased from upstream/master before PR
    To keep rebasing your work:
    `git pull --rebase prod master`
4. All PR's should be atomic (1 commit) for ease of reversion/rollback
5. PR's must be approved by a developer before merge
6. PR's must pass automated tests

How to squash commits:

Method 1:
    Use `git commit --amend` and `git push remote branch -f`

Method 2:
    Make multiple commits as usual, then:
    `git checkout master`
    `git pull master`
    `git checkout feature-branch`
    `git rebase master`
    `git reset $(git merge-base master feature-branch)`
    `git add -A`
    `git commit -m 'the whole feature'`
    `git push <remote> <branch> -f`

## Deployment

This project is committed to following best practices of CI and CD.  To that end, automated testing is performed via Travis-CI and automated deployment is performed via Heroku.

A successful deployment is dependent on three things:
1. Passing Travis-CI tests
2. Peer code review and approval
3. Successful automated deploy

TODO: Need public feedback for successful deploy
TODO: How to Rollback

## Getting Started with git

1. Fork the project repository to create a personal working repo
2. Clone your fork `git clone <your-fork>`
3. Set the project repository as upstream, and rename it `git remote add upstream <production-repo>` and `git remote rename upstream prod`
4. Set rename your fork `git remote rename origin <your-name>`
5. Check the remote repository names `git remote -v` should have 4 lines
