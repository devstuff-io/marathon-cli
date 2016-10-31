# $ marathon-cli_

## Install

* `pip install -e git+git://github.com/meganlkm/marathon-cli.git#egg=marathon-cli`
* Set the following environment variables:

  - MARATHON_URL
  - MARATHON_USER
  - MARATHON_PASSWORD

* view the usage with `marathon --help`


### Examples

#### See apps

```bash
marathon apps
# pickle the object and save to a file for debugging or testing
marathon apps --pickle the-app-id
```

#### Create or update an app

```bash
marathon put-app --pickle --dry-run the-app-id app.json.j2 \
    foo=bar \
    env=AWS_ACCOUNT_ID \
    env=APP_ENV \
    file=VERSION
```
