%define name	rxp
%define version	1.4.8
%define rel	5
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XML parser
Group:		Development/Other
License:	GPL
URL:		https://www.cogsci.ed.ac.uk/~richard/rxp.html
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




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.8-5mdv2011.0
+ Revision: 614800
- the mass rebuild of 2010.1 packages

* Tue Mar 16 2010 Eric Fernandez <zeb@mandriva.org> 1.4.8-4mdv2010.1
+ Revision: 520721
- rebuild

* Wed May 06 2009 Eric Fernandez <zeb@mandriva.org> 1.4.8-3mdv2010.0
+ Revision: 372594
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.4.8-2mdv2009.0
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Eric Fernandez <zeb@mandriva.org> 1.4.8-2mdv2008.0
+ Revision: 60305
-rebuild


* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 1.4.8-1mdv2007.0
+ Revision: 99889
- 1.4.8
- Import rxp

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon.org.uk> 1.4.7-1mdv2007.0
- new release
- use mkrel

* Sat Aug 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-2mdk
- rebuild 
- spec cleanup

* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.4.0-1mdk 
- 1.4.0 final
- rpmbuildupdate aware

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.4.0-0.pre10.1mdk
- new version

