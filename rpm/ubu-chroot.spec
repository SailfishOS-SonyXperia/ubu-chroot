Name:       ubu-chroot
Summary:    Minimal set of android tools
Version:    1.0
Release:    1
Group:      Tools
License:    GPL
Source0:    ubuntu-focal-20210531-android-rootfs.tar.bz2
Source1:    %{name}-%{version}.tar.bz2
Provides:   ubu-trusty
Obsoletes:  ubu-trusty
Requires(post): bzip2
Requires(post): coreutils
Requires(post): tar


%description
ubu-trusty for Mer


%prep
%setup -q -T -b 1 -c

%build

%install
mkdir -p %{buildroot}/srv/mer/sdks/ubu
# ln instead of cp/mv to avoid removing src
ln %{SOURCE0} %{buildroot}/srv/mer/sdks

%post
tar --numeric-owner -xjf /srv/mer/sdks/%(basename %{SOURCE0}) -C /srv/mer/sdks/ubu && rm /srv/mer/sdks/%(basename %{SOURCE0})

%files
%defattr(-,root,root,-)
/srv/mer/sdks/*
