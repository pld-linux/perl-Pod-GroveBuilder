%define	pdir	Pod
%define	pnam	GroveBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	Pod-GroveBuilder perl module
Summary(pl):	Modu³ perla Pod-GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	8

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
Patch1:		%{name}-SGML-SPGroveBuilder.patch
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod-GroveBuilder - module for creating SGML::Grove objects from POD
documents.

%description -l pl
Pod-GroveBuilder - modu³ do tworzenia obiektów SGML::Grove z
dokumentów POD.

%prep
%setup -q -n Pod-GroveBuilder-%{version}
%patch0 -p0
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Pod/GroveBuilder.pm
%{_mandir}/man3/*
