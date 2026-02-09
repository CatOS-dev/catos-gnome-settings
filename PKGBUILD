pkgname=catos-gnome-settings
pkgver=2.0
pkgrel=5
pkgdesc="CatOS Gnome Settings"
arch=("any")
depends=('catos-branding')
url="https://www.catos.info/"
license=("GPL")
install="${pkgname}.install"
source=("$pkgname::git+file://$PWD")
sha256sums=("SKIP")

build() {
    cd "$srcdir/$pkgname"
}

package() {
   cd "$srcdir/$pkgname"

    # 安装calamares配置文件
    install -d "$pkgdir/etc"
    install -d "$pkgdir/usr"

    # 复制配置文件（根据实际文件结构调整）
    if [ -d "etc" ]; then
        cp -r etc/* "$pkgdir/etc/"
    fi

    if [ -d "usr" ]; then
        cp -r usr/* "$pkgdir/usr/"
    fi
}
