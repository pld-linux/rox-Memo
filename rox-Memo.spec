%include  /usr/lib/rpm/macros.python
%define _appsdir /usr/X11R6/share/ROX-apps
%define _name Memo
Summary:	ROX-Memo is a simple alarm clock
Summary(pl.UTF-8):   ROX-Memo jest prostym budzikiem
Name:		rox-%{_name}
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{_name}-%{version}.tgz
URL:		http://rox.sourceforge.net/memo.php3
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-Memo is a small utility which you can use to store appointments and 'TODO'
items. It displays the next few entries in a small window, and can also be
instructed to beep and bring up a window with a message later.

%description -l pl.UTF-8
ROX-Memo jest małym narzędziem służącym do przechowywania dat spotkań oraz
listy rzeczy do zrobienia. Program wyświetla, w małym oknie, kilka kolejnych
pozycji. Ponadto może dawać sygnał dźwiękowy lub otworzyć okno z wiadomością.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

install App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
