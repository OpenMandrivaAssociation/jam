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
URL:		http://equinox-project.org
Source0:	http://downloads.sourceforge.net/project/ede/%{name}/%{fullversion}/%{name}-%{fullversion}.tar.gz

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
