Summary:	XSettings Daemon for KDE Environment
Name:     	xsettings-kde
Version:	0.5
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source: 	%{name}-%{version}.tar.bz2
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/xsettings-kde/

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	X11-devel

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.

%prep
%setup -q

%build

make CFLAGS="$RPM_OPT_FLAGS" lib=%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -f xsettings-kde $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/autostart/
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/autostart/xsettings-kde.desktop
[Desktop Entry]
Encoding=UTF-8
Exec=xsettings-kde
Name=XSettings-KDE
X-KDE-autostart-after=kdesktop
Type=Service
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc ChangeLog README
%{_bindir}/*
%{_datadir}/autostart/*

