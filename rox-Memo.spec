%define _name Memo
Summary:	ROX-Memo is a simple alarm clock
Summary(pl.UTF-8):   ROX-Memo jest prostym budzikiem
Name:		rox-%{_name}
Version:	1.9.5
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
# Source0-md5:	65e6106f6551e2a9151dd0f102341a7d
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/Memo
Requires:	python-pygtk-gtk
Requires:	rox >= 2.3
Requires:	rox-Lib2
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Memo is a small utility which you can use to store appointments and 'TODO'
items. It displays the next few entries in a small window, and can also be
instructed to beep and bring up a window with a message later.

%description -l pl.UTF-8
ROX-Memo jest małym narzędziem służącym do przechowywania dat spotkań oraz
listy rzeczy do zrobienia. Program wyświetla, w małym oknie, kilka kolejnych
pozycji. Ponadto może dawać sygnał dźwiękowy lub otworzyć okno z wiadomością.

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_roxdir}/%{_name}/{Help,Messages},%{_desktopdir},%{_pixmapsdir}}

cd %{_name}

install App* *.py .DirIcon Options.xml $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install Messages/it.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages

install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox-Memo.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.py[co]
%{_roxdir}/%{_name}/Help
%dir %{_roxdir}/%{_name}
%dir %{_roxdir}/%{_name}/Messages
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
