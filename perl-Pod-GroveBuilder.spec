#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Pod
%define		pnam	GroveBuilder
Summary:	Pod::GroveBuilder perl module
Summary(pl.UTF-8):	Moduł perla Pod::GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	11
# same as perl (in README, COPYING says Artistic)
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af37328dd21b302a425092243bf365a0
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Pod-GroveBuilder/
Patch1:		%{name}-SGML-SPGroveBuilder.patch
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-SGML-SPGroveBuilder
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::GroveBuilder - module for creating SGML::Grove objects from POD
documents.

%description -l pl.UTF-8
Pod::GroveBuilder - moduł do tworzenia obiektów SGML::Grove z
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ChangeLog README
%{perl_vendorlib}/Pod/GroveBuilder.pm
%{_mandir}/man3/*
