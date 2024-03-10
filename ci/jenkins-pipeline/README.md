# Jenkins 流水线

参考: [Jenkins 流水线](https://www.jenkins.io/zh/doc/book/pipeline/)

在运维开发自动化中，持续集成通常使用 Jenkins 来实现应用的镜像构建，通过调用 jenkins api，创建 jenkins 流水线 job，
我们可以通过定义 Jenkins 流水线的 Jenkinsfile，定义流水线的执行步骤，在每个 step 中，执行对应的操作，例如拉取 gitlab 项目代码，
项目代码构建，编译，sonar 代码扫描，以及其他的代码质量检测等，然后根据项目语言类型，生成对应的 Dockerfile，通过 docker 或者 kaniko 进行镜像构建，将构建好的镜像，
上传到 docker hub 或者内部的 harbour 镜像仓库，即可完成代码持续集成流程。

Jenkins agent 作为每个 job 执行环境，我们可以通常选择服务器本身，也可以选择 k8s pod，当需要执行 job 运行 ci 任务时，创建一个 pod 执行
任务，执行完成以后删除 job 所在的 pod ，参考 
* [jenkins kubernetes plugin](https://plugins.jenkins.io/kubernetes/)
* [阿里云 ECI 弹性容器调度](https://help.aliyun.com/zh/eci/product-overview/scenarios)