Summary:	XSettings Daemon for KDE Environment
Name:		xsettings-kde
Version:	0.12.3.2
Release:	6
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.xz
URL:		https://abf.rosalinux.ru/mdksoft/xsettings-kde
# (tpg) original source https://quickgit.kde.org/?p=xsettings-kde.git
Patch2:		0003-Enable-PrimaryPaste.patch
Patch3:		0004-Use-Adwaita-instead-of-gnome-as-fallback-icon-theme.patch
Patch4:		0005-Ensure-GTK-scrollbar-clicks-behaviour-behaves-like-Q.patch
Patch5:		0006-add-forgotten-to-previous-commit.patch
Patch6:		0007-Stop-using-deprecated-GSettings-API.patch
# (tpg) Patch 7, 8 and 9 are not needed
#Patch7:		0008-Stop-using-deprecated-GLib-API.patch
#Patch8:		0009-Convert-to-autotools-and-add-xsettings-kde.desktop-f.patch
#Patch9:		0010-ChangeLog-is-auto-generated-since-git.patch
Patch10:	0011-Update-website-links-in-README.patch
Patch11:	0012-README-simplify-what-it-works-for.patch
# (tpg) patch 12 is not needed
#Patch12:	0013-Remove-i18n-and-documentation-macros-as-it-is-not-us.patch
Patch13:	0014-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch14:	0015-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch15:	0016-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" lib=%{_lib}

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/autostart/%{name}.desktop
