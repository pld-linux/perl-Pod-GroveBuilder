%include	/usr/lib/rpm/macros.perl
Summary:	Pod-GroveBuilder perl module
Summary(pl):	Modu³ perla Pod-GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Pod/Pod-GroveBuilder-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	perl >= 5.005_03-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod-GroveBuilder - module for creating SGML::Grove objects from POD
documents.

%description -l pl
Pod-GroveBuilder - modu³ do tworzenia obiektów SGML::Grove z
dokumentów POD.

%prep
%setup -q -n Pod-GroveBuilder-%{version}
%patch -p0

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
