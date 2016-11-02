# $ marathon-cli_

## Install

* `pip install marathon-cli`
* Set the following environment variables:
  - `MARATHON_URL`
  - `MARATHON_USER`
  - `MARATHON_PASSWORD`
* view the usage with `marathon --help`


### Examples

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
