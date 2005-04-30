%define _name Memo
Summary:	ROX-Memo is a simple alarm clock
Summary(pl):	ROX-Memo jest prostym budzikiem
Name:		rox-%{_name}
Version:	1.9.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
# Source0-md5:	65e6106f6551e2a9151dd0f102341a7d
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/Memo
Requires:	python-pygtk-gtk
Requires:	rox >= 2.2.0-2
Requires:	rox-Lib2
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Memo is a small utility which you can use to store appointments and 'TODO'
items. It displays the next few entries in a small window, and can also be
instructed to beep and bring up a window with a message later.

%description -l pl
ROX-Memo jest ma³ym narzêdziem s³u¿±cym do przechowywania dat spotkañ oraz
listy rzeczy do zrobienia. Program wy¶wietla, w ma³ym oknie, kilka kolejnych
pozycji. Ponadto mo¿e dawaæ sygna³ d¼wiêkowy lub otworzyæ okno z wiadomo¶ci±.

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appsdir}/%{_name}/{Help,Messages},%{_desktopdir},%{_pixmapsdir}}

cd %{_name}

install App* *.py .DirIcon Options.xml $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install Messages/it.gmo $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages

install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox-Memo.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
%dir %{_appsdir}/%{_name}/Messages
%lang(it) %{_appsdir}/%{_name}/Messages/it.gmo
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
