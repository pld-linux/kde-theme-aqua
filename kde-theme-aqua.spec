%define		_theme	acqua

Summary:	Acqua theme
Summary(pl):	Motyw Acqua
Name:		kde-theme-%{_theme}
Version:	1
Release:	4.5
License:	GPL
Group:		Themes/Gtk
Source0:	http://www.kde-look.org/content/files/153-Acqua.tar.gz
# Source0-md5:	3d8976d51710df0296c074ee9fa7112e
Source1:	http://www.ecsis.net/%7Egregday/AQUA-ICONS-07-23-2003.tar.gz
# Source1-md5:	0b1c1e0a8534c652c7f3c15bdd931718
URL:		http://kde-look.org/content/show.php?content=153
Requires:	kdelibs
Obsoletes:	kde-theme-Acqua
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
MacOS-like theme.

%description -l pl
Motyw przypominający MacOS.

%prep
%setup  -q -n Acqua

%build
rm -f missing

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_datadir}/{apps/kstyle,apps/kthememgr/Themes,apps/kwin/icewm-themes},%{_iconsdir}}

cp -pR style/{pixmaps,themes}	$RPM_BUILD_ROOT%{_datadir}/apps/kstyle
cp -pR style/wallpapers/*	$RPM_BUILD_ROOT%{_iconsdir}

cp -pR theme/Acqua.ktheme	$RPM_BUILD_ROOT%{_datadir}/apps/kthememgr/Themes
cp -pR theme/Acqua		$RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes

%{__tar} xfz %{SOURCE1} -C $RPM_BUILD_ROOT%{_iconsdir}

%post
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe ChangeLog
%{_datadir}/apps/kstyle/pixmaps/*
%{_datadir}/apps/kstyle/themes/*
%{_iconsdir}/*
%{_datadir}/apps/kthememgr/Themes/*
%{_datadir}/apps/kwin/icewm-themes/*
