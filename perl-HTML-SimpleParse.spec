%define	pdir	HTML
%define	pnam	SimpleParse
%include	/usr/lib/rpm/macros.perl
Summary:	HTML-SimpleParse perl module
Summary(pl):	Modu³ perla HTML-SimpleParse
Name:		perl-HTML-SimpleParse
Version:	0.10
Release:	6

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-SimpleParse module.

%description -l pl
HTML-SimpleParse jest modu³em pozwalaj±cym analizowaæ pliki HTML.

%prep
%setup -q -n HTML-SimpleParse-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/SimpleParse.pm
%{_mandir}/man3/*
