Name:       sailfishos-disable-glass-avatar

BuildArch: noarch

Summary:    Disable glass avatar
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   voicecall-ui-jolla >= 0.8.22.1

%description
Patch for showing original avatar when calling without glass effect

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-disable-glass-avatar
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-disable-glass-avatar

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-disable-glass-avatar ]; then
/usr/sbin/patchmanager -u sailfishos-disable-glass-avatar || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-disable-glass-avatar ]; then
/usr/sbin/patchmanager -u sailfishos-disable-glass-avatar || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-disable-glass-avatar
