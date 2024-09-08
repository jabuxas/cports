pkgname = "r2modman-plus"
pkgver = "3.1.49"
pkgrel = 0
build_style = ""
hostmakedepends = ["yarn", "nodejs", "python"]
makedepends = []
depends = []
pkgdesc = "Thunderstore mod manager"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/ebkr/r2modmanPlus"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b23119297deda09793760f9962b51bbf8887c1738b9befb99b414573316bc743"
# check takes quite a bit
# options = ["!check", "!cross"]


def prepare(self):
    self.do("yarn", "install", allow_network=True)


def install(self):
    self.install_license("LICENSE")
