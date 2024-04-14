#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-kblocks
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
Summary:	Single player falling blocks puzzle game
Group:		Games/Arcade
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kblocks/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kblocks/-/archive/%{gitbranch}/kblocks-%{gitbranchd}.tar.bz2#/kblocks-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kblocks-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
KBlocks is the classic falling blocks game.

The idea is to stack the falling blocks to create horizontal lines
without any gaps. When a line is completed it is removed, and more
space is available in the play area. When there is not enough space
for blocks to fall, the game is over.

%files -f kblocks.lang
%{_datadir}/qlogging-categories6/kblocks.categories
%{_bindir}/kblocks
%{_datadir}/applications/org.kde.kblocks.desktop
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
%{_datadir}/knsrcfiles/kblocks.knsrc
%{_datadir}/kblocks
%{_datadir}/config.kcfg/kblocks.kcfg
%{_iconsdir}/hicolor/*/apps/kblocks.*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kblocks-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kblocks --with-html
