Summary:	XSettings Daemon for KDE Environment
Name:     	xsettings-kde
Version:	0.11
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/KDE
Source: 	%{name}-%{version}.tar.bz2
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/xsettings-kde/

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libx11-devel glib2-devel

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.

%prep
%setup -q

%build

make CFLAGS="%optflags" LDFLAGS="%ldflags" lib=%{_lib}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
cp -f xsettings-kde %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/autostart/
cat << EOF > %{buildroot}%{_datadir}/autostart/xsettings-kde.desktop
[Desktop Entry]
Encoding=UTF-8
Exec=xsettings-kde
Name=XSettings-KDE
X-KDE-autostart-after=kdesktop
Type=Service
OnlyShowIn=KDE;
EOF

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc ChangeLog README
%{_bindir}/*
%{_datadir}/autostart/*

