%define		version		2.5
%define		codename	haiku
%define		reldate		20080327
%define		fullversion	%{version}%{?codename:-%codename}%{?reldate:-%reldate}

Name:		jam
Summary:	A nice replacement for make
Version:	%{version}
Release:	%{?reldate:0.%reldate.}1
License:	MIT
Group:		Development/Other
URL:		https://equinox-project.org
Source0:	http://downloads.sourceforge.net/project/ede/%{name}/%{fullversion}/%{name}-%{fullversion}.tar.gz
BuildRequires:	bison

%description
Jam is a nice replacement for make (and the mess called Automake) providing
a good facility for writing sane compile scripts.

%prep
%setup -qn %{name}

%build
make

%install
export BINDIR="%{buildroot}%{_bindir}"
./jam0 install

%files
%attr (755,root,root) %{_bindir}/jam
%doc README README.CHANGES RELNOTES


%changelog
* Thu Jul 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.5-0.20080327.1
+ Revision: 809026
- imported package jam


* Sat Jan 06 2007 David Walluck <walluck@mandriva.org> 2.5-5mdv2007.0
+ Revision: 104968
- rebuild
  bunzip2 patches
- Import jam

* Fri Dec 23 2005 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 2.5-4mdk
- rebuild
- %%mkrel

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-3mdk
- rebuild

