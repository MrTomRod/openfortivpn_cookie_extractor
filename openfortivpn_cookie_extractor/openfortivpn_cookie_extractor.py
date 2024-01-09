import json
import time
import subprocess
import lz4.block


def load_svpncookies(file):
    with open(file, 'rb') as f:
        start_bytes = f.read(8)
        assert start_bytes == b"mozLz40\0", f"Invalid magic number {start_bytes=}"
        data = json.loads(lz4.block.decompress(f.read()))

    return [
        cookie for cookie in data['cookies']
        if cookie.get('name', '') == 'SVPNCOOKIE'
    ]


def start_openfortivpn(openfortivpn_cmd: str, svpncookie: str):
    cmd = f'{openfortivpn_cmd} --cookie={svpncookie}'
    subprocess.run(cmd, shell=True, text=True)


def connection_loop(browser_cmd: str, openfortivpn_cmd: str, recovery_jsonlz4_file: str, ):
    print(browser_cmd)
    subprocess.run(browser_cmd, shell=True)
    fail_count = 0
    while True:
        svpncookies = load_svpncookies(recovery_jsonlz4_file)
        if svpncookies:
            fail_count = 0
            svpncookie = svpncookies[0]['value']
            start_openfortivpn(openfortivpn_cmd, svpncookie)
            print('Openfortivpn died. Trying again...')
        else:
            fail_count += 1
            print('No cookie found. Sleeping...')

        if fail_count > 10:
            print('Too many failures. Exiting...')
            exit(1)

        time.sleep(5)


def cli(
        browser_cmd: str,
        openfortivpn_cmd: str,
        file: str = '~/.mozilla/firefox/*/sessionstore-backups/recovery.jsonlz4'
):
    """
    This script starts a browser and openfortivpn. It then waits for the browser to create a SVPNCOOKIE and starts openfortivpn with that cookie.

    Example usage:
       openfortivpn_cookie_extractor --browser_cmd 'firefox https://vpn.uni.org/remote/saml/start' --openfortivpn_cmd 'sudo openfortivpn vpn.uni.org --cookie={cookie}'

    :param browser_cmd: Command to start the browser, e.g. 'firefox https://vpn.uni.org/remote/saml/start'
    :param openfortivpn_cmd: Command to start openfortivpn, e.g. 'sudo openfortivpn vpn.uni.org --cookie={cookie}' ({cookie} will be replaced with the actual cookie)
    :param file: Path to recovery.jsonlz4 file, e.g. '~/.mozilla/firefox/someprofile/sessionstore-backups/recovery.jsonlz4'
    """
    import os
    import glob

    found_files = glob.glob(os.path.expanduser(file))
    assert len(found_files) == 1, f'Failed to find {file=}; FILES={found_files}\nPlease specify it as an argument!'
    file = found_files[0]
    print(f'Found recovery.jsonlz4 here: {file}')

    connection_loop(browser_cmd, openfortivpn_cmd, file)


def main():
    from fire import Fire

    Fire(cli)


if __name__ == '__main__':
    main()
