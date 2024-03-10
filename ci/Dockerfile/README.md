# Dockerfile

不同的编程语言，需要不同的 `Dockerfile`，根据每个语言生成 docker 镜像的方式，你可以根据需求自定义修改构建阶段的操作。在标准的 Kubernetes 集群中，
由于没有 docker 守护进程，同时考虑到安全性，我们需要在用户空间进行镜像构建，我们可以选择 [kaniko](https://github.com/GoogleContainerTools/kaniko)
进行镜像构建。

## 镜像构建

### docker 镜像构建
```shell
docker build -t IMAGE-NAME:TAG .
```

### Kubernetes 上基于 [kaniko](https://github.com/GoogleContainerTools/kaniko) 构建
```shell
kaniko --dockerfile=./Dockerfile --context=./ --destination=IMAGE-NAME --snapshotMode=redo --ignore-path=/var/mail --ignore-path=/var/spool/mail
```

### [前端项目 nginx 配置](./nginx_conf/README.md)