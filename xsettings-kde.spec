Summary:	XSettings Daemon for KDE Environment
Name:     	xsettings-kde
Version:	0.12.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0: 	%{name}-%{version}.tar.bz2
URL:		https://abf.rosalinux.ru/moondrake/xsettings-kde

BuildRequires:	pkgconfig(x11) pkgconfig(glib-2.0)

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" lib=%{_lib}

%install
%makeinstall_std

%files 
%doc ChangeLog README
%{_bindir}/*
%{_datadir}/autostart/*
