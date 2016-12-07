# $ marathon-cli_

* [Setup](#setup)
* [Usage](#usage)
* [Examples](#examples)

---

<a name="setup" id="setup"></a>

## Setup

* `pip install marathon-cli`
* Set the following environment variables:
  - `MARATHON_URL`
  - `MARATHON_USER`
  - `MARATHON_PASSWORD`
* view the usage with `marathon --help`


<a name="usage" id="usage"></a>

## Usage

````
Usage: marathon [OPTIONS] COMMAND [ARGS]...

  cli helpers for the marathon api.

Options:
  --version   print the installed version and exit
  -h, --help  Show this message and exit.

Commands:
  app-ids           Get the ids of all apps deployed to a marathon instance.
  app-tasks         Get app tasks.
  app-versions      Get app versions.
  apps              Get apps deployed to a marathon instance.
  delete-app        Destroy app.
  delete-app-tasks  Kill app tasks.
  delete-tasks      Delete specified task ids.
  deployments       List all running deployments.
  groups            Get the group with all applications and all transitive child groups.
  info              Get info about the Marathon Instance.
  leader            Returns the current leader.
  metrics           Get metrics data from this Marathon instance.
  ping              Ping this Marathon instance.
  plugins           Returns the list of all loaded plugins.
  put-app           Update or create an app with id.
  queue             List all the tasks queued up or waiting to be scheduled.
  raw               Call the given uri.
  restart-app       Restart app.
  tasks             Get all running tasks.
````

---

<a name="examples" id="examples"></a>

## Examples

#### See apps

```bash
marathon apps
# pickle the object and save to a file for debugging or testing
marathon apps --pickle the-app-id
```

#### Create or update an app

Example app template:

```json
{
  "id": "/{{ app_id }}",
  "container": {
    "docker": {
      "forcePullImage": true,
      "image": "{{ ecr_image }}",
      "network": "BRIDGE",
      "portMappings": [
        {
          "containerPort": 8000
        }
      ]
    },
    "type": "DOCKER"
  },
  "env": {
    "VERSION": "{{ VERSION }}",
    "PROJECT_KEY": "{{ PROJECT_KEY }}",
    "APP_ENV": "{{ app_env }}",
    "AWS_REGION": "{{ AWS_REGION|default('us-east-1') }}"
  },
  "ports": [
    8000
  ]
}
```

The command to create or update the app:

```bash
marathon put-app [--pickle] [--dry-run] {app-id} {template-file} {variable-map}
```

```bash
marathon put-app --pickle my-app example.json.j2 \
    ecr_image=repo/image \
    app_env=dev \
    env=AWS_REGION \
    file=VERSION
```

**Variable map types/functions**

Pattern                | template var name | Description
-----------------------|-------------------|--------------------------
`variable_name=value`  | `variable_name`   | key/value
`env_var=VAR_NAME`     | `VAR_NAME`        | pass the value of the environment variable as the value
`file=filename`        | `filename`        | get the contents of `filename` and strip newlines
