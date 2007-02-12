Summary:	Simple multimedia player which uses GTK+2
Summary(pl.UTF-8):   Prosta odgrywarka plików multimedialnych
Name:		ammp
Version:	2.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/ammp/%{name}-%{version}.tar.gz
# Source0-md5:	bd3f051d5b6cc221d56d4aec67edf4c3
Source1:	%{name}.desktop
URL:		http://ammp.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	smpeg-devel >= 0.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple multimedia player which uses GTK+2.

%description -l pl.UTF-8
Prosty odtwarzacz plików multimedialnych używający GTK+2.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install pixmaps/logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ammp
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
