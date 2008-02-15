Summary:	Small backup application for the KDE
Summary(pl.UTF-8):	Niewielka aplikacja do kopii zapasowych dla KDE
Name:		konserve
Version:	0.10.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/konserve/%{name}-%{version}.tar.bz2
# Source0-md5:	04260394e62d799957002262d2efb9e6
URL:		http://konserve.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konserve is a small backup application for the KDE 3.x environment.

%description -l pl.UTF-8
Konserve to niewielka aplikacja do kopii zapasowych dla środowiska KDE
3.x.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/konserve.desktop \
        $RPM_BUILD_ROOT%{_desktopdir}/kde

echo "Categories=Qt;KDE;System;" >> \
        $RPM_BUILD_ROOT%{_desktopdir}/kde/konserve.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/konserve
%{_datadir}/apps/* # specify excplicit dirs here (to avoid packaging kde dirs)
%{_iconsdir}/hicolor/*/apps/konserve.png
%{_desktopdir}/kde/*.desktop
