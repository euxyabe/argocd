FROM python:3.13-alpine AS page-builder

WORKDIR /app

ARG PAGE_TITLE="Nginx Demo"
ARG PAGE_MESSAGE="Deployed by GitHub Actions, ECR, Argo CD, and EKS."
ARG GIT_SHA="local"
ARG GITHUB_RUN_NUMBER="local"
ARG BUILD_TIME="local"

COPY index.html.template render_index.py ./

RUN python render_index.py

FROM nginx:1.27-alpine

COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=page-builder /app/index.html /usr/share/nginx/html/index.html
