Name:		kblocks
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Single player falling blocks puzzle game
Group:		Games/Arcade
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kblocks/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)

%description
KBlocks is the classic falling blocks game.

The idea is to stack the falling blocks to create horizontal lines
without any gaps. When a line is completed it is removed, and more
space is available in the play area. When there is not enough space
for blocks to fall, the game is over.

%files
%{_kde_bindir}/kblocks
%{_kde_applicationsdir}/kblocks.desktop
%{_kde_appsdir}/kblocks
%{_kde_datadir}/config.kcfg/kblocks.kcfg
%{_kde_configdir}/kblocks.knsrc
%{_kde_docdir}/HTML/en/kblocks
%{_kde_iconsdir}/hicolor/*/apps/kblocks.*

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
