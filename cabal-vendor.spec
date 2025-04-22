Name: cabal-vendor

Version: 1.0.0
Release: alt1

Summary: tool for vendoring dependencies of cabal package
License: BSD-3-Clause
Group: Development/Haskell

URL: https://github.com/lRespublica/cabal-vendor
VCS: https://github.com/lRespublica/cabal-vendor.git

Source: %name-%version.tar

Source9: README
Source10: LICENSE

BuildArch: noarch

Requires: cabal-install

%description
Cabal-vendor sets up a local repo with cabal package dependencies

Useful for vendoring and local builds (with rpm-build-haskell-vendored)

%prep
%setup

%install
install -pm 755 -D -t %buildroot/%_bindir cabal-vendor
cp -t . %SOURCE9 %SOURCE10

%files
%doc README LICENSE
%_bindir/cabal-vendor

%changelog
