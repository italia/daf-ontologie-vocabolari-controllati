from pathlib import Path
import re
import requests
import pytest
import time

re_url = re.compile(r'[<"]https://github[^>"]*')

def get_urls(glob_path):
  files = Path(".").glob(glob_path)
  for f in files:
    for url in re_url.findall(f.read_text()):
        yield f, url.strip('<">')


@pytest.mark.parametrize('fpath,url', get_urls("VocabolariControllati/**/*.ttl"))
def test_vocab_url(fpath,url):
    # raise NotImplementedError
    if 'deprecated' in fpath.as_posix().lower():
        return
    if 'github.com/italia/daf-ontologie-vocabolari-controllati/issues' in url:
        return

    for i in range(3):
      ret = requests.head(url)
      if ret.status_code == 429:
        time.sleep(int(ret.headers['Retry-After']))
        continue
    assert ret.status_code in (200,301,302)


@pytest.mark.parametrize('fpath,url', get_urls("Ontologie/**/latest/*.ttl"))
def test_onto_url(fpath,url):
    if 'deprecated' in fpath.as_posix().lower():
        return
    if 'github.com/italia/daf-ontologie-vocabolari-controllati/issues' in url:
        return
    for i in range(3):
      ret = requests.head(url)
      if ret.status_code == 429:
        time.sleep(int(ret.headers['Retry-After']))
        continue
    assert ret.status_code in (200,301,302)
