You need to write a simple API over http which takes as input a __file__, containing runtime logs from a CI of the form:

```
GOCACHE=off go test -timeout 20m -v${WHAT:+ -run="$WHAT"} ./test/e2e/
[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1/register.go:28 0
[ 0]EXIT:   /usr/local/src/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go:28 0
[ 0]ENTER:  /usr/local/src/github.com/openshift/machine-config-operator/pkg/generated/clientset/versioned/scheme/register.go:19 0
[ 0]ENTER:  /usr/local/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go:32         addKnownTypes
[ 0]EXIT:   /usr/local/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go:32         addKnownTypes
[ 0]EXIT:   /usr/local/src/golang/src/github.com/openshift/machine-config-operator/pkg/generated/clientset/versioned/scheme/register.go:19 0
=== RUN   TestMCDToken
 10 [ 1]ENTER:  /usr/local/src/github.com/openshift/machine-config-operator/test/e2e/mcd_test.go:21 TestMCDToken
 11 [ 0]ENTER:  /usr/local/src/github.com/openshift/machine-config-operator/cmd/common/client_builder.go:34 NewClientBuilder
 12 [ 0]EXIT:   /usr/local/src/github.com/openshift/machine-config-operator/cmd/common/client_builder.go:34 NewClientBuilder
 13 [ 0]ENTER:  /usr/local/src/github.com/openshift/machine-config-operator/cmd/common/client_builder.go:22 KubeClientOrDie
 14 [ 0]EXIT:   /usr/local/src/github.com/openshift/machine-config-operator/cmd/common/client_builder.go:22 KubeClientOrDie
 15 [ 1]EXIT:   /usr/local/src/github.com/openshift/machine-config-operator/test/e2e/mcd_test.go:21 TestMCDToken
 16 --- PASS: TestMCDToken (3.86s)
```
Your module should parse the file and return through the API a JSON of the form given below:

```json
{
  "result": [{
    "operation": "ENTRY",
    "filename": "/usr/local/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
    "line_number": 32,
    "name": "addKnownTypes"
  },
  {
    "operation": "EXIT",
    "filename": "/usr/local/src/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
    "line_number": 28,
    "name": "anonymous"
  }]
}
```

"name" is "anonymous" wherever you encounter an invalid function name(like '0' in the above logs). A valid function name follows the following rule: `must begin with (unicode_letter or _), and can end with many (unicode_letter, unicode_digit or _)`.

In addition to this, feel free to do the following for bonus points (we would prefer you to do at least one of these activities):

* Design an OpenAPI 2.0 (swagger) spec for this API
* Write a Dockerfile to pack your code inside a container
* Add logic to your source to make it scale better under high load (concurrency/parallelism/threading etc.) such that it is able to accept more than two files through the API and process them simultaneously.

Extra points for designing your code well through your knowledge of OOP/design patterns and adding some basic comments wherever required.

On compeleting your solution push either to a private Github repo or gist and add us(@rhdev-analytics-interviews
) as a contributor so I can see it for grading purposes or send us a tarball of your code. I would prefer if you can include a one pager design document explaining your design choices so we know the solution is not plagiarised.