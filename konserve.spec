Summary:	Small backup application for the KDE
Summary(pl):	Niewielka aplikacja do kopii zapasowych dla KDE
Name:		konserve
Version:	0.10.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/konserve/%{name}-%{version}.tar.bz2
# Source0-md5:	5ca31d0eb261a52e91a1593b5da3b7be
URL:		http://konserve.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Konserve is a small backup application for the KDE 3.x environment.

%description -l pl
Konserve to niewielka aplikacja do kopii zapasowych dla ¶rodowiska KDE
3.x.

%prep
%setup -q

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_desktopdir}/Applications/konserve.desktop \
        $RPM_BUILD_ROOT%{_desktopdir}/kde

echo "Categories=Qt;KDE;System;" >> \
        $RPM_BUILD_ROOT%{_desktopdir}/kde/konserve.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konserve
%{_datadir}/apps/*
%{_iconsdir}/*/*/*/*
%{_desktopdir}/*
