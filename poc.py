from urllib.request import urlopen
from time import sleep


def check_github_repolocation(url):
  resp = urlopen(url)
  return url != resp.geturl(), url, resp.geturl()


def check_github_repos(urls, wait=0.25):
  vulnerable_repos = []
  for url in urls:
    check, _, newurl = check_github_repolocation(url)
    if check:
      vulnerable_repos.append([url, newurl])
    sleep(wait)
  return vulnerable_repos


def print_vulnerable_repos(vulnerable_repos):
  for vulnerable in vulnerable_repos:
    print('{} redirects to {}'.format(*vulnerable))

repos = [
  'https://github.com/aristocrat-merlin/repojack-original',
]

print_vulnerable_repos(check_github_repos(repos))

###
### https://github.com/aristocrat-merlin/repojack-original redirects to https://github.com/aristocrat-merlin/repojack-renamed
###
