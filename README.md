# cric

cric (**C**onvert **R**aw cookies to **I**mportable browser **C**ookies) converts raw cookies to a browser importable format. It was initially developed to convert cookies retrieved from [XSSHunter](https://xsshunter.com) to an importable format.

Currently, only two browsers (Chrome and Firefox) are supported and are both referenced in [template.json](https://github.com/sawzeeyy/cric/blob/master/template.json). You may make changes to the file to suit your purpose.

# Installation
```
$ git clone https://github.com/sawzeeyy/cric.git
$ cd cric
```

### Additional for Linux users
```
ln -s ~/FULL_PATH/cric.py /usr/local/bin/cric
```

Then you can run directly using

```
$ cric
```

# Usage
```
python3 cric.py [-h] -d DOMAIN -i INPUT [-t TIMESTAMP] [-o OUTPUT] [-b BROWSER]
```

| Short        | Long           | Description  |
| ------------- |-------------| -----|
| -d | --domain | Domain name(s) or text file containing a list of domains |
| -i | --input | Text file containing the raw cookies |
| -t | --timestamp | The time the cookie will expire (Default: 4724524800) |
| -o | --output | JSON file containing the browser importable cookies (Default: domain.json) |
| -b | --browser | Name of browser to use its cookie format (Default: chrome) |


### Examples
- List all options and switches
```
python3 cric.py -h
```

- Basic Usage
```
python3 cric.py -d website.com -i cookies.txt
```

- Specify multiple domains

```
python3 cric.py -d website.com,website.net -i cookies.txt
```

OR

```
python3 cric.py -d website.txt -i cookies.txt
```
where website.txt contains the domains


- Specify timestamp
```
python3 cric.py -d website.com -i cookies.txt -t 1568851200
```

- Specify browser
```
python3 cric.py -d website.com -i cookies.txt -b firefox
```

- Specify output
```
python3 cric.py -d website.com -i cookies.txt -o website_cookies.json
```

- Using all options

```
python3 cric.py -d website.com -i cookies.txt -t 1568851200 -b firefox -o website_cookies.json
````
# License

cric is licensed under the GNU GPL v3, take a look at the [license](/LICENSE) for more information.

# Want to Contribute?
This was made to suit my purpose but yours may be different. Any pull requests are very much appreciated!