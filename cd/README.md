# CD（持续部署）

持续部署是指将软件代码的变化，自动化的交付到对应的环境中，通俗讲就是自动化的实现软件部署流程，在传统的软件开发中，我们通常通过手动方式，或者编写shell
脚本方式，登录对应环境的服务器，修改各种配置文件，然后停止老的服务进程，然后启动新的服务进程实现服务新版本的部署，在云原生时代，对于 k8s 来说，
持续部署就是更新一个工作负载的镜像，将一个 deployment、statefulset、cloneset 等工作负载的镜像进行更新，即可完成新服务的部署。

对于我们常见的一个无状态的服务(例如前端Vue、React项目，或者后端 web 微服务等) 来说，当首次上线时，我们可以在 k8s 集群的对应 namespace 下面，创建它所依赖的 k8s 资源。例如

* Service : 用于服务发现
* ConfigMap: 存储服务的配置信息，例如配置文件等
* Deployment：运行服务的无状态工作负载

当服务首次上线时，我们创建以上依赖的资源，即可完成服务的持续部署；后续部署时，只需要自动化的更新服务的镜像即可，这个发布过程控制，我们可以通过一个后端服务，调用
k8s 相关的 api 实现，也可以通过 GitOps (https://www.gitops.tech/) 方式实现.

完成的无状态服务在 k8s上的部署文档，可以参考这个 demo 项目 [lianjia](https://github.com/minicloudsky/lianjia/tree/master/deploy) 

GitOps 是一种实现云原生应用程序持续部署的方法, 它通过使用开发人员已经熟悉的工具（包括 Git 和持续部署工具），专注于在操作基础设施(例如
Prometheus监控、k8s集群监控、ingress、istio等)时提供以开发人员为中心的体验。 我们通过在 git 仓库中，存储云原生应用期望的状态对应的 yaml 
配置文件，当这些配置文件更新时，我们的 gitops 工具，会自动的轮询监听 我们期望的状态和应用的实际状态，自动将应用的状态更新为我们期望的状态，实现应用的自动部署。

常见的 GitOps 工具有:

* [FluxCd](https://fluxcd.io/flux/)
* [ArgoCd](https://argo-cd.readthedocs.io/en/stable/)
