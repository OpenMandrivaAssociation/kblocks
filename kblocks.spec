Name:		kblocks
Version:	17.03.80
Release:	1
Epoch:		1
Summary:	Single player falling blocks puzzle game
Group:		Games/Arcade
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kblocks/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
KBlocks is the classic falling blocks game.

The idea is to stack the falling blocks to create horizontal lines
without any gaps. When a line is completed it is removed, and more
space is available in the play area. When there is not enough space
for blocks to fall, the game is over.

%files
%doc %{_docdir}/HTML/en/kblocks
%{_bindir}/kblocks
%{_datadir}/applications/org.kde.kblocks.desktop
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
%{_datadir}/kxmlgui5/kblocks/kblocksui.rc
%{_sysconfdir}/xdg/kblocks.knsrc
%{_datadir}/kblocks
%{_datadir}/config.kcfg/kblocks.kcfg
%{_iconsdir}/hicolor/*/apps/kblocks.*




#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
