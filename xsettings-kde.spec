Summary:	XSettings Daemon for KDE Environment
Name:		xsettings-kde
Version:	0.12.3.2
Release:	9
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.xz
URL:		https://abf.rosalinux.ru/mdksoft/xsettings-kde
# (tpg) original source https://quickgit.kde.org/?p=xsettings-kde.git
Patch3:		0003-Enable-PrimaryPaste.patch
Patch4:		0004-Use-Adwaita-instead-of-gnome-as-fallback-icon-theme.patch
Patch5:		0005-Ensure-GTK-scrollbar-clicks-behaviour-behaves-like-Q.patch
Patch6:		0006-add-forgotten-to-previous-commit.patch
Patch7:		0007-Stop-using-deprecated-GSettings-API.patch
Patch11:	0011-Update-website-links-in-README.patch
Patch12:	0012-README-simplify-what-it-works-for.patch
Patch14:	0014-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch15:	0015-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch16:	0016-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.

%prep
%setup -q

cat << EOF > xsettings-kde.desktop
[Desktop Entry]
Exec=xsettings-kde
Name=XSettings-KDE
X-KDE-autostart-after=kdesktop
X-KDE-autostart-phase=1
Type=Service
OnlyShowIn=KDE;
EOF

%apply_patches

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" lib=%{_lib}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 xsettings-kde %{buildroot}%{_bindir}/xsettings-kde

mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
install -m 644 xsettings-kde.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/xsettings-kde.desktop

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/xsettings-kde.desktop
