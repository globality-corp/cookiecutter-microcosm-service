# This assumes the following variables are available to the circleci job:
# CIRCLE_BRANCH: available by default in all circleci jobs
# CIRCLE_SHA1: available by default in all circleci jobs
# ECR_INSTANCE_ID: should be your amazon ecr instance id.
# ECR_DOMAIN: Should be the amazon ecr domain id for your region.

BRANCH_TAG="$(echo $CIRCLE_BRANCH | sed 's|^release/.*|release|' | sed 's|/|-|g')"
ECR_HOST_PREFIX=$ECR_INSTANCE_ID.$ECR_DOMAIN

eval $(aws ecr get-login --region us-east-1)
docker build -t $ECR_HOST_PREFIX/$CIRCLE_PROJECT_REPONAME:$CIRCLE_SHA1 --build-arg GEM_FURY_URL=$GEMFURY_REPO_URL .
docker tag $ECR_HOST_PREFIX/$CIRCLE_PROJECT_REPONAME:$CIRCLE_SHA1 $ECR_HOST_PREFIX/$CIRCLE_PROJECT_REPONAME:$BRANCH_TAG
docker push $ECR_HOST_PREFIX/$CIRCLE_PROJECT_REPONAME:$CIRCLE_SHA1
docker push $ECR_HOST_PREFIX/$CIRCLE_PROJECT_REPONAME:$BRANCH_TAG
