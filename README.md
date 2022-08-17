# Salmorejo

Salmorejo is a command line tool which will help you to run your own Python scripts in order to test, debug and/or analyze the status of your Kubernetes cluster in real time.

> Salmorejo is under heavy development

## How does it work?

Salmorejo will connect to your "current-connected" Kubernetes cluster (check `$ kubectl cluster-info`) and it will received changes in the desired objects. These events will be forwarded to your custom Python script.

Your python script must contain a function call `callback` which has the argument `event`. Every event will contain 3 main fields:

* 'type': The type of event such as "ADDED", "DELETED", etc.
* 'raw_object': a dict representing the watched object.
* 'object': A model representation of raw_object. The name of
            model will be determined based on
            the func's doc string. If it cannot be determined,
            'object' value will be the same as 'raw_object'.

> Event information has been defined by the [kubernetes library](https://github.com/kubernetes-client/python).

## Supported Objects

Currently, Salmorejo supports:

* Configmaps ("configmap", "configmaps", "cm")
* Daemonsets ("daemonset", "daemonsets", "ds")
* Deployments ("deployments", "deployment")
* Ingresses ("ingress", "ingresses", "ing")
* Pods ("pods", "pod", "po")
* Secrets ("secret", "secrets")
* Services ("services", "service", "svc")
* Statefulsets  ("statefulset", "statefulsets", "sts")

## Installation

### From Pypi

```bash
$ python -m pip install salmorejo
```

### From Code

```bash
$ python -m pip install -e .
```

## How to use it?

### CLI

```bash
$ salmorejo watch <python script path> <comma-separated-list of kubernetes objects>
```

### From Code repository

```bash
$ python main.py watch <python script path> <comma-separated-list of kubernetes objects>
```

### Example

```bash
$ salmorejo watch ./scripts/counter.py pod,svc,deployments

+------------+--------------------+-------+
|    KIND    |     NAMESPACE      | COUNT |
+------------+--------------------+-------+
|  Service   |      default       |   2   |
+------------+--------------------+-------+
| Deployment |    kube-system     |   1   |
+------------+--------------------+-------+
|    Pod     |    kube-system     |   8   |
+------------+--------------------+-------+
| Deployment | local-path-storage |   1   |
+------------+--------------------+-------+
|  Service   |    kube-system     |   1   |
+------------+--------------------+-------+
|    Pod     | local-path-storage |   1   |
+------------+--------------------+-------+
|    Pod     |      default       |   4   |
+------------+--------------------+-------+
```

### Examples

Examples of Scripts can be found under [here](./scripts/)


## Why Python

Although [Go](https://go.dev/) is the lingua franca to code against Kubernetes, [Python](https://go.dev/) could be considered the most used programming language by SysAdmins, SREs or Platform Engineers. Salmorejo was thought for this kind of people, and we hope that they enjoy it.

## What actually is Salmorejo?

Salmorejo is a traditional Andalusian food, originally from Córdoba. [Wiki](https://en.wikipedia.org/wiki/Salmorejo).
