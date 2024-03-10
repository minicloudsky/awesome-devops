# gitlab ci

[gitlab ci](https://docs.gitlab.cn/jh/ci/yaml/gitlab_ci_yaml.html) 通过项目仓库下的 `.gitlab-ci.yml` 配置文件来定义流水线，核心还是定义不同的环境或者代码分支，需要哪些步骤，做哪些代码构建、编译、
镜像构建等操作，也可以在完成操作后，进行持续部署操作，例如通过 docker 命令、kubectl 命令、调用其他api 来更新容器镜像，完成服务的部署。
