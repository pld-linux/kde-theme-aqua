
%define		_theme	aqua

Summary:	Aqua theme
Summary(pl.UTF-8):	Motyw Aqua
Name:		kde-theme-%{_theme}
Version:	3.2
Release:	4
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/153-acqua-3.2.tar.bz2
# Source0-md5:	cd8a0ba106a6ad207e9858832856c23b
Source1:	http://www.ecsis.net/%7Egregday/AQUA-ICONS-07-23-2003.tar.gz
# Source1-md5:	0b1c1e0a8534c652c7f3c15bdd931718
URL:		http://kde-look.org/content/show.php?content=153
# Also:	http://www.kde-look.org/content/show.php?content=5057
Requires:	kdelibs
Requires:	kde-style-%{_theme}
Requires:	kde-decoration-%{_theme}
Requires:	kde-icons-%{_theme}
Requires:	kde-wallpaper-%{_theme}
Requires:	kdm-user-pics-%{_theme}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MacOS-like theme.

%description -l pl.UTF-8
Motyw przypominający MacOS.

%package -n kde-style-%{_theme}
Summary:	Acqua theme
Summary(pl.UTF-8):	Motyw Aqua
Group:		Themes
Requires:	kdelibs
Obsoletes:	kde-theme-acqua
Obsoletes:	kde-theme-Acqua

%description -n kde-style-%{_theme}
MacOS-like theme.

%description -n kde-style-%{_theme} -l pl.UTF-8
Motyw przypominający MacOS.

%package -n kde-icons-%{_theme}
Summary:	KDE icon theme - %{_theme}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_theme}
Group:		Themes
Requires:	kdelibs
Obsoletes:	kde-theme-acqua
Obsoletes:	kde-theme-Acqua

%description -n kde-icons-%{_theme}
The Aqua icon set to end all Aqua icon sets!
Includes over 4,000 icons in sizes from 16x16 to 128x128.

%description -n kde-icons-%{_theme} -l pl.UTF-8
Ten motyw ikon bije wszystkie inne motywy Aquy.
Zawiera ponad 4,000 ikon w rozmiarach od 16x16 do 128x128.

%package -n kde-wallpaper-%{_theme}
Summary:	KDE wallpaper - %{_theme}
Summary(pl.UTF-8):	Tapeta do KDE - %{_theme}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdebase-core
Obsoletes:	kde-theme-acqua
Obsoletes:	kde-theme-Acqua

%description -n kde-wallpaper-%{_theme}
A wallpaper to go with KDE %{_theme} style.

%description -n kde-wallpaper-%{_theme} -l pl.UTF-8
Tapeta pasująca do stylu %{_theme} slicker.

%package -n kde-decoration-%{_theme}
Summary:	Icewm window decoration for kwin - %{_theme}
Summary(pl.UTF-8):	Dekoracja icewm dla kwin - %{_theme}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-%{_theme}
Icewm window decoration for kwin - %{_theme}.

%description -n kde-decoration-%{_theme} -l pl.UTF-8
Dekoracja icewm dla kwin - %{_theme}.

%package -n kdm-user-pics-%{_theme}
Summary:	KDM users pixmaps - %{_theme}
Summary(pl.UTF-8):	Grafiki użytkowników dla KDM - %{_theme}
Group:		Themes
Requires:	kdm
Obsoletes:	kdm-pixmaps-aqua

%description -n kdm-user-pics-%{_theme}
KDM users pixmaps - %{_theme}.

%description -n kdm-user-pics-%{_theme} -l pl.UTF-8
Grafiki użytkowników dla KDM - %{_theme}.

%prep
%setup -q -a1 -n acqua-3.2

%install
install -d $RPM_BUILD_ROOT{%{_datadir}/{wallpapers,apps/{kstyle,kwin/icewm-themes,kdm/pics/users}},%{_iconsdir}/Aqua}

cp -pR {pixmaps,themes}		$RPM_BUILD_ROOT%{_datadir}/apps/kstyle/
cp -pR wallpapers/*		$RPM_BUILD_ROOT%{_datadir}/wallpapers/

cp -pR icewm-themes/Acqua	$RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes

#%{__tar} xfz %{SOURCE1} -C $RPM_BUILD_ROOT%{_iconsdir}
find Aqua -type d -name '.xvpics' \
	-o -type d -name '.thumbnails' | xargs rm -rf

cp -pR Aqua/16x16 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
cp -pR Aqua/22x22 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
cp -pR Aqua/32x32 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
cp -pR Aqua/48x48 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
cp -pR Aqua/64x64 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
cp -pR Aqua/128x128 $RPM_BUILD_ROOT%{_iconsdir}/Aqua
install Aqua/index.desktop $RPM_BUILD_ROOT%{_iconsdir}/Aqua

cp -pR Aqua/kdm/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/

%post
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-style-%{_theme}
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{_datadir}/apps/kstyle/pixmaps/*
%{_datadir}/apps/kstyle/themes/*

%files -n kde-decoration-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n kde-icons-%{_theme}
%defattr(644,root,root,755)
%{_iconsdir}/Aqua

%files -n kde-wallpaper-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/Acqua.jpg

%files -n kdm-user-pics-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/*
