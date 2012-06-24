%define	pdir	Pod
%define	pnam	GroveBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	Pod-GroveBuilder perl module
Summary(pl):	Modu� perla Pod-GroveBuilder
Name:		perl-Pod-GroveBuilder
Version:	0.01
Release:	8

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	�r�unart�l/Forritunarm�l/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Spr�k/Perl
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
Pod-GroveBuilder - modu� do tworzenia obiekt�w SGML::Grove z
dokument�w POD.

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
