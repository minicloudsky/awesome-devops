# CI(持续集成)

[持续集成](https://zh.wikipedia.org/wiki/%E6%8C%81%E7%BA%8C%E6%95%B4%E5%90%88)，简单说就是代码的持续构建和编译、
代码质量检测等业务流程， 在云原生时代，持续集成的核心是将业务代码，通过构建编译，镜像构建，代码安全漏洞检测，sonar代码扫描等流程，
对代码进行质量检测后，打包成一个容器镜像到镜像仓库，供后续应用部署使用。

## 常见持续集成工具

* [Gitlab ci](./gitlab-ci/README.md)
* [Jenkins pipeline](./jenkins-pipeline/README.md)
* [GitHub actions](./github-actions/README.md)
* [Circle ci](https://circleci.com/)

## [各种编程语言的 Dockerfile](./Dockerfile/README.md)
