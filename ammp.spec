Summary:	Simple multimedia player which uses GTK+2
Summary(pl):	Prosta odgrywarka plików multimedialnych
Name:		ammp
Version:	2.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bd3f051d5b6cc221d56d4aec67edf4c3
URL:		http://ammp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple multimedia player which uses GTK+2

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ammp/pixmaps/*
