%define name	rxp
%define version	1.4.8
%define rel	3
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XML parser
Group:		Development/Other
License:	GPL
URL:		http://www.cogsci.ed.ac.uk/~richard/rxp.html
Source:		ftp://ftp.cogsci.ed.ac.uk/pub/richard/%{name}-%{version}.tar.bz2
Patch:		%{name}.makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
RXP is a validating XML parser written in C. It is used by the LT XML toolkit,
and the Festival speech synthesis system.

%prep
%setup
%patch

%build
export CFLAGS=$RPM_OPT_FLAGS
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYRIGHT Manual Threads
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


