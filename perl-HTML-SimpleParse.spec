%include	/usr/lib/rpm/macros.perl
Summary:	HTML-SimpleParse perl module
Summary(pl):	Modu³ perla HTML-SimpleParse
Name:		perl-HTML-SimpleParse
Version:	0.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-SimpleParse-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-SimpleParse module.

%description -l pl
HTML-SimpleParse jest modu³em pozwalaj±cym analizowaæ pliki HTML.

%prep
%setup -q -n HTML-SimpleParse-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/SimpleParse
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/HTML/SimpleParse.pm
%{perl_sitearch}/auto/HTML/SimpleParse

%{_mandir}/man3/*
