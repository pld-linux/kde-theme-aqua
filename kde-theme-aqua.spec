%define		_theme	Acqua

Summary:	Acqua theme
Summary(pl):	Temat Acqua
Name:		kde-theme-%{_theme}
Version:	1
Release:	4
License:	GPL
Group:		Themes/Gtk
Source0:	153-Acqua.tar.gz
URL:		http://kde-look.org/content/show.php?content=153
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
MacOS-like theme.

%description -l pl
Temat przypominaj±cy MacOS.

%prep
%setup  -q -n %{_theme}

%build
rm -f missing

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_datadir}/{apps/kstyle,apps/kthememgr/Themes,apps/kwin/icewm-themes},%{_pixmapsdir}}

cp -pR style/{pixmaps,themes}	$RPM_BUILD_ROOT%{_datadir}/apps/kstyle
cp -pR style/wallpapers/*	$RPM_BUILD_ROOT%{_pixmapsdir}

cp -pR theme/Acqua.ktheme	$RPM_BUILD_ROOT%{_datadir}/apps/kthememgr/Themes
cp -pR theme/%{_theme}		$RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes

%post
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kstyle/pixmaps/*
%{_datadir}/apps/kstyle/themes/*
%{_pixmapsdir}/*
%{_datadir}/apps/kthememgr/Themes/*
%{_datadir}/apps/kwin/icewm-themes/*
