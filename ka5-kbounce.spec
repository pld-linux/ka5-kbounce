#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kbounce
Summary:	Kbounce
Name:		ka5-%{kaname}
Version:	22.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d9177cb6c3aa80b279940966f416b36a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBounce is a single player arcade game with the elements of puzzle. It
is played on a field, surrounded by wall, with two or more balls
bouncing around within the walls. The object of the game is to build
new walls to decrease the size of the active field.

%description -l pl.UTF-8
KBounce jest jednoosobową grą zręcznościową z elementami zagadki. Jest
rozgrywana na polu otoczonym ścianami, z dwoma lub więcej piłkami
odbijającymi się od ścian. Celem gry jest budowanie nowych ścian, żeby
zmniejszać rozmiar aktywnego pola gry.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_desktopdir}/org.kde.kbounce.desktop
%{_iconsdir}/hicolor/128x128/apps/kbounce.png
%{_iconsdir}/hicolor/16x16/apps/kbounce.png
%{_iconsdir}/hicolor/22x22/apps/kbounce.png
%{_iconsdir}/hicolor/32x32/apps/kbounce.png
%{_iconsdir}/hicolor/48x48/apps/kbounce.png
%{_iconsdir}/hicolor/64x64/apps/kbounce.png
%{_datadir}/kbounce
%{_datadir}/metainfo/org.kde.kbounce.appdata.xml
%{_datadir}/qlogging-categories5/kbounce.categories
