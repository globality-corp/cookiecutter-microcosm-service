FROM 308798440167.dkr.ecr.us-east-1.amazonaws.com/python-service:master

ARG GEM_FURY_URL

# We are {{cookiecutter.project_name}}
ENV NAME {{cookiecutter.project_name}}
LABEL service-type="python-service"
LABEL uses-postgres="true"

# Copy top-level files and install dependencies
COPY MANIFEST.in README.md setup.cfg setup.py /src/
RUN pip install --extra-index-url $GEM_FURY_URL .

# Copy source and reinstall
COPY $NAME /src/$NAME/
RUN rm -rf /src/$NAME/tests
RUN pip install -U -e .
