#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	GroveBuilder
Summary:	Pod::GroveBuilder perl module
Summary(pl):	Modu³ perla Pod::GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	10
# as perl itself in README, COPYING says Artistic
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af37328dd21b302a425092243bf365a0
Patch0:		%{name}-man.patch
Patch1:		%{name}-SGML-SPGroveBuilder.patch
BuildRequires:	perl-devel >= 5.6.1
%if %{with tests}
BuildRequires:	perl-SGML-SPGroveBuilder
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::GroveBuilder - module for creating SGML::Grove objects from POD
documents.

%description -l pl
Pod::GroveBuilder - modu³ do tworzenia obiektów SGML::Grove z
dokumentów POD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ChangeLog README
%{perl_vendorlib}/Pod/GroveBuilder.pm
%{_mandir}/man3/*
