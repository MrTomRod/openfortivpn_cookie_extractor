# openfortivpn_cookie_extractor

This Python script is a workaround for the University of Bern's VPN service (univpn.unibe.ch) which does not support Linux. It uses the Firefox sessionstore-backups to extract the SVPNCOOKIE and then
starts openfortivpn with the cookie.

The script runs in an infinite loop and tries to connect every 5 seconds. If the connection fails, it tries again.

## Requirements

- Python 3.6 or higher
- pip install lz4 fire
- On Firefox's about:config, set `browser.privatebrowsing.autostart` to false
- On Firefox's about:config, set `privacy.sanitize.pending` to false
- Add this to visudo: `USERNAME ALL=(ALL:ALL) NOPASSWD: /usr/bin/openfortivpn` (replace `USERNAME` with your username)

## Installation

To install this package, run the following command:

```bash
pipx install git+https://github.com/MrTomRod/openfortivpn_cookie_extractor
```

## Usage

To use this script, run something like the following command:

```bash
vpn \
--browser_cmd 'firefox https://univpn.unibe.ch/remote/saml/start --cookie={cookie}' \
--openfortivpn_cmd 'sudo openfortivpn univpn.unibe.ch'
```

You can also specify the path to the `recovery.jsonlz4` file if you have multiple Firefox profiles:

```bash
vpn \
--browser_cmd 'firefox https://univpn.unibe.ch/remote/saml/start --cookie={cookie}' \
--openfortivpn_cmd 'sudo openfortivpn univpn.unibe.ch' \
--file='~/.mozilla/firefox/some-profile-id/sessionstore-backups/recovery.jsonlz4'
```

## Acknowledgements

This project was inspired by [fuckForticlient](https://github.com/nonamed01/fuckForticlient/).
