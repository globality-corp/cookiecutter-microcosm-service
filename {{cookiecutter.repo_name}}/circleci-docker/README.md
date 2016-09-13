# globality-circleci-docker

# Problem

Currently there is no direct support for pushing images to docker registries in circleci.

# Solution

Circleci does support running arbitrary commands. The script in this
respository builds an image from a project, tags it into a docker registry and
pushes it there with both a tag for the SHA of the commit that triggered this
build as well as a tag for the branch the image was built from.

Release branches are a special case and all release branches are tagged into
one `release` tag.

# Usage

You can use this script in your repo with git subtrees:

`git subtree pull --prefix circleci-docker https://github.com/globality-corp/globality-circleci-docker master --squash`

This will pull this repo into a directory circleci-docker in your project and
you will be able to build a docker image from you project by calling the
`push_to_ecr.sh` script from your circle.yml file. For example:

```
dependencies:
  override:
    - ./circleci-docker/push_to_ecr.sh
```
