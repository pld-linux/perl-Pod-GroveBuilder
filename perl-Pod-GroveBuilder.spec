%include	/usr/lib/rpm/macros.perl
Summary:	Pod-GroveBuilder perl module
Summary(pl):	Modu³ perla Pod-GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Pod/Pod-GroveBuilder-%{version}.tar.gz
Patch0:		perl-Pod-GroveBuilder-man.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Pod/GroveBuilder
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,ChangeLog,README}.gz

%{perl_sitelib}/Pod/GroveBuilder.pm
%{perl_sitearch}/auto/Pod/GroveBuilder

%{_mandir}/man3/*
