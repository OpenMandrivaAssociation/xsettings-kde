Summary:	XSettings Daemon for KDE Environment
Name:     	xsettings-kde
Version:	0.12.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Source: 	%{name}-%{version}.tar.bz2
URL:		http://svnweb.mageia.org/soft/theme/xsettings-kde/

BuildRequires:	pkgconfig(x11) pkgconfig(glib-2.0)

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
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -f xsettings-kde $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/autostart/
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/autostart/xsettings-kde.desktop
[Desktop Entry]
Exec=xsettings-kde
Name=XSettings-KDE
X-KDE-autostart-after=kdesktop
Type=Service
OnlyShowIn=KDE;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc ChangeLog README
%{_bindir}/*
%{_datadir}/autostart/*





%changelog

* Fri Oct 07 2011 dmorgan <dmorgan> 0.12.3-1.mga2
+ Revision: 152570
- RFE: Gtk/IMModule support (RHBZ#727822)
  Patch from Fedora

* Sat May 07 2011 mikala <mikala> 0.12.2-1.mga1
+ Revision: 95726
- Update tarball to 0.12.2 :
 -add a patch for lmenut to use upstream [General]ColorScheme (mga #900)

* Sat Mar 19 2011 dmorgan <dmorgan> 0.12.1-1.mga1
+ Revision: 74526
- New upstream version 0.12.1
  Remove Encoding from desktop file
- Fix URL of the upstream project

* Mon Feb 07 2011 dmorgan <dmorgan> 0.12-1.mga1
+ Revision: 48482
- New version 0.12

* Thu Feb 03 2011 dmorgan <dmorgan> 0.11-4.mga1
+ Revision: 46543
- imported package xsettings-kde


* Wed Dec 22 2010 Funda Wang <fwang@mandriva.org> 0.11-4mdv2011.0
+ Revision: 623787
- tighten BR

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-3mdv2011.0
+ Revision: 608241
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-2mdv2010.1
+ Revision: 524468
- rebuilt for 2010.1

* Wed Aug 19 2009 Frederic Crozat <fcrozat@mandriva.com> 0.11-1mdv2010.0
+ Revision: 417978
- Release 0.11 :
 - Fix colors when using Ia_Ora-KDE (Mdv bug #52740) (rodrigo)

* Thu Mar 26 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10-1mdv2009.1
+ Revision: 361392
- Release 0.10 :
 - enable icon in button under KDE4
 - drop DPI settings if they are not set in KDE (Guido G?\195?\188nther)
 - use glib mainloop (Guido G?\195?\188nther)

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.9-2mdv2009.1
+ Revision: 350767
- rebuild

* Mon Sep 29 2008 Frederic Crozat <fcrozat@mandriva.com> 0.9-1mdv2009.0
+ Revision: 289732
- Release 0.9 :
 - fix colorscheme support for KDE4

* Fri Sep 05 2008 Frederic Crozat <fcrozat@mandriva.com> 0.8-1mdv2009.0
+ Revision: 281344
- Release 0.8 :
 - add support for KDE4
 - add support for DPI settings in KDE
 - switch file selector to GIO

* Fri Jul 04 2008 Frederic Crozat <fcrozat@mandriva.com> 0.7-3mdv2009.0
+ Revision: 231793
- Fix autostart file to be only valid for KDE

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2009.0
+ Revision: 226082
- rebuild

* Fri Feb 08 2008 Frederic Crozat <fcrozat@mandriva.com> 0.7-1mdv2008.1
+ Revision: 164244
- Release 0.7 :
 - don't set GTK theme using XSettings if KDE did it itself
 - fix memleak

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 26 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6-1mdv2008.0
+ Revision: 93073
- Release 0.6 :
 -failover correctly when some configuration files aren't present

* Fri Sep 21 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5-1mdv2008.0
+ Revision: 91946
- Release 0.5
 - handle multiple kde profiles specified as prefixes

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 0.4-2mdv2008.0
+ Revision: 76611
- rebuild for 2008
- don't package COPYING
- Import xsettings-kde



* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4-1mdv2007.0
- Release 0.4 :
 * change theme according to color scheme for Ia Ora (Mdv bug #25574)
 * fix theme detection
 * support kde profile
 * don't change theme if ~/.gtkrc-2.0 exists

* Mon Mar 06 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdk
- Release 0.3 :
 - support Net/FallbackIconTheme, fix Mdk bug #19441)

* Thu Aug 25 2005 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdk 
- Release 0.2 :
 - force gnome-vfs gtk2 file selector backend

* Wed Jul 27 2005 Frederic Crozat <fcrozat@mandriva.com> 0.1-1mdk 
- Initial package
