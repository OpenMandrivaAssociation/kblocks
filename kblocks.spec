Name:		kblocks
Version:	22.08.1
Release:	1
Epoch:		1
Summary:	Single player falling blocks puzzle game
Group:		Games/Arcade
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kblocks/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDEGames)

%description
KBlocks is the classic falling blocks game.

The idea is to stack the falling blocks to create horizontal lines
without any gaps. When a line is completed it is removed, and more
space is available in the play area. When there is not enough space
for blocks to fall, the game is over.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kblocks.categories
%{_bindir}/kblocks
%{_datadir}/applications/org.kde.kblocks.desktop
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
%{_datadir}/knsrcfiles/kblocks.knsrc
%{_datadir}/kblocks
%{_datadir}/config.kcfg/kblocks.kcfg
%{_iconsdir}/hicolor/*/apps/kblocks.*

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
